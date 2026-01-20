document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(res => {
        if (res.status === 200) {
            window.location.href = "/";  // redirect to homepage
        } else {
            alert("Invalid username or password");
        }
    });
});
