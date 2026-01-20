document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const user={
            username:document.getElementById("username").value,
            password:document.getElementById("password").value,
        
        };

        fetch("/sign-up",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify(user)
        })
        .then(res=> res.json())
        .then(data=> {
            alert(data.message);
            form.reset();
        })
        .catch(err =>console.error("Error:",err));
            });
});