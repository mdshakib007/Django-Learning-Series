const getParam = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
    .then(res => res.json())
    .then(data => displayDetails(data));

    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then(res => res.json())
    .then(data => displayReview(data));

    fetch(`https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${param}`)
    .then(res => res.json())
    .then(data => displayAvailableTime(data));
};

const displayDetails = (doctor) => {
    parent = document.getElementById("doc-details-card");
    div1 = document.createElement("div");
    div2 = document.createElement("div");
    div1.classList.add("m-2");
    div1.innerHTML = `
        <h1 class="text-3xl font-bold my-4">${doctor.full_name}</h1>
        <h4 class="text-violet-700 mb-4 font-bold text-xl">Fee Tk. ${doctor.fee}</h4>
        <p><span class="font-bold">Designations:</span> <br>${
            doctor.designation.map(desig => {
                return `<div class="badge badge-outline p-3 my-2">${desig}</div>`
            }) 
        }</p>
        <p><span class="font-bold">Specializations:</span> <br>${
            doctor.specialization.map(spec => {
                return `<div class="badge badge-outline p-3 my-2">${spec}</div>`
            }) 
        }</p>
        <button class="btn bg-violet-700 border-none hover:bg-violet-800  text-white" onclick="my_modal_1.showModal()">Take Appoinment</button>
    `
    div2.innerHTML = `
        <img src="${doctor.image}" alt="${doctor.full_name}" class="max-h-96 rounded-md">
    `
    parent.appendChild(div1);
    parent.appendChild(div2);
};

const displayReview = (reviews) => {
    reviews.forEach(review => {
        parent = document.getElementById("reviews-of-doctor");
        div = document.createElement("div");    
        div.classList.add("min-h-36");
        div.innerHTML = `
            <div class="">
                <h3 class="text-xl font-bold text-violet-700">${review.reviewer}</h3>
                <h6 class="">${review.rating}</h6>
                <p class="text-sm text-gray-600">${review.body.slice(0,100)}...<p>
            </div>
        `;
        parent.appendChild(div);
    });
};

const displayAvailableTime = (times) => {
    times.forEach(time => {
        const parent = document.getElementById("time");
        const option = document.createElement("option");
        option.value = time.id;
        option.innerText = time.name;
        parent.appendChild(option);
    });
};

const handleAppoinment = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");

    const appoin_type = document.getElementsByName("appoinment-type");
    const selected = Array.from(appoin_type).find((button) => button.checked);
    const symptom = document.getElementById("symptom").value;
    const time = document.getElementById("time");
    const selected_time = time.options[time.selectedIndex];
    const info = {
        appointment_type : selected.value,
        appointment_status : "Pending",
        time : selected_time.value,
        symptom : symptom,
        cancel : false,
        patient : 1,
        doctor : param,
    };

    fetch("https://testing-8az5.onrender.com/appointment/", {method : "POST", headers : {"content-type" : "application/json"}, body : JSON.stringify(info)})
    .then(res => res.json())
    .then(data => console.log(data));
};


getParam();