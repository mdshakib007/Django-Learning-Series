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

loadServices();