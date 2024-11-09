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
        container.innerText = "Please Type to Search!"
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
    if (!init)
        document.getElementById('result-title').innerText = "Search Result";
    else
        document.getElementById('result-title').innerText = "All Products";

    if (!searchResult.meals) {
        container.innerHTML = `
        <div class='card'>
        <h1 class='text-danger m-5'>No Item Found!</h1>
        <button class='btn btn-danger m-2' onclick="location.reload()">Refresh</button>
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
            id: product.idMeal,
            name: product.strMeal,
            image: product.strMealThumb,
            category: product.strCategory,
            from: product.strArea,
            tags: product.strTags,
            video: product.strYoutube,
            ingredients: [product.strIngredient1, product.strIngredient2, product.strIngredient3]
        }
        // console.log(info);

        div.innerHTML = `
            <img src=${info.image} class='card-img-top' alt='meal'>
            <div class='card-body'>
                <h2 class='card-title'>${info.name}</h2>
                <p class='card-text text-secondary'>Category: ${info.category}</p>
                <button class='btn btn-warning' onclick="showDetails('${info.id}', '${info.name}', '${info.image}', '${info.from}', '${info.category}', '${info.tags}', '${info.video}', '${info.ingredients}')">Details</button>
                <button class='btn btn-outline-primary' onclick="addToList('${info.id}', '${info.name}', '${info.image}', '${info.category}')">Add to List +</button>
            </div>
        `;
        container.appendChild(div);
    }
};

function showDetails(id, title, image, area, category, tags, video, ingredients) {
    // console.log(id, title, image, area, category, tags, video, ingredients);
    const modalTitle = document.getElementById('modalLabel');
    const modalBody = document.querySelector('#detailsModal .modal-body');

    modalTitle.innerText = title;
    modalBody.innerHTML = `
        <img src=${image} class="img-fluid mb-3" style='height: 250px'/>
        <h5 class="text-primary">${area} - ${category}</h5>
        <p class='text-secondary'>
            Ingredients: ${ingredients} and more... <br>
            Tags: ${tags} <br>
            Video: <a class='text-decoration-none' href='${video}' target='_blank'>${video}</a>
        </p>
    `;

    // Trigger modal
    const modal = new bootstrap.Modal(document.getElementById('detailsModal'));
    modal.show();

};

function addToList(id, name, image, category) {
    // console.log(id, name, image, category);
    id = parseInt(id);
    if (myItems.includes(id) || myItems.length == 10) {
        const modalTitle = document.getElementById('modalLabel');
        const modalBody = document.querySelector('#detailsModal .modal-body');
        modalTitle.innerText = "Problem Occurred!";
        modalBody.innerHTML = `
            <h4 class='text-danger'>This food item is already in my list or Maximum amount of item added to the list!</h4>
        `;
        const modal = new bootstrap.Modal(document.getElementById('detailsModal'));
        modal.show();
        return;
    }

    myItems.push(id);
    const container = document.getElementById('my-list');
    const div = document.createElement('div');
    div.classList.add('card');
    div.classList.add('shadow-sm');
    div.innerHTML = `
        <img src=${image} class='card-img-top' alt='meal'>
        <div class='card-body'>
            <h2 class='card-title'>${name}</h2>
            <p class='card-text text-secondary'>Category: ${category}</p>
            <button class='btn btn-danger' onclick="removeFromList('${id}')">Remove</button>
        </div>
    `;
    container.appendChild(div);
    document.getElementById('my-items-title').innerText = `My List - ${myItems.length} Items`;
}

function removeFromList(id) {
    id = parseInt(id);
    const idx = myItems.indexOf(id);
    if (idx !== -1) {
        myItems.splice(idx, 1);
    }
    
    const container = document.getElementById('my-list');
    const cards = container.getElementsByClassName('card');
    for (let card of cards) {
        if (card.querySelector('button').getAttribute('onclick') === `removeFromList('${id}')`) {
            container.removeChild(card);
            break;
        }
    }
    document.getElementById('my-items-title').innerText = `My List - ${myItems.length} Items`;
}


// initial place of all product
initPlace();