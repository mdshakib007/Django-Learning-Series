const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};

const handleRegister = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first-name");
    const last_name = getValue("last-name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm-password");
    info = { username, first_name, last_name, email, password, confirm_password };

    if (password === confirm_password) {
        document.getElementById("error-message").innerText = "";
        const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
        if (passwordRegex.test(password)) {

            document.getElementById("error-message").innerText = "";
            document.getElementById("register-btn").innerHTML = `<span class="loading loading-spinner loading-xs"></span>`;
            document.getElementById("register-success").innerText = "";

            fetch("https://smartcarebd-backend.onrender.com/patient/register/", {
                method: "POST",
                headers: { "content-type": "application/json" },
                body: JSON.stringify(info),
            })
            .then(res => res.json())
            .then(data => {
                if (data.username) {
                    document.getElementById("error-message").innerText = data.username;
                } else if(data.Error){
                    document.getElementById("error-message").innerText = data.Error;
                } else{
                    document.getElementById("register-success").innerText = "Please Check Your Email For Confirmation!"
                }
                document.getElementById("register-btn").innerHTML = `Register`;
            });

        } else {
            document.getElementById("error-message").innerText = "Password must be at least 8 characters, at least 1 uppercase, 1 lowercase and a digit!";
        }
    } else {
        document.getElementById("error-message").innerText = "Password & Confirm Password didn't match!";
    }
};

const handleLogin = (event) => {
    event.preventDefault();

    const username = getValue("login-username");
    const password = getValue("login-password");
    const info = { username, password };
    document.getElementById("login-btn").innerHTML = `<span class="loading loading-spinner loading-xs"></span>`;
    fetch("https://smartcarebd-backend.onrender.com/patient/login/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(info),
    })
    .then(res => res.json())
    .then(data => {
        if (data.token && data.user_id) {
            document.getElementById("login-error-message").innerText = "";
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "index.html";
        }
        else {
            document.getElementById("login-error-message").innerText = "Wrong username or password provided!";
        }
        document.getElementById("login-btn").innerHTML = `Login`;
    });
};

