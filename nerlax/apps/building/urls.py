from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *

urlpatterns = [

    path('list_unit/', login_required(ListUnit.as_view()), name='list-unit'),
    path('create_unit/', login_required(CreateUnit.as_view()), name='create-unit'),
    path('update_unit/<int:pk>', login_required(UpdateUnit.as_view()), name='update-unit'),
    path('delete_unit/<int:pk>', login_required(DeleteUnit.as_view()), name='delete-unit'),


    path('list_building/', login_required(ListBuilding.as_view()), name='list-building'),
    path('list_msupplier/', login_required(ListSupplier.as_view()), name='list-msupplier'),
    path('create/', login_required(CreateBuilding.as_view()), name='create-building'),
    path('update/<int:pk>', login_required(UpdateBuilding.as_view()), name='update-building'),
    path('delete/<int:pk>', login_required(DeleteBuilding.as_view()), name='delete-building'),

    path('list_ce/', login_required(ListCommonExpenses.as_view()), name='list-ce'),
    path('create_ce/', login_required(CreateCommonExpenses.as_view()), name='create-ce'),
    path('update_ce/<int:pk>', login_required(UpdateCommonExpenses.as_view()), name='update-ce'),
    path('delete_ce/<int:pk>', login_required(DeleteCommonExpenses.as_view()), name='delete-ce'),

    path('list_ce_lines/', login_required(ListCommonExpensesLines.as_view()), name='list-ce-lines'),
    path('create_ce_lines/', login_required(CreateCommonExpensesLines.as_view()), name='create-ce-lines'),
    path('update_ce_lines/<int:pk>', login_required(UpdateCommonExpensesLines.as_view()), name='update-ce-lines'),
    path('delete_ce_lines/<int:pk>', login_required(DeleteCommonExpensesLines.as_view()), name='delete-ce-lines'),

    path('list_garage/', login_required(ListGarage.as_view()), name='list-garage'),
    path('create_garage/', login_required(CreateGarage.as_view()), name='create-garage'),
    path('update_garage/<int:pk>', login_required(UpdateGarage.as_view()), name='update-garage'),
    path('delete_garage/<int:pk>', login_required(DeleteGarage.as_view()), name='delete-garage'),

    path('list_garage_lines/', login_required(ListGarageLines.as_view()), name='list-garage-lines'),
    path('list_garage_lines_sm/', login_required(ListGarageLinesSm.as_view()), name='list-garage-lines-sm'),
    path('create_garage_lines/', login_required(CreateGarageLines.as_view()), name='create-garage-lines'),
    path('update_garage_lines/<int:pk>', login_required(UpdateGarageLines.as_view()), name='update-garage-lines'),
    path('delete_garage_lines/<int:pk>', login_required(DeleteGarageLines.as_view()), name='delete-garage-lines'),
]

urlpatterns += [
    path('unit/', login_required(TemplateView.as_view(template_name='buildings/unit.html')), name='unit'),
    path('building/', login_required(TemplateView.as_view(template_name='buildings/building.html')), name='building'),
    path('common-expenses/', login_required(TemplateView.as_view(template_name='buildings/common_expenses.html')), name='common-expenses'),
    path('ce_lines/', login_required(TemplateView.as_view(template_name='buildings/common_expenses/create.html')), name='ce-lines'),
    path('garage/', login_required(TemplateView.as_view(template_name='buildings/garage.html')), name='garage'),
    path('garage_lines/', login_required(TemplateView.as_view(template_name='buildings/garage/create.html')), name='garage-lines'),
    path('garage_lines_sm/', login_required(TemplateView.as_view(template_name='buildings/garage/lines/list_lines.html')), name='garage-lines-sm'),
]
