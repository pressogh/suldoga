window.onload = (function(){
    $("#keyword").keyup(function() {
    var k = $(this).val();
    $(".coclist > .cardBox").hide();
    var temp = $(".coclist > .cardBox > .titleKr:contains('" + k + "')");
    var temp2 = $(".coclist > .cardBox > .titleEng:contains('" + k + "')");
    
    $(temp).parent().show();
    $(temp2).parent().show();
})

let check = true; // 바뀌기 때문에 let으로 선언
function changeLike() {
  document.getElementById('img').src = check
    ? 'img/unlike.png' //연산자 이용 체크
    : 'img/like.png';
    check = !check;
}

})

