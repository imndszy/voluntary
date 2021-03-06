var EventUtil = {
    addHandler: function(element, type, handler) {
        if (element.addEventListener) {
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;
        }
    },
    removeHandler: function(element, type, handler) {
        if (element.removeEventListener) {
            element.removeEventListener(type, handler, false);
        } else if (element.detachEvent) {
            element.detachEvent("on" + type, handler);
        } else {
            element["on" + type] = null;
        }
    }
};
$(function() {
    var acid = $("#acid").val();
    $.ajax({
        url: '/api/v1_0/activities',
        dataType: 'JSON',
        type: 'GET',
        success: function(data) {
            if (data.status == "ok") {
                for (var i = 0; i < data.result.length; i++) {
                    if (data.result[i].acid == acid) {
                        if (data.result[i].actype == "1") {
                            document.getElementById("actype1").checked = true;
                        } else {
                            document.getElementById("actype2").checked = true;
                        }
                        document.getElementById("title").value = data.result[i].subject,
                            document.getElementById("address").value = data.result[i].ac_place,
                            document.getElementById("introduce2").value = data.result[i].introduce,
                            document.getElementById("start_time").value = data.result[i].start_time,
                            document.getElementById("finish_time").value = data.result[i].finish_time,
                            document.getElementById("required_stus").value = data.result[i].required_stus,
                            document.getElementById("alltime").value = data.result[i].vol_time
                    }
                }
            } else {

            }
        }
    });
    var checkinTimer = null,
        checkoutTimer = null;
    $("#checkinCloseBtn").click(function(){
        clearInterval(checkinTimer);
        $("#checkin_image").attr('src','');
    });
    $("#checkoutCloseBtn").click(function(){
        clearInterval(checkoutTimer);
        $("#checkout_image").attr('src','')
    });
    $("#publish").click(function() {
        var start_time = $("#start_time").val();
        var finish_time = $("#finish_time").val();
        if (!start_time || !finish_time) {
            alert("请填写活动安排时间！");
            this.focus();
            return false;
        }
        $.ajax({
            url: '/api/v1_0/activities',
            dataType: 'JSON',
            type: 'POST',
            data: {
                acid: acid,
                actype: $('input[type="radio"]:checked').val(),
                title: $("#title").val(),
                ac_place: $("#address").val(),
                introduce: $("#introduce2").val(),
                start_time: $("#start_time").val(),
                finish_time: $("#finish_time").val(),
                required_stus: $("#required_stus").val(),
                vol_time: $("#alltime").val()
            },
            success: function(data) {
                if (data.status == "ok") {
                    window.location.href = "/admin";
                } else {
                    alert("信息不完整");
                }
            }
        });
    });
    function check(acid,checkstart,checkwork,method){
        $.ajax({
            url: "/api/v1_0/qrcode/" + method,
            dataType: "JSON",
            type: "POST",
            data: {
                acid: acid,
                check_start: checkstart,
                check_work: checkwork
            },
            success: function(data) {
                if (data.status === "ok") {
                    document.getElementById(method+'_image').setAttribute("src", data.data);
                } else if (data.status === "fail") {
                    alert(data.data);
                } else {
                    alert(data.data);
                }
            }
        });
    }
    $("#checkin").click(function() {
        var checkin_start = document.getElementById("checkin_start").value,
            checkin_work = document.getElementById("checkin_work").value;
        if (!checkin_work) {
            alert("请填写有效期。");
            return false;
        }
        check(acid,checkin_start,checkin_work,"checkin");
        clearInterval(checkinTimer);
        checkinTimer = setInterval(function(){
                    check(acid,checkin_start,checkin_work,"checkin");
                },30*1000);
        setTimeout(function(){
                clearInterval(checkinTimer);
                $("#checkin_image").attr('src','');
            },checkin_work*60*1000);
        });
    $("#checkout").click(function() {
        // var checkout_start = document.getElementById("checkout_start").value;
        // if (!checkout_start || !checkout_work) {
        //     alert("请填写完整信息。");
        //     return false;
        // }
        // $.ajax({
        //     url: "/api/v1_0/qrcode/checkout",
        //     dataType: "JSON",
        //     type: "POST",
        //     data: {
        //         acid: acid,
        //         checkout_start: checkout_start,
        //         checkout_work: checkout_work
        //     },
        //     success: function(data) {
        //         if (data.status === "ok") {
        //             document.getElementById('checkout_image').setAttribute("src", data.data);
        //         } else if (data.status === "fail") {
        //             alert(data.data);
        //         } else {
        //             alert(data.data);
        //         }
        //     }
        // });
        var checkout_start = document.getElementById("checkout_start").value,
            checkout_work = document.getElementById("checkout_work").value;
        if (!checkout_work) {
            alert("请填写有效期。");
            return false;
        }
        check(acid,checkout_start,checkout_work,"checkout");
        clearInterval(checkoutTimer);
        checkoutTimer = setInterval(function(){
                    check(acid,checkout_start,checkout_work,"checkout");
                },30*1000);
        setTimeout(function(){
            clearInterval(checkoutTimer);
            $("#checkout_image").attr('src','');
        },checkout_work*60*1000);
    });
});
