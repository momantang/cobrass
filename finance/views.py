from django.shortcuts import render
from finance.models import StockIndexSnapShot, CronJob
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.conf import settings

import easyquotation
import pandas as pd
import QUANTAXIS as qa


# Create your views here.

def index(request):
    # stock_index_snapshot = StockIndexSnapShot.objects.last()
    quotation = easyquotation.use('sina')
    indexs = quotation.stocks(['sh000001', 'sz399001', 'sh000300', 'sz399006'], prefix=True)
    df_indexs = pd.DataFrame.from_dict(indexs).T
    dicts = df_indexs.to_dict()
    print(dicts)
    return render(request, 'finance/index.html', {'dicts': dicts})


def update_cronjob(request):
    cronjobs = settings.COBRASS_DESCRIBE_CRONJOBS
    CronJob.objects.all().delete()
    for cj in cronjobs:
        cronjob = CronJob()
        cronjob.job_name = cj[0]
        cronjob.frequency = cj[1]
        cronjob.frequency_cron = cj[2]
        cronjob.method = cj[3]
        cronjob.describe = cj[4]
        cronjob.save()
    return HttpResponseRedirect('/cronjob')


class CronjobView(generic.ListView):
    template_name = 'finance/cronjob.html'
    context_object_name = 'cronjob_list'

    def get_queryset(self):
        return CronJob.objects.all()


def html_page(request, page='about'):
    res = dict()
    if page == 'projects':
        res = {'quantaxis': qa.__version__}
        print('projects')
    return render(request, 'finance/{}.html'.format(page), {'res': res})
