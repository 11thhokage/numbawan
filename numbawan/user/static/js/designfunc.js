window.addEventListener('scroll', function () {
  var header = document.getElementById('header');
  if (window.scrollY > 50) {
    header.classList.add('scroll');
  } else {
    header.classList.remove('scroll');
  }
});
/*==================== VIEW PASSWORD ====================*/
function togglePasswordVisibility() {
  var passwordInput = document.getElementById('password');
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
  } else {
    passwordInput.type = 'password';
  }
}