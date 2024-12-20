from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [


    path('list_activity/', login_required(ListActivityType.as_view()), name='list-activity'),
    path('create-activity/', login_required(CreateActivityType.as_view()), name='create-activity'),
    path('update-activity/<int:pk>', login_required(UpdateActivityType.as_view()), name='edit-activity'),
    path('delete-activity/<int:pk>', login_required(DeleteActivityType.as_view()), name='delete-activity'),
    path('import-activity/', login_required(UploadActivityType), name='import-activity'),

    path('kanban/', login_required(KanbanSupplier.as_view()), name='kanban-supplier'),
    path('list-supplier/', login_required(ListSupplier.as_view()), name='list-supplier'),
    path('create-supplier/', login_required(CreateSupplier.as_view()), name='create-supplier'),
    path('update-supplier/<int:pk>', login_required(UpdateSupplier.as_view()), name='edit-supplier'),
    path('delete-supplier/<int:pk>', login_required(DeleteSupplier.as_view()), name='delete-supplier'),

    path('list-classification/', login_required(ListClassification.as_view()), name='list-classification'),
    path('create-classification/', login_required(CreateClassifications.as_view()), name='create-classification'),
    path('update-classification/<int:pk>', login_required(UpdateClassifications.as_view()), name='edit-classification'),
    path('delete-classification/<int:pk>', login_required(DeleteClassifications.as_view()), name='delete-classification'),
    path('import-classification/', login_required(UploadClassification), name='import-classification'),

    path('list-services/', login_required(ListServices.as_view()), name='list-services'),
    path('create-services/', login_required(CreateServices.as_view()), name='create-services'),
    path('update-services/<int:pk>', login_required(UpdateServices.as_view()), name='edit-services'),
    path('delete-services/<int:pk>', login_required(DeleteServices.as_view()), name='delete-services'),
    path('import-services/', login_required(UploadServices), name='import-services'),

    path('list-state/', login_required(ListState.as_view()), name='list-state'),
    path('create-state/', login_required(CreateState.as_view()), name='create-state'),
    path('update-state/<int:pk>', login_required(UpdateState.as_view()), name='edit-state'),
    path('delete-state/<int:pk>', login_required(DeleteState.as_view()), name='delete-state'),
    path('import-state/', login_required(upload_states), name='import-state'),

    path('list-city/', login_required(ListCity.as_view()), name='list-city'),
    path('create-city/', login_required(CreateCity.as_view()), name='create-city'),
    path('update-city/<int:pk>', login_required(UpdateCity.as_view()), name='edit-city'),
    path('delete-city/<int:pk>', login_required(DeleteCity.as_view()), name='delete-city'),
    path('load_cities/', login_required(LoadCities), name='load-cities'),
    path('import-city/', login_required(UploadCity), name='import-city'),
]

urlpatterns += [
    path('activity_type/', login_required(TemplateView.as_view(template_name='settings/activity.html')), name='activity-type'),
    path('classification/', login_required(TemplateView.as_view(template_name='settings/classification.html')), name='classification'),
    path('services/', login_required(TemplateView.as_view(template_name='settings/services.html')), name='services'),
    path('supplier/', login_required(TemplateView.as_view(template_name='settings/supplier/list.html')), name='supplier'),
    path('state/', login_required(TemplateView.as_view(template_name='settings/state.html')), name='state'),
    path('city/', login_required(TemplateView.as_view(template_name='settings/city.html')), name='city'),
]
