from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


from .views import *

urlpatterns = [
    path('ce_report/', login_required(ceReportView.as_view()), name='report-ce'),
    ]
