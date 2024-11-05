function sum(num1, num2) {
    return num1 + num2;
}

console.log(sum(1, 2));


// arrow function
const sum2 = (num1, num2) => num1 + num2;

console.log(sum2(4, 3));


// multiline arrow function
const sum3 = (num1, num2, num3) => {
    const s = num1 + num2 + num3;
    return s;
}
console.log(sum3(5, 3, 2));
