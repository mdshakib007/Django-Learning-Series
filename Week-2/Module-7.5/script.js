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

function placeSearchResult(searchResult) {
    const container = document.getElementById('search-result');
    document.getElementById('result-title').innerText = "Search Result";

    if (!searchResult.meals) {
        container.innerHTML = `
        <div class='card'>
        <h1 class='text-danger m-5'>No Item Found!</h1>
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
        div.innerHTML = `
            <img src=${product.strMealThumb} class='card-img-top' alt='meal'>
            <div class='card-body'>
                <h2 class='card-title'>${product.strMeal}</h2>
                <button class='btn btn-primary' onclick="showDetails('${product.strMeal}', '${product.strMealThumb}', '${product.strArea}', '${product.strCategory}')">Details</button>
            </div>
        `;
        container.appendChild(div);
    }
}

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

}
