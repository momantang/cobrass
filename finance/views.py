from django.shortcuts import render
from finance.models import StockIndexSnapShot, CronJob
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.conf import settings


# Create your views here.

def index(request):
    # stock_index_snapshot = StockIndexSnapShot.objects.last()

    return render(request, 'finance/index.html')


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
    return render(request, 'finance/{}.html'.format(page))
