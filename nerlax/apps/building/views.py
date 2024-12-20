from django.shortcuts import *
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.views.generic import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from .forms import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Home(request):
    if request.user.user_type == '2':
        return redirect(reverse('home_employee'))
    elif request.user.user_type == '1':
        return redirect(reverse('home_client'))
    else:
        return redirect(reverse(template_name='home.html'))


def HomeEmployee(request):
    return render(request, template_name='dashboard.html')


def HomeClient(request):
    return render(request, template_name='dashboard_client.html')


class ListBuilding(ListView):
    model = Building
    context_object_name = 'buildings'
    queryset = model.objects.filter(state=True)
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True),
                                'application/json')
        else:
            return redirect('nerlax:building')


class CreateBuilding(CreateView):
    model = Building
    form_class = buildingForm
    template_name = 'buildings/building/create.html'
    success_message = 'Success: Building was created.'
    success_url = reverse_lazy('nerlax:building')


class UpdateBuilding(UpdateView):
    model = Building
    form_class = buildingForm
    template_name = 'buildings/building/edit.html'

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
            return redirect('nerlax:building')


class DeleteBuilding(DeleteView):
    model = Building
    template_name = 'buildings/building/delete.html'

    def post(self, request, *args, **kwargs):
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
            return redirect('nerlax:building')


class ListSupplier(ListView):
    model = Supplier
    context_object_name = 'supplier'
    template_name = 'buildings/building/add_modals.html'
    queryset = model.objects.filter(state=True)
    paginate_by = 10

    # def get(self, request, *args, **kwargs):
    #     if is_ajax(request=request):
    #         return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
    #     else:
    #         return redirect('nerlax:create-building')


class ListUnit(ListView):
    model = Unit
    context_object_name = 'units'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True),
                                'application/json')
        else:
            return redirect('nerlax:unit')


class CreateUnit(CreateView):
    model = Unit
    form_class = unitForm
    template_name = 'buildings/units/create.html'
    success_message = 'Success: Unit was created.'
    success_url = reverse_lazy('nerlax:unit')


class UpdateUnit(UpdateView):
    model = Unit
    form_class = unitForm
    template_name = 'buildings/units/edit.html'

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
            return redirect('nerlax:unit')


class DeleteUnit(DeleteView):
    model = Unit
    template_name = 'buildings/units/delete.html'

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
            return redirect('nerlax:unit')


class ListCommonExpenses(ListView):
    model = CommonExpenses
    context_object_name = 'expenses'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True),
                                'application/json')
        else:
            return redirect('nerlax:common-expenses')


class CreateCommonExpenses(CreateView):
    model = CommonExpenses
    form_class = commonExpensesForm
    template_name = 'buildings/common_expenses/create.html'
    success_message = 'Success: Common Expenses was created.'
    success_url = reverse_lazy('nerlax:common-expenses')


class UpdateCommonExpenses(UpdateView):
    model = CommonExpenses
    form_class = commonExpensesForm
    template_name = 'buildings/common_expenses/edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        lines = list(CommonExpensesLines.objects.filter(state=True, common_expenses=self.kwargs.get('pk')).
                     values_list('id', 'concept', 'amount',))
        print(lines)
        return super(UpdateCommonExpenses, self).get(request, *args, **kwargs)

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
            return redirect('nerlax:common-expensese')


class DeleteCommonExpenses(DeleteView):
    model = CommonExpenses
    template_name = 'buildings/common_expenses/delete.html'

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
            return redirect('nerlax:common-expenses')


class ListCommonExpensesLines(ListView):
    model = CommonExpensesLines
    context_object_name = 'expenses_lines'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        lines = list(CommonExpensesLines.objects.filter(state=True).values_list('id', 'common_expenses', 'concept', 'amount'))
        common_expenses = list(CommonExpenses.objects.filter(state=True).values_list('id', 'total_amount'))
        print(lines)
        print(common_expenses)
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True),
                                'application/json')
        else:
            return redirect('nerlax:ce-lines')


class CreateCommonExpensesLines(CreateView):
    model = CommonExpensesLines
    form_class = commonExpensesLinesForm
    template_name = 'buildings/common_expenses/lines/create_lines.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                line = CommonExpensesLines(
                    concept=form.cleaned_data.get('concept'),
                    amount=form.cleaned_data.get('amount'),
                    common_expenses=form.cleaned_data.get('common_expenses')
                )
                line.save()
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
            return redirect('nerlax:create-ce')


class UpdateCommonExpensesLines(UpdateView):
    model = CommonExpensesLines
    form_class = commonExpensesLinesForm
    template_name = 'buildings/common_expenses/lines/edit_lines.html'

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
            return redirect('nerlax:create-ce')


class DeleteCommonExpensesLines(DeleteView):
    model = CommonExpensesLines
    template_name = 'buildings/common_expenses/lines/delete_lines.html'

    def post(self, request, *args, **kwargs):
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
            return redirect('nerlax:create-ce')


class ListGarage(ListView):
    model = Garage
    context_object_name = 'garages'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(
                serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('nerlax:garage')


class CreateGarage(CreateView):
    model = Garage
    form_class = GarageForm
    template_name = 'buildings/garage/create.html'
    success_message = 'Success: Garage was created.'
    success_url = reverse_lazy('nerlax:garage')


class UpdateGarage(UpdateView):
    model = Garage
    form_class = GarageForm
    template_name = 'buildings/garage/edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        lines = list(GarageLines.objects.filter(state=True, garage=self.kwargs.get('pk')).values_list('id', 'apartment',
                                                                                                      'amount',
                                                                                                      'is_paid'))
        print(lines)
        return super(UpdateGarage, self).get(request, *args, **kwargs)

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
            return redirect('nerlax:garage')


class DeleteGarage(DeleteView):
    model = Garage
    template_name = 'buildings/garage/delete.html'

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
            return redirect('nerlax:garage')


class ListGarageLines(ListView):
    model = GarageLines
    context_object_name = 'lines_garages'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(
                serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('nerlax:create-garage')


class ListGarageLinesSm(ListView):
    model = GarageLines
    context_object_name = 'garages_sm'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(
                serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('nerlax:garage-lines-sm')


class CreateGarageLines(CreateView):
    model = GarageLines
    form_class = GarageLinesForm
    template_name = 'buildings/garage/lines/create_lines.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                line = GarageLines(
                    apartment=form.cleaned_data.get('apartment'),
                    amount=form.cleaned_data.get('amount'),
                    garage=form.cleaned_data.get('garage'),
                    is_paid=form.cleaned_data.get('is_paid'),
                    voucher=form.cleaned_data.get('voucher'),
                )
                line.save()
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
            return redirect('nerlax:create-garage')


class UpdateGarageLines(UpdateView):
    model = GarageLines
    form_class = GarageLinesForm
    template_name = 'buildings/garage/lines/edit_lines.html'

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, request.FILES, instance=self.get_object())
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
            return redirect('nerlax:create-garage')


class DeleteGarageLines(DeleteView):
    model = GarageLines
    template_name = 'buildings/garage/lines/delete_lines.html'

    def post(self, request, *args, **kwargs):
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
            return redirect('nerlax:create-garage')
