$(document).ready(function () {
  $('form').on('submit', function (event) {
    event.preventDefault();

    let userInfo = new FormData(this);

    fetch('/create-password', {
      method: 'POST',
      body: userInfo,
    })
      .then((response) => response.json())
      .then((generatedPassword) => {
        $('#generated_pw').val(generatedPassword);
        $('#result_card').removeClass('d-none');
      });
  });
});
