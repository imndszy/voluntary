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
            cache: false,
            success: function(data) {
                if (data.status == "ok") {
                    $("#username").html(data.stuid);
                    $("#section-topline-1").empty();
                    $("#section-topline-2").empty();
                    var item = '',
                        item1 = '',
                        item2 = '',
                        item3 = '';
                    for (var i = 0; i < data.result.length; i++) {
                        if (data.result[i].actype === 1) {
                            if (data.result[i].finished === false) {
                                item += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box">';
                                item += '进行中';
                                item += '</span></h5></div><div class="about-text"><a href="detail/';
                                item += data.result[i].acid;
                                item += '"><h4>';
                                item += data.result[i].subject;
                                item += '</h4><p>';
                                item += data.result[i].introduce;
                                item += '</p></a></div><div class="clearfix"> </div></div>';
                            } else if (data.result[i].finished === true) {
                                item1 += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box"style="background:#919c9c">';
                                item1 += '已结束';
                                item1 += '</span></h5></div><div class="about-text"><a href="detail/';
                                item1 += data.result[i].acid;
                                item1 += '"><h4 style="color:#ccc">';
                                item1 += data.result[i].subject;
                                item1 += '</h4><p style="color:#ccc">';
                                item1 += data.result[i].introduce;
                                item1 += '</p></a></div><div class="clearfix"> </div></div>';
                            }
                        }
                    }
                    for (var j = 0; j < data.result.length; j++) {
                        if (data.result[j].actype === 2) {
                            if (data.result[j].finished === false) {
                                item2 += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box" >';
                                item2 += '进行中';
                                item2 += '</span></h5></div><div class="about-text"><a href="detail/';
                                item2 += data.result[j].acid;
                                item2 += '"><h4>';
                                item2 += data.result[j].subject;
                                item2 += '</h4><p>';
                                item2 += data.result[j].introduce;
                                item2 += '</p></a></div><div class="clearfix"> </div></div>';
                            } else if (data.result[j].finished === true) {
                                item3 += '';
                                item3 += ' <div class="about-grid ad-more"><div class="about-box"><h5><span class="ab-box" style="background:#919c9c">';
                                item3 += '已结束';
                                item3 += '</span></h5></div><div class="about-text"><a href="detail/';
                                item3 += data.result[j].acid;
                                item3 += '"><h4 style="color:#ccc">';
                                item3 += data.result[j].subject;
                                item3 += '</h4><p style="color:#ccc">';
                                item3 += data.result[j].introduce;
                                item3 += '</p></a></div><div class="clearfix"> </div></div>';
                            }
                        }

                    }
                    item = item + item1;
                    $("#section-topline-1").append(item);
                    item2 = item2 + item3;
                    $("#section-topline-2").append(item2);
                    $("#username").html(data.stuid);
                    var sl = document.getElementById("section-topline-1").getElementsByTagName("p");
                    var sh = document.getElementById("section-topline-2").getElementsByTagName("p");
                    for (i = 0; i < sl.length; i++) {
                        if (sl[i].innerHTML.length > 28) {
                            var slh = sl[i].innerHTML.slice(0, 30) + '...';
                            sl[i].innerHTML = slh;
                        }
                    }
                    for (i = 0; i < sh.length; i++) {
                        if (sh[i].innerHTML.length > 28) {
                            var shh = sh[i].innerHTML.slice(0, 30) + '...';
                            sh[i].innerHTML = shh;
                        }
                    }
                } else {
                    alert("列表为空。");
                }
            }
        });
    });
