window.onload = function () {
  $('#keyword').keyup(function () {
    var k = $(this).val();
    $(' .coclist > .cocktailDiv >.cardBox').hide();
    var temp = $(
      ".coclist > .cocktailDiv > .cardBox > .titleKr +.titleEng:contains('" +
        k +
        "')"
    );

    $(temp).parent().show();
  });

  let check = true; // 바뀌기 때문에 let으로 선언
  function changeLike() {
    document.getElementById('img').src = check
      ? 'img/unlike.png' //연산자 이용 체크
      : 'img/like.png';
    check = !check;
  }
};
