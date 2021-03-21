$("select").on('change', function(){
var adress = $('select option:selected' ).text();
$.ajax({
    type: "GET",
    url: "valuesubstitution",
    data: {
      'adress': adress,
    },
    dataType: "json",
    cache: false,
    success:function (data){
    price = data['price']
       $("#id_price").val(data['price'])
       var mintime = parseInt(data['minimaltimeforpayment'])
       var pricevalue = $("#id_price").val()
       var finalprice = mintime * price
       document.getElementById('id_amountoftime').setAttribute('min', mintime);
       $("#id_amountoftime").val(mintime)

        $("#id_price").val(finalprice)
const datestart = document.getElementById('id_startofvalidityperiod').value;
           const time = document.getElementById('id_amountoftime').value;
           let newDate = new Date(datestart);
           const curHoursNum = newDate.getHours();
           newDate.setHours(curHoursNum + Number(time));
           let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       if(datestart != "")
       {
                   $("#id_expirationdate").val(finalDateStr);
       }
    }
    });
});
$("#id_amountoftime").on('change', function(){
       var mintime = $("#id_amountoftime").val();
       var finalprice = mintime * price
                     $("#id_price").val(finalprice)
       const datestart = document.getElementById('id_startofvalidityperiod').value;
           const time = document.getElementById('id_amountoftime').value;
           let newDate = new Date(datestart);
           const curHoursNum = newDate.getHours();
           newDate.setHours(curHoursNum + Number(time));
           let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       if(datestart != "")
       {
                   $("#id_expirationdate").val(finalDateStr);
       }
});
window.onload = function() {
    let date = document.getElementById('id_startofvalidityperiod');
    date.addEventListener('change', function(event) {
           const datestart = document.getElementById('id_startofvalidityperiod').value;
           const time = document.getElementById('id_amountoftime').value;
           let newDate = new Date(datestart);
           const curHoursNum = newDate.getHours();
           newDate.setHours(curHoursNum + Number(time));
           let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       if(datestart != "")
       {
                   $("#id_expirationdate").val(finalDateStr);
       }
    });
}

