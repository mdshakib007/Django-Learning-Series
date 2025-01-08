const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};

const handleRegister = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first-name");
    const last_name = getValue("last-name");
    const password = getValue("password");
    const confirm_password = getValue("confirm-password");
    info = { username, first_name, last_name, password, confirm_password };
    console.log(info);
    if (password === confirm_password) {
        document.getElementById("error-message").innerText = "";
        const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
        if (passwordRegex.test(password)) {
            document.getElementById("error-message").innerText = "";
            fetch("https://testing-8az5.onrender.com/patient/register/", {
                method: "POST",
                headers: { "content-type": "application/json" },
                body: JSON.stringify(info),
            })
                .then(res => res.json())
                .then(data => console.log(data));
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

    fetch("https://testing-8az5.onrender.com/patient/login/",{
        method : "POST",
        headers : {"content-type" : "application/json"},
        body : JSON.stringify(info),
    })
    .then(res => res.json())
    .then(data => {
        if(data.token && data.user_id){
            document.getElementById("login-error-message").innerText = "";
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "index.html";
        }
        else{
            document.getElementById("login-error-message").innerText = "username or password didn't match!";
        }
    });
};