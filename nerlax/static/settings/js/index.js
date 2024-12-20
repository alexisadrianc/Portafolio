//State
function list_state(){
    $.ajax({
        url: "/settings/list-state/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#state_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['code'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-state/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteStateForm(\'/settings/delete-state/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#state_table tbody').append(row);
            }
            $('#state_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_state();
});

function update_state(){
    $.ajax({
        data: $('#edit_state_form').serialize(),
        url: $('#edit_state_form').attr('action'),
        type: $('#edit_state_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_state();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_state(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_state_form').attr('action'),
        type: $('#delete_state_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_state();
            $('#stateDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteStateForm(url){
    $('#stateDelete').load(url, function(){
        $(this).modal('show');
    });
}

var $ = jQuery.noConflict();

function importStateFile(url){
    $('#importFile').load(url, function(){
        $(this).modal('show');
    });
}

//City
function list_city(){
    $.ajax({
        url: "/settings/list-city/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#city_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['code'] + '</td>';
                row += '<td>' + response[i]['fields']['state'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-city/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteCityForm(\'/settings/delete-city/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#city_table tbody').append(row);
            }
            $('#city_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_city();
});

function update_city(){
    $.ajax({
        data: $('#edit_city_form').serialize(),
        url: $('#edit_city_form').attr('action'),
        type: $('#edit_city_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_city();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_city(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_city_form').attr('action'),
        type: $('#delete_city_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_city();
            $('#cityDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteCityForm(url){
    $('#cityDelete').load(url, function(){
        $(this).modal('show');
    });
}

//Activity
function list_activity(){
    $.ajax({
        url: "/settings/list_activity/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#activity_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-activity/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteActivityForm(\'/settings/delete-activity/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#activity_table tbody').append(row);
            }
            $('#activity_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_activity();
});

function edit_activity(){
//    activate_button();
    $.ajax({
        data: $('#edit_activity_form').serialize(),
        url: $('#edit_activity_form').attr('action'),
        type: $('#edit_activity_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_activity();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_activity(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_activity_form').attr('action'),
        type: $('#delete_activity_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_activity();
            $('#activityTypeDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteActivityForm(url){
    $('#activityTypeDelete').load(url, function(){
        $(this).modal('show');
    });
}

//Classification
function list_classification(){
    $.ajax({
        url: "/settings/list-classification/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#classification_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-classification/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteClassificationForm(\'/settings/delete-classification/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#classification_table tbody').append(row);
            }
            $('#classification_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_classification();
});

function update_classification(){
//    activate_button();
    $.ajax({
        data: $('#edit_classification_form').serialize(),
        url: $('#edit_classification_form').attr('action'),
        type: $('#edit_classification_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_classification();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_classification(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_property_form').attr('action'),
        type: $('#delete_property_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_classification();
            $('#classificationDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteClassificationForm(url){
    $('#classificationDelete').load(url, function(){
        $(this).modal('show');
    });
}

//Supplier
function list_supplier(){
    $.ajax({
        url: "/settings/list-supplier/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#supplier_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td>' + response[i]['fields']['mobile'] + '</td>';
                row += '<td>' + response[i]['fields']['email'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-supplier/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteSupplierForm(\'/settings/delete-supplier/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#supplier_table tbody').append(row);
            }
            $('#supplier_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_supplier();
});

function create_supplier(){
    var data = new FormData($('#create_supplier_form').get(0));
    $.ajax({
        data: data,
        url: $('#create_supplier_form').attr('action'),
        type: $('#create_supplier_form').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function(response){
            notificationSuccess(response.msj);
            list_supplier();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function update_supplier(){
//    activate_button();
    var data = new FormData($('#edit_supplier_form').get(0));
    $.ajax({
        data: data,
        url: $('#edit_supplier_form').attr('action'),
        type: $('#edit_supplier_form').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function(response){
            notificationSuccess(response.msj);
            list_supplier();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_supplier(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_supplier_form').attr('action'),
        type: $('#delete_supplier_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_supplier();
            $('#supplierModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteSupplierForm(url){
    $('#supplierModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

$("#id_region").change(function(){
    const region = $(this).val();
    const upd = $("#edit_supplier_form");
    const crear = $("#create_supplier_form");
    if (upd.length > 0){
        formulario = upd;
    }else{
        formulario =crear;
    }
    const url = formulario.attr("data-cities-url")
    $.ajax({
        url: url,
        data: {
            'region': region
        },
        success: function(data){
            let html_data = '<option value="">--------</option>';
            data.forEach(function(city){
                html_data += `<option value="${city.id}">${city.name}</option>`
            });
            $("#id_city").html(html_data);
        }
    })
})

//Services
function list_services(){
    $.ajax({
        url: "/settings/list-services/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#services_type_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-services/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteServicesForm(\'/settings/delete-services/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#services_type_table tbody').append(row);
            }
            $('#services_type_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_services();
});

function update_services(){
    $.ajax({
        data: $('#edit_services_form').serialize(),
        url: $('#edit_services_form').attr('action'),
        type: $('#edit_services_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_services();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_services(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_services_form').attr('action'),
        type: $('#delete_services_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_services();
            $('#servicesTypesDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteServicesForm(url){
    $('#servicesTypesDelete').load(url, function(){
        $(this).modal('show');
    });
}