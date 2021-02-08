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

    }
    });
});
$("#id_amountoftime").on('change', function(){
       var mintime = $("#id_amountoftime").val();
       var finalprice = mintime * price
                     $("#id_price").val(finalprice)
});