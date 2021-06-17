var mintime
var price
//Выбор адреса парковки
$("select").on('change', function(){
    $("#id_expirationdate").prop("disabled", false);
    $("#id_amountoftime").prop("disabled", false);
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
    price = data['price'];
       $("#id_price").val(data['price']);
       mintime = parseInt(data['minimaltimeforpayment']);
       var pricevalue = $("#id_price").val();
       var finalprice = mintime * price;
       document.getElementById('id_amountoftime').setAttribute('min', mintime);
       $("#id_amountoftime").val(mintime);

        $("#id_price").val(finalprice);
const datestart = document.getElementById('id_expirationdate').value;
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

//Изменение количества времени для оплаты
$("#id_amountoftime").on('change', function(){
           const time = document.getElementById('id_amountoftime').value;
       var finalprice = time * price;
        $("#id_price").val(finalprice);
});

//Изменение даты начала срока действия оплаты
$("#id_expirationdate").on('change', function() {
    $("#id_expirationtime").prop("disabled", false);
    if (document.getElementById('id_expirationtime').value == "")
    {

    }
    else{
        const date = document.getElementById('id_expirationdate').value;
const time = document.getElementById('id_expirationtime').value;
const timemin = document.getElementById('id_amountoftime').value;
const datetimestart = date + 'T' + time;
let newDate = new Date(datetimestart);
const curHoursNum = newDate.getHours();
newDate.setHours(curHoursNum + Number(timemin));
let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
   if(date != "")
   {
        $("#id_enddateandtime").val(finalDateStr);
   }
    }
});

//Изменение времени начала срока действия оплаты
$("#id_expirationtime").on('change', function(){
const date = document.getElementById('id_expirationdate').value;
const time = document.getElementById('id_expirationtime').value;
const timemin = document.getElementById('id_amountoftime').value;
const datetimestart = date + 'T' + time;
let newDate = new Date(datetimestart);
const curHoursNum = newDate.getHours();
newDate.setHours(curHoursNum + Number(timemin));
let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
   if(date != "")
   {
        $("#id_enddateandtime").val(finalDateStr);
   }
});

//Нажатие на кнопку "Перейти к оплате"
$("#button").on("click", function () {
    const date = document.getElementById('id_expirationdate').value;
const time = document.getElementById('id_expirationtime').value;
localStorage.setItem("date",date);
localStorage.setItem("time",time);
});
window.onload = function() {
    $("#id_amountoftime").prop("disabled", false);
    $("#id_expirationdate").prop("disabled", false);
    $("#id_expirationtime").prop("disabled", false);
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
         const time = document.getElementById('id_amountoftime').value;
    var finalprice = price * time
       $("#id_price").val(finalprice)
       var mintime = parseInt(data['minimaltimeforpayment'])
       document.getElementById('id_amountoftime').setAttribute('min', mintime);
       $("#id_amountoftime").val(mintime)
    }
    });
    const date = localStorage.getItem("date");
    const time = localStorage.getItem("time");
    const phone = localStorage.getItem("phone");
    $("#id_expirationdate").val(date);
$("#id_expirationtime").val(time);
$("#id_telephone").val(phone);
localStorage.removeItem("date");
localStorage.removeItem("time");
if(document.getElementById('exampleFormControlSelect1').value !="")
{
        $("#id_expirationdate").prop("disabled", false);
}
 if (document.getElementById('id_expirationtime').value == "")
    {

    }
    else{
             $("#id_expirationtime").prop("disabled", false);
 }
};
$("#id_amountoftime").bind('keyup mouseup', function () {
    const date = document.getElementById('id_expirationdate').value;
const time = document.getElementById('id_expirationtime').value;
const timemin = document.getElementById('id_amountoftime').value;
const datetimestart = date + 'T' + time;
let newDate = new Date(datetimestart);
const curHoursNum = newDate.getHours();
newDate.setHours(curHoursNum + Number(timemin));
let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
   if(document.getElementById('exampleFormControlSelect1').value !="") {
       if (document.getElementById('id_expirationtime').value == "") {

       } else {
           $("#id_enddateandtime").val(finalDateStr);
       }
   }
});




