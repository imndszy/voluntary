    $(function() {
        $("nav#menu")
            .mmenu({
                navbar: {
                    title: ""
                },
                navbars: [{
                    height: 3,
                    content: ['<a align="center"><img src="../static/images/coupon_icon4.png"  style="width:60px;height:60px;" /></a><div class="bbiigg" id="username"></div>']
                }],
                counters: true,
                extensions: ["pagedim-black", "pageshadow", "effect-menu-zoom", "theme-dark", "widescreen"],
                offCanvas: {
                    position: "right"
                }
            })
            //数据获取
        $.ajax({
            url: '/api/v1_0/activity',
            dataType: 'JSON',
            type: 'GET',
            success: function(data) {
                if (data.status == "ok") {
                    $("#username").html(data.stuid);
                    $("#section-topline-1").empty();
                    $("#section-topline-2").empty();
                    for (var i = 0; i < data.result.length; i++) {
                        if (data.result[i].actype == 1) {
                            if (data.result[i].finished == 0) {
                                var item = ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box">0';
                                item += i + 1;
                                item += '</span></h5></div><div class="about-text"><a href="detail/';
                                item += data.result[i].acid;
                                item += '"><h4>';
                                item += data.result[i].subject;
                                item += '</h4><p>';
                                item += data.result[i].introduce;
                                item += '</p></a></div><div class="clearfix"> </div></div>';
                                $("#section-topline-1").append(item);
                            }
                        } else {
                            if (data.result[i].finished == 0) {
                                var item = '';
                                item += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box">0';
                                item += i + 1;
                                item += '</span></h5></div><div class="about-text"><a href="detail/';
                                item += data.result[i].acid;
                                item += '"><h4>';
                                item += data.result[i].subject;
                                item += '</h4><p>';
                                item += data.result[i].introduce;
                                item += '</p></a></div><div class="clearfix"> </div></div>';
                                $("#section-topline-2").append(item);
                            }
                        }
                    }
                    for (var i = 0; i < data.result.length; i++) {
                        if (data.result[i].actype == 1) {
                            if (data.result[i].finished == 1) {
                                var item = ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box">0';
                                item += i + 1;
                                item += '</span></h5></div><div class="about-text"><a href="detail/';
                                item += data.result[i].acid;
                                item += '"><h4 style="color:#ccc">';
                                item += data.result[i].subject;
                                item += '</h4><p style="color:#ccc">';
                                item += data.result[i].introduce;
                                item += '</p></a></div><div class="clearfix"> </div></div>';
                                $("#section-topline-1").append(item);
                            }
                        } else {
                            if (data.result[i].finished == 1) {
                                var item = '';
                                item += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box">0';
                                item += i + 1;
                                item += '</span></h5></div><div class="about-text"><a href="detail/';
                                item += data.result[i].acid;
                                item += '"><h4 style="color:#ccc">';
                                item += data.result[i].subject;
                                item += '</h4><p style="color:#ccc">';
                                item += data.result[i].introduce;
                                item += '</p></a></div><div class="clearfix"> </div></div>';
                                $("#section-topline-2").append(item);
                            }
                        }
                    }
                    $("#username").html(data.stuid);
                    var sl = document.getElementById("section-topline-1").getElementsByTagName("p");
                    var sh = document.getElementById("section-topline-2").getElementsByTagName("p");
                    for (i = 0; i < sl.length; i++) {
                        if (sl[i].innerHTML.length > 30) {
                            var slh = sl[i].innerHTML.slice(0, 30) + '...';
                            sl[i].innerHTML = slh;
                        }
                    }
                    for (i = 0; i < sh.length; i++) {
                        if (sh[i].innerHTML.length > 30) {
                            var shh = sh[i].innerHTML.slice(0, 30) + '...';
                            sh[i].innerHTML = shh;
                        }
                    }
                } else {
                    alert("列表为空。");
                }
            }
        })
    });