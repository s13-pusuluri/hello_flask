
function validate() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('confirmPassword').value

    if (username.value === '') {
        alert('Username is required!');
    } else if (email.value === '') {
        alert('Email is required!');
    } else if (password.value === '') {
        alert('Password is required!');
    } else if (password.value !== passwordConfirmation.value) {
        alert('Passwords must match!');
    } else {
        //  Submit the form
        form.submit();

    }
}