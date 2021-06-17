var video
$("select").on('change', function(){
     var adress = $("#adress").val();
     $.ajax({
    type: "GET",
    url: "video",
    data: {
      'adress': adress,
    },
    dataType: "json",
    cache: false,
    success:function (data) {
          video = data['video'];
                     $("#video").css("opacity", "1");
          $('#video').attr('href', video);
    }
    })
});

