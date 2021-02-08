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
 $("#id_price").val(nametickets['price'])
    }
    });
});