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
        },
    };
    //ajax
    $(document).ready(function() {
        var btn = document.getElementById("btn");
        EventUtil.addHandler(btn, "click", function() {
            var su = document.getElementById("su").value;
            if (su === '0') {
                var verify = confirm("确定要报名该活动吗？");
                if (verify === true) {
                    $.ajax({
                        url: '/api/v1_0/user/activity-registration',
                        dataType: 'JSON',
                        type: 'POST',
                        data: {
                            acid: $('#acid').val(),
                        },
                        success: function(data) {
                            if (data.status === "ok") {
                                alert("报名成功!");
                                var number = document.getElementById("number");
                                var num = number.innerHTML.split("/");
                                num0 = parseInt(num[0]) + 1;
                                number.innerHTML = num0 + "/" + num[1];
                                document.getElementById('su').value=1;

                            } else if (data.status === "fail") {
                                alert("信息有误。");
                            } else if (data.status === "full") {
                                alert("人数已满。");
                            } else {
                                alert("请勿重复报名。");
                            }
                        }
                    });
                }
            }else if (su === '1') {
                var verify2 = confirm("确定要取消报名吗？");
                if (verify2 === true) {
                    $.ajax({
                        url: '/api/v1_0/user/activity-unregistration',
                        dataType: 'JSON',
                        type: 'POST',
                        data: {
                            acid: $('#acid').val(),
                        },
                        success: function(data) {
                            if (data.status === "ok") {
                                alert("已取消报名!");
                                var number = document.getElementById("number");
                                var num = number.innerHTML.split("/");
                                num0 = parseInt(num[0]) - 1;
                                number.innerHTML = num0 + "/" + num[1];
                                document.getElementById('su').value=0;

                            } else if (data.status === "none") {
                                alert("您还未报名。");
                            } else{
                                alert("请稍后重试");
                            }
                        }
                    });
                }
            }
        });
    });