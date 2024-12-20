$(document).ready(function() {
    $('#init_date').datepicker({
        changeYear: true,
        changeMonth: true,
    });
    $('#expiration_date').datepicker({
        changeYear: true,
        changeMonth: true,
    });
    $('#renovation_date').datepicker({
        changeYear: true,
        changeMonth: true,
    });
    $('#payment_date').datepicker({
        changeYear: true,
        changeMonth: true,
    });
    $('#payment_date_g').datepicker({
        changeYear: true,
        changeMonth: true,
    });

});

function list_building(){
    $.ajax({
       url: "/nerlax/list_building/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#building_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['amenities'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['unit_qty'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/nerlax/update/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="open_modal_building(\'/nerlax/delete/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#building_table tbody').append(row);
            }
            $('#building_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_building();
});

function update_building(){
//    activate_button();
    $.ajax({
        data: $('#edit_building_form').serialize(),
        url: $('#edit_building_form').attr('action'),
        type: $('#edit_building_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_building();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_building(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_building_form').attr('action'),
        type: $('#delete_building_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_building();
            $('#buildingModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function open_modal_building(url){
    $('#buildingModalDelete').load(url, function(){
        $(this).modal('show');
   });
}

function list_supplier_building(){
    $.ajax({
       url: "/nerlax/list_msupplier/",
        type: "get",
        dataType: "json",
        success: function(response){
            if ($.fn.DataTable.isDataTable('#msupplier_table')){
                ($('#msupplier_table').DataTable().destroy());
            }
            $('#msupplier_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td>' + response[i]['fields']['mobile'] + '</td>';
                row += '<td>' + response[i]['fields']['email'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/settings/update-supplier/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteSupplierForm(\'/settings/delete-supplier/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#msupplier_table tbody').append(row);
            }
            $('#msupplier_table').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

function addSupplier_form(url){
    $('#addSupplier').load(url, function(){
        $(this).modal('show');
    });
}

$("#id_region").change(function(){
    const region = $(this).val();
    const upd = $("#edit_building_form");
    const crear = $("#form-create-building");
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

//Unit
var $ = jQuery.noConflict()
function list_unit(){
    $.ajax({
       url: "/nerlax/list_unit/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#unit_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['building_id'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['meter_qty'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['garage'] + '</td>';
                row += '<td>' + response[i]['fields']['renter'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['init_date'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/nerlax/update_unit/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteUnitForm(\'/nerlax/delete_unit/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#unit_table tbody').append(row);
            }
            $('#unit_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

function create_unit(){
    $.ajax({
        data: $('#create_unit_form').serialize(),
        url: $('#create_unit_form').attr('action'),
        type: $('#create_unit_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function edit_unit(){
    $.ajax({
        data: $('#edit_unit_form').serialize(),
        url: $('#edit_unit_form').attr('action'),
        type: $('#edit_unit_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_unit(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_unit_form').attr('action'),
        type: $('#delete_unit_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
            $('#unitModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteUnitForm(url){
    $('#unitModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

$(document).ready(function(){
    list_unit();
});

//common expenses
function list_common_expenses(){
    $.ajax({
       url: "/nerlax/list_ce/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#common_expenses_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['building'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['payment_date'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['total_amount'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/nerlax/update_ce/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" width="24" height="24" style="-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); transform: rotate(360deg);" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M15.752 3a2.25 2.25 0 0 1 2.25 2.25v.753h.75a3.254 3.254 0 0 1 3.252 3.25l.003 5.997a2.249 2.249 0 0 1-2.248 2.25H18v1.25A2.25 2.25 0 0 1 15.75 21h-7.5A2.25 2.25 0 0 1 6 18.75V17.5H4.25A2.25 2.25 0 0 1 2 15.25V9.254a3.25 3.25 0 0 1 3.25-3.25l.749-.001L6 5.25A2.25 2.25 0 0 1 8.25 3h7.502zm-.002 10.5h-7.5a.75.75 0 0 0-.75.75v4.5c0 .414.336.75.75.75h7.5a.75.75 0 0 0 .75-.75v-4.5a.75.75 0 0 0-.75-.75zm3.002-5.996H5.25a1.75 1.75 0 0 0-1.75 1.75v5.996c0 .414.336.75.75.75H6v-1.75A2.25 2.25 0 0 1 8.25 12h7.5A2.25 2.25 0 0 1 18 14.25V16h1.783a.749.749 0 0 0 .724-.749l-.003-5.997a1.754 1.754 0 0 0-1.752-1.75zm-3-3.004H8.25a.75.75 0 0 0-.75.75l-.001.753h9.003V5.25a.75.75 0 0 0-.75-.75z" fill="currentColor"/></g><rect x="0" y="0" width="24" height="24" fill="rgba(0, 0, 0, 0)" /></svg></a>';
                row += '<a href="#" onclick="open_modal_form(\'/nerlax/delete_ce/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#common_expenses_table tbody').append(row);
            }
            $('#common_expenses_table').DataTable({
                "aLengthMenu": [[6, 12, 18, 24, -1], [6, 12, 18, 24, "All"]],
                "idDisplayLength": 6
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_common_expenses();
});

function update_ce(){
    $.ajax({
        data: $('#edit_ce_form').serialize(),
        url: $('#edit_ce_form').attr('action'),
        type: $('#edit_ce_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_common_expenses(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_ce_form').attr('action'),
        type: $('#delete_ce_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses();
            $('#commonExpensesModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function open_modal_form(url){
    $('#commonExpensesModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

//common expenses lines
function list_common_expenses_lines(){
    $.ajax({
       url: "/nerlax/list_ce_lines/",
       type: "get",
       dataType: "json",
       success: function(response){
            if ($.fn.DataTable.isDataTable('#ce_lines_table')){
                ($('#ce_lines_table').DataTable().destroy());
            }
            $('#ce_lines_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['concept'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['amount'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="#" onclick="editExpensesLinesForm(\'/nerlax/update_ce_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteExpensesLinesForm(\'/nerlax/delete_ce_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#ce_lines_table tbody').append(row);
            }
            $('#ce_lines_table').DataTable({
                dom: 'Brtip',
                buttons:
                {
                    name: 'primary',
                    buttons: []
                }
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_common_expenses_lines();
});

function addExpensesLinesForm(url){
    $('#expensesLinesModal').load(url, function(){
        $(this).modal('show');
    });
}

function editExpensesLinesForm(url){
    $('#expensesLinesModalEdit').load(url, function(){
        $(this).modal('show');
    });
}

function deleteExpensesLinesForm(url){
    $('#expensesLinesModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

function add_ce_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_create_data').serialize(),
        url: $('#form_create_data').attr('action'),
        type: $('#form_create_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses_lines();
            $('#expensesLinesModal').modal('hide');
        },
        error: function(error){
            console.log(error);
        }
    });
}

function edit_ce_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_edit_data').serialize(),
        url: $('#form_edit_data').attr('action'),
        type: $('#form_edit_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses_lines();
            $('#expensesLinesModalEdit').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_ce_lines(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_ce_lines_form').attr('action'),
        type: $('#delete_ce_lines_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses_lines();
            $('#expensesLinesModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

//garage
function list_garage(){
    $.ajax({
       url: "/nerlax/list_garage/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#garage_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['building'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['payment_date'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['total_amount'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/nerlax/update_garage/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" width="24" height="24" style="-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); transform: rotate(360deg);" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M15.752 3a2.25 2.25 0 0 1 2.25 2.25v.753h.75a3.254 3.254 0 0 1 3.252 3.25l.003 5.997a2.249 2.249 0 0 1-2.248 2.25H18v1.25A2.25 2.25 0 0 1 15.75 21h-7.5A2.25 2.25 0 0 1 6 18.75V17.5H4.25A2.25 2.25 0 0 1 2 15.25V9.254a3.25 3.25 0 0 1 3.25-3.25l.749-.001L6 5.25A2.25 2.25 0 0 1 8.25 3h7.502zm-.002 10.5h-7.5a.75.75 0 0 0-.75.75v4.5c0 .414.336.75.75.75h7.5a.75.75 0 0 0 .75-.75v-4.5a.75.75 0 0 0-.75-.75zm3.002-5.996H5.25a1.75 1.75 0 0 0-1.75 1.75v5.996c0 .414.336.75.75.75H6v-1.75A2.25 2.25 0 0 1 8.25 12h7.5A2.25 2.25 0 0 1 18 14.25V16h1.783a.749.749 0 0 0 .724-.749l-.003-5.997a1.754 1.754 0 0 0-1.752-1.75zm-3-3.004H8.25a.75.75 0 0 0-.75.75l-.001.753h9.003V5.25a.75.75 0 0 0-.75-.75z" fill="currentColor"/></g><rect x="0" y="0" width="24" height="24" fill="rgba(0, 0, 0, 0)" /></svg></a>';
                row += '<a href="#" onclick="deleteGarageForm(\'/nerlax/delete_garage/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#garage_table tbody').append(row);
            }
            $('#garage_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_garage();
});

function create_garage(){
    $.ajax({
        data: $('#create_garage_form').serialize(),
        url: $('#create_garage_form').attr('action'),
        type: $('#create_garage_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function update_garage(){
    $.ajax({
        data: $('#edit_garage_form').serialize(),
        url: $('#edit_garage_form').attr('action'),
        type: $('#edit_garage_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_garage(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_garage_form').attr('action'),
        type: $('#delete_garage_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage();
            $('#garageModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteGarageForm(url){
    $('#garageModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

function addGarageLinesForm(url){
    $('#garageLinesModal').load(url, function(){
        $(this).modal('show');
    });
}

function editGarageLinesForm(url){
    $('#garageLinesModalEdit').load(url, function(){
        $(this).modal('show');
    });
}

function deleteGarageLinesForm(url){
    $('#garageLinesModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

//garage lines
function list_garage_lines(){
    $.ajax({
       url: "/nerlax/list_garage_lines/",
       type: "get",
       dataType: "json",
       success: function(response){
            if ($.fn.DataTable.isDataTable('#garage_lines_table')){
                ($('#garage_lines_table').DataTable().destroy());
            }
            $('#garage_lines_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['apartment'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['amount'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['is_paid'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="#" onclick="editGarageLinesForm(\'/nerlax/update_garage_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteGarageLinesForm(\'/nerlax/delete_garage_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#garage_lines_table tbody').append(row);
            }
            $('#garage_lines_table').DataTable({
                dom: 'Brtip',
                buttons:
                {
                    name: 'primary',
                    buttons: []
                }
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

function list_garage_lines_sm(){
    $.ajax({
       url: "/nerlax/list_garage_lines_sm/",
       type: "get",
       dataType: "json",
       success: function(response){
            if ($.fn.DataTable.isDataTable('#garage_lines_table')){
                ($('#garage_lines_table').DataTable().destroy());
            }
            $('#garage_lines_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['apartment'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['amount'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['is_paid'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="#" onclick="editGarageLinesForm(\'/nerlax/update_garage_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteGarageLinesForm(\'/nerlax/delete_garage_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#garage_lines_table tbody').append(row);
            }
            $('#garage_lines_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_garage_lines();
});

function add_garage_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_create_data').serialize(),
        url: $('#form_create_data').attr('action'),
        type: $('#form_create_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage_lines();
            $('#garageLinesModal').modal('hide');
        },
        error: function(error){
            console.log(error);
        }
    });
}

function edit_garage_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_edit_data').serialize(),
        url: $('#form_edit_data').attr('action'),
        type: $('#form_edit_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage_lines();
            $('#garageLinesModalEdit').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_garage_lines(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#form_delete_data').attr('action'),
        type: $('#form_delete_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_garage_lines();
            $('#garageLinesModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}