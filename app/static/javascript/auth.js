document.addEventListener("DOMContentLoaded", () => {

    const container = document.getElementById("auth-container");

    const showRegister = document.getElementById("show-register");
    const showLogin = document.getElementById("show-login");

    const mobileRegister = document.getElementById("mobile-register");
    const mobileLogin = document.getElementById("mobile-login");


    // Show registration panel
    function openRegister() {
        container.classList.add("active");
    }

    // Show login panel
    function openLogin() {
        container.classList.remove("active");
    }


    // Desktop buttons
    showRegister?.addEventListener("click", openRegister);
    showLogin?.addEventListener("click", openLogin);

    // Mobile buttons
    mobileRegister?.addEventListener("click", openRegister);
    mobileLogin?.addEventListener("click", openLogin);

});