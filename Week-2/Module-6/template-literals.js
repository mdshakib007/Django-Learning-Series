let country_name = "Bangladesh";
const country = `My country name is ${country_name}`;
console.log(country);

let x = [1, 2, 3, 4, 5];
let y = [6, 7, 8, 9, 0];
console.log(...x);      // ... means we traverse the array and print all the values without bracket.

console.log(...x, ...y);

let mx = Math.max(...x);
console.log(mx);


