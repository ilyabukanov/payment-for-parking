var number
var code
var phonenumber
$("#exit").on("click", function () {
    localStorage.removeItem("phone");
  document.location.href = "http://localhost/exit"
});
$("#buttonsms").on("click", function () {
function getRandomInt(min,max){
  number = Math.floor(Math.random() * (max - min)) + min;
  return number
}
getRandomInt(1000, 9999)
phonenumber = $("#phonenumber").val();
$.ajax({
    url: "https://sms.ru/sms/send?api_id=EEB94BC4-609B-7248-EDFB-0C41307A2E8C&to="+ phonenumber +"&msg=Одноразовый код для входа в личный кабинет на сайте по оплате парковок: "+ number +"&json=1",
    type: "POST",
    error:function(error){
        if(phonenumber == ""){
$("#errorMess").text("Введите номер телефона");
}
        else{
                 var re = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/;
        var valid = re.test(phonenumber);
        if(valid){
if(phonenumber != ""){
alert(number)
$("#errorMess").text("");
$("#code").css("opacity", "1");
$("#buttoncode").css("opacity", "1");
}
        }
        else {
                        $("#errorMess").text("Номер телефона введён не верно");
        }
        }
   }
    })
});
$("#buttoncode").on("click", function () {
code = $("#code").val();
//console.log(number)
      if(code != number)
      {
                  $("#errorMess").text("Код из SMS введён не верно");
      }
      else{
      $.ajax({
    type: "GET",
    url: "session",
    data: {
      'phonenumber': phonenumber,
    },
    dataType: "text",
    cache: false,
    success:function (data){
    if(data == "yes"){
        localStorage.setItem("phone",phonenumber);
          document.location.href = "http://localhost/personalaccount?number=" + phonenumber;
      $("#errorMess").text("");
    }
    }
    });
      }
});
