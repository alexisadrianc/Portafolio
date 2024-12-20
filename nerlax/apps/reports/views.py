from django.shortcuts import render
from django.views.generic import TemplateView
from ..reports.forms import CeReportForm


class ceReportView(TemplateView):
    template_name = 'reports/ce_reports.html'

    def get_context_data(self, **kwargs):
        context = super(ceReportView, self).get_context_data(**kwargs)
        context['form'] = CeReportForm
        return context


