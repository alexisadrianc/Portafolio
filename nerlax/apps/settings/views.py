import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.views.generic import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Activity Types
class ListActivityType(ListView):
    model = ActivityType
    context_object_name = 'activity'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:activity-type')


class CreateActivityType(CreateView):
    model = ActivityType
    form_class = ActivityTypeForm
    template_name = 'settings/activity/create.html'
    success_message = 'Success: Activity type was created.'
    success_url = reverse_lazy('settings:activity-type')


class UpdateActivityType(UpdateView):
    model = ActivityType
    form_class = ActivityTypeForm
    template_name = 'settings/activity/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:activity-type')


class DeleteActivityType(DeleteView):
    model = ActivityType
    template_name = 'settings/activity/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:activity-type')


def UploadActivityType(request):
    template_name = 'settings/import/import_activity.html'

    prompt = {
        'order': 'Order of the CSV should by Name, Description'
    }

    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_files = request.FILES['file_activity']

    if not csv_files.name.endswith('.csv'):
        return HttpResponse("This is not a csv file")

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = ActivityType.objects.update_or_create(
            name=column[0],
            description=column[1],
        )
    messages.success(request, 'Your csv file has been imported successfully =)', extra_tags='alert-success')
    return HttpResponseRedirect(reverse_lazy('settings:activity-type'))


# Classifications
class ListClassification(ListView):
    model = Classification
    context_object_name = 'classification'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:classification')


class CreateClassifications(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'settings/classification/create.html'
    success_message = 'Success: Classification was created.'
    success_url = reverse_lazy('settings:classification')


class UpdateClassifications(UpdateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'settings/classification/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:classification')


class DeleteClassifications(DeleteView):
    model = Classification
    template_name = 'settings/classification/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:classification')


def UploadClassification(request):
    template_name = 'settings/import/import_classification.html'

    prompt = {
        'order': 'Order of the CSV should by Name, Description'
    }

    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_files = request.FILES['file_classification']

    if not csv_files.name.endswith('.csv'):
        return HttpResponse("This is not a csv file")

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Classification.objects.update_or_create(
            name=column[0],
            description=column[1],
        )
    messages.success(request, 'Your csv file has been imported '
                              'successfully =)', extra_tags='alert-success')
    return HttpResponseRedirect(reverse_lazy('settings:classification'))

# Services types
class ListServices(ListView):
    model = Services
    context_object_name = 'services'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('settings:services')


class CreateServices(CreateView):
    model = Services
    form_class = ServicesForm
    template_name = 'settings/services/create.html'
    success_message = 'Success: Services type was created.'
    success_url = reverse_lazy('settings:services')


class UpdateServices(UpdateView):
    model = Services
    form_class = ServicesForm
    success_message = 'Success: Services type was updated.'
    template_name = 'settings/services/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:services')


class DeleteServices(DeleteView):
    model = Services
    template_name = 'settings/services/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:services')


def UploadServices(request):
    template_name = 'settings/import/city_import.html'

    prompt = {
        'order': 'Order of the CSV should by Name, Supplier'
    }

    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_files = request.FILES['file_services']

    if not csv_files.name.endswith('.csv'):
        return HttpResponse("This is not a csv file")

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        supplier_id = Supplier.objects.get(nro_documento=column[1])
        _, created = Services.objects.update_or_create(
            name=column[0],
            supplier=supplier_id,
        )
    messages.success(request, 'Your csv file has been imported successfully =)', extra_tags='alert-success')
    return HttpResponseRedirect(reverse_lazy('settings:services'))


# Supplier
class KanbanSupplier(ListView):
    model = Supplier
    template_name = 'settings/supplier.html'
    context_object_name = 'supplier'
    queryset = model.objects.filter(state=True)
    paginate_by = 24


class ListSupplier(ListView):
    model = Supplier
    context_object_name = 'supplier'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:supplier')


class CreateSupplier(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'settings/supplier/create.html'
    success_message = 'Success: Supplier was created.'
    success_url = reverse_lazy('settings:kanban-supplier')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(data=request.POST, files=request.FILES)
            if form.is_valid():
                new_supplier = Supplier(
                    name=form.cleaned_data.get('name'),
                    address=form.cleaned_data.get('address'),
                    address2=form.cleaned_data.get('address2'),
                    city=form.cleaned_data.get('city'),
                    postal_code=form.cleaned_data.get('postal_code'),
                    region=form.cleaned_data.get('region'),
                    mobile=form.cleaned_data.get('mobile'),
                    email=form.cleaned_data.get('email'),
                    nro_documento=form.cleaned_data.get('nro_documento'),
                    logo=form.cleaned_data.get('logo'),
                )
                new_supplier.save()
                msj = f'{self.model.__name__} created successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not created !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:supplier')


class UpdateSupplier(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'settings/supplier/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:supplier')


class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'settings/supplier/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:supplier')


# State
class ListState(ListView):
    model = State
    context_object_name = 'state'
    queryset = model.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:state')


class CreateState(CreateView):
    model = State
    form_class = StateForm
    template_name = 'settings/state/create.html'
    success_message = 'Success: State was created.'
    success_url = reverse_lazy('settings:state')


class UpdateState(UpdateView):
    model = State
    form_class = StateForm
    success_message = 'Success: State was updated.'
    template_name = 'settings/state/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:state')


class DeleteState(DeleteView):
    model = State
    template_name = 'settings/state/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.active = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:state')


def upload_states(request):
    template_name = 'settings/import/state_import.html'

    prompt = {
        'order': 'Order of the CSV should by State, Code'
    }

    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_files = request.FILES['file_state']

    if not csv_files.name.endswith('.csv'):
        return HttpResponse("This is not a csv file")

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = State.objects.update_or_create(
            name=column[0],
            code=column[1]
        )
    messages.success(request, 'Your csv file has been imported '
                              'successfully =)', extra_tags='alert-success')
    return HttpResponseRedirect(reverse_lazy('settings:state'))


# City
class ListCity(ListView):
    model = City
    context_object_name = 'city'
    queryset = model.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('settings:city')


class CreateCity(CreateView):
    model = City
    form_class = CityForm
    template_name = 'settings/city/create.html'
    success_message = 'Success: City was created.'
    success_url = reverse_lazy('settings:city')


class UpdateCity(UpdateView):
    model = City
    form_class = CityForm
    success_message = 'Success: City was updated.'
    template_name = 'settings/city/edit.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:city')


class DeleteCity(DeleteView):
    model = City
    template_name = 'settings/city/delete.html'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=request):
            object = self.get_object()
            object.active = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('settings:city')


def LoadCities(request):
    region_id = request.GET.get('region')
    cities = City.objects.filter(state=region_id)
    return JsonResponse(list(cities.values('id', 'name')), safe=False)


def UploadCity(request):
    template_name = 'settings/import/city_import.html'

    prompt = {
        'order': 'Order of the CSV should by City, Code, State'
    }

    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_files = request.FILES['file_city']

    if not csv_files.name.endswith('.csv'):
        return HttpResponse("This is not a csv file")

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        state_id = State.objects.get(code=column[2])
        _, created = City.objects.update_or_create(
            name=column[0],
            code=column[1],
            state=state_id,
        )
    messages.success(request, 'Your csv file has been imported '
                              'successfully =)', extra_tags='alert-success')
    return HttpResponseRedirect(reverse_lazy('settings:city'))
