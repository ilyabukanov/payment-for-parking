var numberofdays
$("select").on('change', function(){
var nametickets = $('select option:selected' ).text();
$.ajax({
    type: "GET",
    url: "seasonticketprice",
    data: {
      'nametickets': nametickets,
    },
    dataType: "json",
    cache: false,
    success:function (nametickets){
        numberofdays = nametickets['numberofdays'];
        $("#id_price").val(nametickets['price']);
        const datestart = document.getElementById('id_startofvalidityperiod').value;
         let newDate = new Date(datestart);
         const curDateNum = newDate.getDate();
         newDate.setDate(curDateNum + Number(numberofdays));
         let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       if(datestart != "")
       {
                    $("#id_expirationdate").val(finalDateStr);
       }
    }
    });
});
window.onload = function() {
    let date = document.getElementById('id_startofvalidityperiod');
    date.addEventListener('change', function(event) {
         const datestart = document.getElementById('id_startofvalidityperiod').value;
         let newDate = new Date(datestart);
         const curDateNum = newDate.getDate();
         newDate.setDate(curDateNum + Number(numberofdays));
         let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       $("#id_expirationdate").val(finalDateStr);
    });
}