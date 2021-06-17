    var number
    var code
    var phonenumber
    $("#exit").on("click", function () {
        localStorage.removeItem("phone");
      document.location.href = "https://demo.vidim.org/exit"
    });
    $("#buttonsms").on("click", function () {
    function getRandomInt(min,max){
      number = Math.floor(Math.random() * (max - min)) + min;
      return number
    }
    getRandomInt(1000, 9999)
    phonenumber = $("#phonenumber").val();
    $.ajax({
        url: "https://sms.ru/sms/send?api_id=80645DBB-95F9-5E9A-9AF7-259B22D14168&to="+ phonenumber +
            "&msg=Одноразовый код для входа в личный кабинет на сайте оплаты услуг парковочных пространств: "+
            number +"&json=1",
        type: "HTTP",
        error:function(error){
            if(phonenumber == ""){
    $("#errorMess").text("Введите номер телефона");
    }
            else{
                     var re = /^((\+7)+([0-9]){10})$/;
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
              document.location.href = "https://demo.vidim.org/personalaccount?number=" + phonenumber;
          $("#errorMess").text("");
        }
        }
        });
          }
    });
