var sumprice = 0
var expirationdates = [];
var prices = [];
$("#enddate").on('change', function () {
     $("#email").removeAttr("disabled");
    const startdate = document.getElementById('startdate').value;
    let newDateStart = new Date(startdate);
    const curHoursNumStart = newDateStart.getHours();
    newDateStart.setHours(curHoursNumStart + Number(0));
    let finalDateStrStart = ('0' + newDateStart.getDate()).slice(-2) + '.' + ('0' + (newDateStart.getMonth() + 1)).slice(-2) + '.' + newDateStart.getFullYear()
    const enddate = document.getElementById('enddate').value;
    let newDateEnd = new Date(enddate);
    const curHoursNumEnd = newDateEnd.getHours();
    newDateEnd.setHours(curHoursNumEnd + Number(0));
    let finalDateStrEnd = ('0' + newDateEnd.getDate()).slice(-2) + '.' + ('0' + (newDateEnd.getMonth() + 1)).slice(-2) + '.' + newDateEnd.getFullYear()

    $.ajax({
        type: "POST",
        url: "date",
        data: {
            'startdate': finalDateStrStart, 'enddate': finalDateStrEnd,
        },
        dataType: "json",
        cache: false,
        success: function (data) {
            if (data.result) {
                for (let i = 0; i < data.result.length; i++) {
                    expirationdates.push(data.result[i].expirationdate);
                    sumprice = sumprice + data.result[i].price__sum;
                    prices.push(data.result[i].price__sum);
                }
            }
            $("h4").append("<span>Итоговая сумму: " + sumprice + "</span>")
            if (window.chart instanceof Chart) {
                window.chart.destroy();
            }
            var ctx = document.getElementById("line").getContext("2d");
            var chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: expirationdates,
                    datasets: [{
                        label: 'Оплата парковочных пространств',
                        backgroundColor: 'rgb(65, 105, 225)',
                        borderColor: 'rgb(65, 105, 225)',
                        data: prices,
                    }]
                },
                options: {}
            });
            var ctx = document.getElementById("bar").getContext("2d");
            var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: expirationdates,
                    datasets: [{
                        label: 'Оплата парковочных пространств',
                        backgroundColor: 'rgb(65, 105, 225)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: prices,
                    }]
                },
                options: {}
            });
            var ctx = document.getElementById("doughnut").getContext("2d");
            var chart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: expirationdates,
                    datasets: [{
                        label: 'Оплата парковочных пространств',
                        backgroundColor: ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"],
                        data: prices,
                    }]
                },
                options: {}
            });
        }
    });
});
$("#buttonword").on("click", function () {
    email = $("#email").val();
    if (email == "") {
        $("#error").text("Введите email адрес");
    } else {
        var re = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        var valid = re.test(email);
        if (valid) {
            $("#error").text("");
                var pricesum = sumprice;
    var date = expirationdates;
    var price = prices;
    const startdate = document.getElementById('startdate').value;
    const enddate = document.getElementById('enddate').value;
    $.ajax({
        type: "POST",
        url: "print",
        data: JSON.stringify({
            'pricesum': pricesum,
            'date': date,
            'price': price,
            'startdate': startdate,
            'enddate': enddate,
            'email': email,
        }),
        dataType: "json",
        cache: false,
        success: function (data) {
        }
    });

        } else {
            $("#error").text("Email адрес введён не верно");
        }
    }
    $.ajax({
        url: "http://localhost/",
        type: "HTTP",
        error: function (error) {
        }
    });
});
$("#startdate").on('change', function () {
    $("#enddate").prop("disabled", false);
});

$("#email").on('change', function () {
         $("#buttonword").removeAttr("disabled");
});

