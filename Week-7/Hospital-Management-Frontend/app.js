const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
    .then(res => res.json())
    .then((data) => displayService(data))
    .catch((err) => console.log(err));
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
                    <p class="card-text">${service.description.slice(0, 100)}...</p>
                    <a href="#" class="btn bg-violet-700 border-none hover:bg-violet-800 text-white max-w-fit">Learn More</a>
                </div>
            </div>
        `
        parent.appendChild(li);
    });
};

const loadDoctor = (name) => {
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${name ? name : ""}`)
    .then((res) => res.json())
    .then((data) => displayDoctor(data?.results));
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
            <h2 class="text-xl font-bold">${doctor?.full_name}</h2>
            <p>If a dog chews shoes whose shoes does he choose?</p>
            <p>            
                ${doctor?.specialization?.map((item) => {
                    return `<div class="badge badge-outline p-2 my-2">${item}</div>`
                })}
            </p>
            <button class="btn bg-violet-700 border-none hover:bg-violet-800  text-white">Details</button>
            </div>
        `;
        parent.appendChild(div);
    })
};

const loadDesignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
    .then(res => res.json())
    .then(data => data.forEach(item =>{
        const parent = document.getElementById("designation-dropdown");
        const li = document.createElement("li");
        li.innerHTML = `
            <a>${item.name}</a>
        `
        parent.appendChild(li);
    }));
};

const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
    .then(res => res.json())
    .then(data => data.forEach(item =>{
        const parent = document.getElementById("specialization-dropdown");
        const li = document.createElement("li");
        li.innerHTML = `
            <a>${item.name}</a>
        `
        parent.appendChild(li);
    }));
};

const handleSearch = () => {
    const value = document.getElementById("search-doctor").value;
    loadDoctor(value);
};



loadServices();
loadDoctor();
loadDesignation();
loadSpecialization();