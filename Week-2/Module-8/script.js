let myItems = [];

function initPlace() {
    const init = true;
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=`)
        .then(res => res.json())
        .then((data) => {
            placeSearchResult(data, init);
    })
};

function searchByName() {
    const val = document.getElementById('input-box').value;
    if (val == '') {
        const container = document.getElementById('result-title');
        container.innerText = "Please Type Anything!"
        return;
    }

    document.getElementById('input-box').value = '';
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${val}`)
        .then(res => res.json())
        .then((data) => {
            placeSearchResult(data);
        })
};

function placeSearchResult(searchResult, init = false) {
    const container = document.getElementById('search-result');
    if(!init)
        document.getElementById('result-title').innerText = "Search Result";
    else document.getElementById('result-title').innerText = "All Products";

    if (!searchResult.meals) {
        container.innerHTML = `
        <div class='card'>
        <h1 class='text-danger m-5'>No Item Found!</h1>
        <button class='btn btn-danger m-2' onclick="location.reload()">All Products</button>
        </div>
        `;
        return;
    }

    container.innerHTML = '';

    for (let product of searchResult.meals) {
        // console.log(product);
        const div = document.createElement('div');
        div.classList.add('card');
        div.classList.add('shadow-sm');

        let info = {
            name : product.strMeal,
            image : product.strMealThumb,
            category : product.strCategory,
            from : product.strArea,
            tags : product.strTags,
            video : product.strYoutube,
            ingredients : [product.strIngredient1, product.strIngredient2, product.strIngredient3],
        }
        // console.log(info);

        div.innerHTML = `
            <img src=${info.image} class='card-img-top' alt='meal'>
            <div class='card-body'>
                <h2 class='card-title'>${info.name}</h2>
                <p class='card-text text-secondary'>Category: ${info.category}</p>
                <button class='btn btn-warning' onclick="showDetails('${product.strMeal}', '${product.strMealThumb}', '${product.strArea}', '${product.strCategory}')">Details</button>
                <button class='btn btn-success' onclick="showDetails('${product.strMeal}', '${product.strMealThumb}', '${product.strArea}', '${product.strCategory}')">Add to List +</button>
            </div>
        `;
        container.appendChild(div);
    }
};

function showDetails(title, image, area, category) {
    // console.log(product);
    const modalTitle = document.getElementById('modalLabel');
    const modalBody = document.querySelector('#detailsModal .modal-body');

    modalTitle.innerText = title;
    modalBody.innerHTML = `
        <img src=${image} class="img-fluid mb-3" style='height: 250px'/>
        <h5 class="text-danger">From: ${area}</h5>
        <p>Category: ${category}</p>
    `;

    // Trigger modal
    const modal = new bootstrap.Modal(document.getElementById('detailsModal'));
    modal.show();

};


// initial place of all product
initPlace();