const loadServices = () => {
    fetch("https://smartcarebd-backend.onrender.com/services/")
    .then(res => res.json())
    .then((data) => displayService(data))
};

const displayService = (services) => {
    services.forEach((service) => {
        const parent = document.getElementById("service-container");
        li = document.createElement("li");
        li.innerHTML = `
            <div class="card shadow h-100">
                <div class="ratio ratio-16x9">
                    <img src=${service.image} class="card-img-top max-h-96 w-full" loading="lazy" alt="...">
                </div>
                <div class="card-body p-3 p-xl-5">
                    <h3 class="card-title h5">${service.name}</h3>
                    <p class="card-text text-gray-600">${service.description.slice(0, 100)}...</p>
                    <a href="#" class="btn bg-violet-700 border-none hover:bg-violet-800 text-white max-w-fit">Learn More</a>
                </div>
            </div>
        `
        parent.appendChild(li);
    });
};

const loadDoctor = (id) => {
    // clear doctors section
    document.getElementById("doctor-cards").innerHTML = "";
    document.getElementById("loading-doctor-card").style.display = "block";

    fetch(`https://smartcarebd-backend.onrender.com/doctor/list/?doctor_id=${id ? id : ""}`)
    .then((res) => res.json())
    .then((data) => {
        document.getElementById("loading-doctor-card").style.display = "none";
        if (data.length > 0){
            document.getElementById("no-doctor-data").style.display = "none";
            displayDoctor(data);
        } else{
            document.getElementById("no-doctor-data").style.display = "block";
        }
    });
};

const displayDoctor = (doctors) => {
    doctors.forEach((doctor) => {
        const parent = document.getElementById("doctor-cards");
        const div = document.createElement("div");
        div.classList.add("bg-base-100");
        div.classList.add("max-w-72");
        div.classList.add("shadow-xl");
        div.classList.add("rounded-md");
        div.classList.add("p-3");
        div.innerHTML = `
            <div class="flex justify-center">
            <img src=${doctor?.image} alt="Shoes" class="rounded-md max-w-64" />
            </div>
            <div class="items-center text-center p-2">
            <h2 class="text-xl font-bold">${doctor.full_name}</h2>
            <p>            
                ${doctor?.specialization?.map((item) => {
                    return `<div class="badge badge-outline p-2 m-1">${item}</div>`
                }).join('')}
            </p>
            <a class="btn btn-sm bg-violet-700 border-none hover:bg-violet-800  text-white" href="doctor-details.html?doctor_id=${doctor.id}">Details</a>
            </div>
        `;
        parent.appendChild(div);
    })
};

const loadDesignation = () => {
    fetch("https://smartcarebd-backend.onrender.com/doctor/designations/")
    .then(res => res.json())
    .then(data => data.forEach(item =>{
        const parent = document.getElementById("designation-dropdown");
        const li = document.createElement("li");
        li.innerHTML = `
            <a onclick="loadDoctor('${item.name}')">${item.name}</a>
        `;
        parent.appendChild(li);
    }));
};

const loadSpecialization = () => {
    fetch("https://smartcarebd-backend.onrender.com/doctor/specializations/")
    .then(res => res.json())
    .then(data => data.forEach(item =>{
        const parent = document.getElementById("specialization-dropdown");
        const li = document.createElement("li");
        li.innerHTML = `
            <a onclick="loadDoctor('${item.name}')">${item.name}</a>
        `
        parent.appendChild(li);
    }));
};

const handleSearch = () => {
    const value = document.getElementById("search-doctor").value;
    document.getElementById("search-doctor").value = "";
    loadDoctor(value);
};

const loadReview = () => {
    fetch("https://smartcarebd-backend.onrender.com/doctor/reviews/")
    .then(res => res.json())
    .then(data => displayReview(data));
};

const displayReview = (reviews) => {
    reviews.forEach(review => {
        parent = document.getElementById("reviews");
        div = document.createElement("div");
        div.classList.add("min-h-36");
        div.innerHTML = `
            <div class="">
                <h3 class="text-xl font-bold text-violet-700">${review.reviewer_name}</h3>
                <h6 class="">${review.rating}</h6>
                <p class="text-sm text-gray-600">${review.body.slice(0,100)}...<p>
            </div>
        `;
        parent.appendChild(div);
    });
}


loadServices();
loadDoctor();
loadDesignation();
loadSpecialization();
loadReview();