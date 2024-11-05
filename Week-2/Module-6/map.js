const products = [
    { id: 1, name: "iPhone", description: "This is from apple", price: 140000, color: "black" },
    { id: 2, name: "Realme", description: "This is from Realme", price: 15000, color: "red" },
    { id: 3, name: "Xiaomi", description: "This is from xiaomi", price: 30000, color: "green" },
    { id: 4, name: "Vivo", description: "This is from Vivo", price: 20000, color: "black" }
];

// map function
console.log(products.map(product => product.id));

const res = products.map(product => product.id + 10);
console.log(res);

// forEach function
products.forEach(product => {
    console.log(product.id);
});


