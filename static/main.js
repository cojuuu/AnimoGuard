$(document).ready(function () {
  $('form').on('submit', function (event) {
    event.preventDefault();

    let userInfo = new FormData(this);

    fetch('/create-password', {
      method: 'POST',
      body: userInfo,
    })
      .then((response) => {
        // Check if the server sent back a 400-level error
        if (!response.ok) {
          return response.json().then((errData) => {
            // Throw an error so the .catch() block below handles it
            throw new Error(errData.error);
          });
        }
        return response.json(); // If it's OK, proceed normally
      })
      .then((generatedPassword) => {
        $('#generated_pw').val(generatedPassword);
        $('#result_card').removeClass('d-none');
      })
      .catch((error) => {
        $('#alertMsg').html(error.message);
        $('#alertBox').removeClass('d-none');
      });
  });
});

$('#copy_btn').on('click', function () {
  let passwordToCopy = $('#generated_pw').val();

  if (passwordToCopy) {
    navigator.clipboard
      .writeText(passwordToCopy)
      .then(() => {
        $('#copy_text').text('Copied!');
        $('#copy_btn i').removeClass('bi-copy').addClass('bi-check2');

        setTimeout(() => {
          $('#copy_text').text('Copy');
          $('#copy_btn i').removeClass('bi-check2').addClass('bi-copy');
        }, 2000);
      })
      .catch((err) => {
        console.error('Failed to copy text: ', err);
      });
  }
});
