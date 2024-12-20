$(document).ready(function() {
    $('#report_date').datepicker({
        changeYear: true,
        changeMonth: true,
    });
 })

function ceReportModalForm(url){
    $('#ceReportModal').load(url, function(){
        $(this).modal('show');
    });
}