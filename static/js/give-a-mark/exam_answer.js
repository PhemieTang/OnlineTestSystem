$("#submitAndTestBtn1").click(function () {
    if ($("#a1").css("display") == "none") {
        $("#a1").show();
        $("#submitAndTestBtn1").css("background-color","#d7003a");
        $("#submitAndTestBtn1").text("隐藏");
    } else {
        $("#a1").hide();
        $("#submitAndTestBtn1").css("background-color","#59b9c6");
        $("#submitAndTestBtn1").text("评分");
    }
});


$("#submitAndTestBtn2").click(function () {
    if ($("#a2").css("display") == "none") {
        $("#a2").show();
        $("#submitAndTestBtn2").css("background-color","#d7003a");
        $("#submitAndTestBtn2").text("隐藏");
    } else {
        $("#a2").hide();
        $("#submitAndTestBtn2").css("background-color","#59b9c6");
        $("#submitAndTestBtn2").text("评分");
    }
});




