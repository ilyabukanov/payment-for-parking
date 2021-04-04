var numberofdays
$("select").on('change', function(){
     $("#id_expirationdate").prop("disabled", false);
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
        const date = document.getElementById('id_expirationdate').value;
           const time = document.getElementById('id_expirationtime').value;
           const datestart = date + 'T' + time;
         let newDate = new Date(datestart);
         const curDateNum = newDate.getDate();
         newDate.setDate(curDateNum + Number(numberofdays));
         let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
       const timee = document.getElementById('id_expirationtime').value;
                          if(date && timee != "")
                 {
                          $("#id_enddateandtime").val(finalDateStr);
                 }
    }
    });
});

$("#id_expirationdate").on('change', function() {
     $("#id_expirationtime").prop("disabled", false);
    if (document.getElementById('id_expirationtime').value == "")
    {

    }
    else {
        const date = document.getElementById('id_expirationdate').value;
        if (date != "") {
            $("#id_expirationtime").prop("disabled", false);
        }
        const time = document.getElementById('id_expirationtime').value;
        const datetimestart = date + 'T' + time;
        let newDate = new Date(datetimestart);
        const curDateNum = newDate.getDate();
        newDate.setDate(curDateNum + Number(numberofdays));
        let finalDateStr = ('0' + newDate.getDate()).slice(-2) + '.' + ('0' + (newDate.getMonth() + 1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0' + newDate.getHours()).slice(-2) + ':' + ('0' + newDate.getMinutes()).slice(-2);
        if (date != "") {
            $("#id_enddateandtime").val(finalDateStr);
        }
    }
});

$("#id_expirationtime").on('change', function(){
 const date = document.getElementById('id_expirationdate').value;
           const time = document.getElementById('id_expirationtime').value;
           const datetimestart = date + 'T' + time;
           let newDate = new Date(datetimestart);
           const curDateNum = newDate.getDate();
         newDate.setDate(curDateNum + Number(numberofdays));
         let finalDateStr = ('0'+newDate.getDate()).slice(-2) + '.' + ('0'+(newDate.getMonth()+1)).slice(-2) + '.' + newDate.getFullYear() + ' ' + ('0'+newDate.getHours()).slice(-2) + ':' + ('0'+newDate.getMinutes()).slice(-2);
   if(date != "") {
       $("#id_enddateandtime").val(finalDateStr);
   }
});
$("#button").on("click", function () {
    const date = document.getElementById('id_expirationdate').value;
const time = document.getElementById('id_expirationtime').value;
localStorage.setItem("date",date);
localStorage.setItem("time",time);
localStorage.setItem("numberofdays",numberofdays);
});
window.onload = function() {
    const date = localStorage.getItem("date");
    const time = localStorage.getItem("time");
    const phone = localStorage.getItem("phone");
    numberofdays = localStorage.getItem("numberofdays");
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