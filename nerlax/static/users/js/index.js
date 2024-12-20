//User
function list_user(){
    $.ajax({
        url: "/list_user/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#table_users tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['first_name'] + '</td>';
                row += '<td>' + response[i]['fields']['last_name'] + '</td>';
                row += '<td>' + response[i]['fields']['username'] + '</td>';
                row += '<td>' + response[i]['fields']['email'] + '</td>';
                row += '<td>' + response[i]['fields']['user_type'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/edit/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a> ';
                row += '<a href="#" onclick="deleteUsersForm(\'/delete/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#table_users tbody').append(row);
            }
            $('#table_users').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_user();
});

function create_users(){
//    activate_button();
    $.ajax({
        data: $('#create_user_form').serialize(),
        url: $('#create_user_form').attr('action'),
        type: $('#create_user_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function update_users(){
//    activate_button();
    $.ajax({
        data: $('#edit_user_form').serialize(),
        url: $('#edit_user_form').attr('action'),
        type: $('#edit_user_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_users(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_users_form').attr('action'),
        type: $('#delete_users_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
            $('#usersModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteUsersForm(url){
    $('#usersModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

function changePasswordModalForm(){
    $('#changePasswordModal').load(function(){
        $(this).modal('show');
    });
}

//Company
function list_company(){
    $.ajax({
        url: "/list-company/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#table_companies tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['rut_dgi'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/update-company/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteCompanyForm(\'/delete-company/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#table_companies tbody').append(row);
            }
            $('#table_companies').DataTable();
        },
        error:function(error){
            alert(error);
        }
    });
}

$(document).ready(function(){
    list_company();
});

function create_company(){
    var data = new FormData($('#create_company_form').get(0));
    $.ajax({
        data: data,
        url: $('#create_company_form').attr('action'),
        type: $('#create_company_form').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function(response){
            notificationSuccess(response.msj);
            list_company();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function update_company(){
    $.ajax({
        data: $('#edit_company_form').serialize(),
        url: $('#edit_company_form').attr('action'),
        type: $('#edit_company_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_company();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_company(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_company_form').attr('action'),
        type: $('#delete_company_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_company();
            $('#companyDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteCompanyForm(url){
    $('#companyDelete').load(url, function(){
        $(this).modal('show');
     });
}

//Group
function list_rol(){
    $.ajax({
        url: "/list-rol/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#table_rol tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/update-rol/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteGroupModalForm(\'/delete-rol/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#table_rol tbody').append(row);
            }
            $('#table_rol').DataTable();
        },
        error:function(error){
            alert(error);
        }
    });
}

$(document).ready(function(){
    list_rol();
});

function update_rol(){
    $.ajax({
        data: $('#edit-rol-form').serialize(),
        url: $('#edit-rol-form').attr('action'),
        type: $('#edit-rol-form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_rol();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_rol(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete-rol-form').attr('action'),
        type: $('#delete-rol-form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_rol();
            $('#rolDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteGroupModalForm(url){
    $('#rolDelete').load(url, function(){
        $(this).modal('show');
     });
}