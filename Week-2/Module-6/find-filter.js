const products = [
    { id: 1, name: "iPhone", description: "This is from apple", price: 140000, color: "black" },
    { id: 2, name: "Realme", description: "This is from Realme", price: 15000, color: "red" },
    { id: 3, name: "Xiaomi", description: "This is from xiaomi", price: 30000, color: "green" },
    { id: 4, name: "Vivo", description: "This is from Vivo", price: 20000, color: "black" }
];

for (let i = 0; i < products.length; i++) {
    if (products[i].id == 2) {
        console.log(products[i]);
    }
}

// find operation
const res = products.find(product => product.id == 2);
console.log(res);

// filter operation
const res2 = products.filter(product => product.color == 'black');
console.log(res2);

