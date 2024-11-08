let currentProduct = {};


const loadProducts = () => {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then((data) => {
            displayProduct(data);
        });
};

const displayProduct = (products) =>{
    const productContainer = document.getElementById('product-container');

    products.forEach(product => {
        div = document.createElement('div');
        div.classList.add('card');
        div.style.width = '18rem';
        div.style.margin = '20px';
        div.style.padding = '20px';

        div.innerHTML = `
            <img src=${product.image} class='card-img-top'/>
            <div class='card-body'>
                <h4 class='card-title'>${product.title.slice(0, 50)}...</h4>
                <h4 class='card-title text-danger'>$${product.price}</h4>
                <p class='card-text text-secondary'>${product.description.slice(0, 100)}...</p>
                <button onclick="addToCart('${product.title}', '${product.price}', '${product.image}')" class='btn btn-primary'>Add to Cart</button>
                <button type='button' data-bs-toggle='modal' data-bs-target='#detailsModal' class='btn btn-secondary' onclick="singleProduct('${product.id}')">Details</button>
            </div>
        `
        productContainer.appendChild(div);
    });
};


const addToCart = (title, price, image) =>{
    const cartCount = document.getElementById('count-item').innerText;
    let convertedCount = parseInt(cartCount);
    convertedCount += 1;
    document.getElementById('count-item').innerText = convertedCount;

    const cartContainer = document.getElementById('cart-container');
    const div =  document.createElement('div');
    div.classList.add('cart-item');
    div.innerHTML = `
        <img src='${image}'/>
        <h5>${title.slice(0, 20)}...</h5>
        <h3>$<span class='price'>${price}</span></h3>
`
    cartContainer.appendChild(div);
    updateCart();
};

const updateCart = () => {
    const allPrices = document.getElementsByClassName('price');
    let cnt = 0;
    for(const price of allPrices){
        cnt = cnt + parseFloat(price.innerText);
    }
    document.getElementById('total-price').innerText = cnt.toFixed(2);
};

const singleProduct = (id) => {
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(res => res.json())
        .then((data) => {
            showDetails(data);
    });
};

const showDetails = (data) => {
    const modalTitle = document.getElementById('modalLabel');
    const modalBody = document.querySelector('#detailsModal .modal-body');

    currentProduct = {
        title: data.title,
        price: data.price,
        image: data.image
    };

    modalTitle.innerText = data.title;
    modalBody.innerHTML = `
        <img src="${data.image}" class="img-fluid mb-3" style='height: 250px'/>
        <h5 class="text-danger">$${data.price}</h5>
        <p>${data.description}</p>
        <p>Category: ${data.category}</p>
    `;
};

const checkOut = () => {
    document.getElementById('count-item').innerText = 0;

    const cartContainer = document.getElementById('cart-container');
    while (cartContainer.firstChild) {
        cartContainer.removeChild(cartContainer.firstChild);
    }
    document.getElementById('total-price').innerText = '0.00';
};



document.addEventListener('DOMContentLoaded', () => {
    loadProducts();

    const addToCartButton = document.querySelector('#detailsModal .btn-primary');
    addToCartButton.addEventListener('click', () => {
        addToCart(currentProduct.title, currentProduct.price, currentProduct.image);
    });
});
