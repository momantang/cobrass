# coding: utf-8
import dash
import dash_core_components as dcc
import dash_html_components as html

import colorlover as cl
import datetime as dt
import flask
import os
import pandas as pd
from pandas_datareader.data import DataReader
import time
import tushare as ts

server = flask.Flask('stock-tickers')
app = dash.Dash('stock-tickers', server=server, url_base_pathname='/dash/gallery/stock-tickers/', csrf_protect=False)
server.secret_key = os.environ.get('secret_key', 'secret')

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-finance-1.28.0.min.js'

colorscale = cl.scales['10']['qual']['Paired']

# df_symbol = pd.read_csv('tickers.csv')
df_symbol = ts.get_stock_basics()

app.layout = html.Div([
    html.Div([
        html.H2('Tushare Explorer',
                style={'display': 'inline',
                       'float': 'left',
                       'font-size': '2.65em',
                       'margin-left': '7px',
                       'font-weight': 'bolder',
                       'font-family': 'Product Sans',
                       'color': "rgba(117, 117, 117, 0.95)",
                       'margin-top': '20px',
                       'margin-bottom': '0'
                       }),
        html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                style={
                    'height': '100px',
                    'float': 'right'
                },
        ),
    ]),
    dcc.Dropdown(
        id='stock-ticker-input',
        options=[{'label': s[0]+'-'+s[1], 'value': s[0]+'-'+s[1]}
                 for s in zip(df_symbol.name, df_symbol.index)],
        value=['旭升股份-603305'],
        multi=True
    ),
    html.Div(id='graphs')
], className="container")

def bbands(price, window_size=10, num_of_std=5):

    rolling_mean = price.rolling(window=window_size).mean().resample('D').asfreq().ffill()
    rolling_std  = price.rolling(window=window_size).std().resample('D').asfreq().ffill()

    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    # print(rolling_mean)
    return rolling_mean, upper_band, lower_band

@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('stock-ticker-input', 'value')])
def update_graph(tickers):
    graphs = []
    for i, ticker in enumerate(tickers):
        try:
            df = ts.get_hist_data(ticker[-6:], 
                            str(dt.datetime.now()-dt.timedelta(30*6))[0:10],
                            str(dt.datetime.now())[0:10])
            df = processing_df(df) # 把缺失的日期数据补全
        except:
            graphs.append(html.H3(
                'Data is not available for {}'.format(ticker),
                style={'marginTop': 20, 'marginBottom': 20}
            ))
            continue

        candlestick = {
            'x': df.index,
            'open': df['open'],
            'high': df['high'],
            'low': df['low'],
            'close': df['close'],
            'type': 'candlestick',
            'name': ticker,
            # 'showlegend': False,
            # 'legendgroup': ticker,
            'xaxis': {'rangeslider':{'visible':False}, 'rangeselector':{'visible':False}},
            'connectgaps': True,
            'increasing': {'line': {'color': colorscale[5]}},
            'decreasing': {'showlegend': False,'line': {'color': colorscale[3]}},
        }
       

        avg_lines = [df.ma5, df.ma20]
        avg_traces = [{
            'x': df.index, 'y': y,
            'type': 'scatter', 'mode': 'lines',
            'line': {'width': 1, 'color': colorscale[(i*2) % len(colorscale)]},
            'hoverinfo': 'none',
            'connectgaps': True,
            'showlegend': True if i == -1 else False,
        } for i, y in enumerate(avg_lines)]

        graphs.append(dcc.Graph(
            id=ticker,
            figure={
                'data': [candlestick] + avg_traces,
                'layout': {
                    'margin': {'b': 0, 'r': 10, 'l': 60, 't': 0},
                    'legend': {'x': 0}
                }
            }
        ))

    return graphs


def processing_df(df):
    df = df.sort_index()
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    df = df.resample('D').asfreq()
    df.close.ffill(inplace=True)
    df.open.fillna(df.close, inplace=True)
    df.high.fillna(df.close, inplace=True)
    df.low.fillna(df.close, inplace=True)

    df.price_change.fillna(0, inplace=True)
    df.p_change.fillna(0, inplace=True)
    df.turnover.fillna(-1, inplace=True)
    df.ffill(inplace=True)
    
    return df

external_css = ["https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2cc54b8c03f4126569a3440aae611bbef1d7a5dd/stylesheet.css"]

for css in external_css:
    app.css.append_css({"external_url": css})


if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })


if __name__ == '__main__':
    app.run_server(debug=True)
