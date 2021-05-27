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
          var video = data['video'];
          $('#video').attr('src', video);
          //var b = document.getElementById(video);
          //b.setAttribute("src", "https://www.youtube.com/watch?v=OcOLyAcmiyM");
    }
    })
});