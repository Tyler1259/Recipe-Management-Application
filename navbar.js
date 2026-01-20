fetch("/check-login")
    .then(res => res.json())
    .then(data => {
        const logoutLink = document.getElementById("logout-link");
        const signupLink = document.getElementById("signup-link");

        if (data.logged_in) {
            logoutLink.style.display = "inline-block";
            signupLink.style.display = "none";
        } else {
            logoutLink.style.display = "none";
            signupLink.style.display = "inline-block";
        }
    })
    .catch(err => console.error("Navbar error:", err));
