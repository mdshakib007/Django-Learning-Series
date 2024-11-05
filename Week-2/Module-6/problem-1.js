const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

arr.map(val => {
    if (val % 2 == 0) {
        console.log(val);
    }
});

const findEven = (arr) => {
    let evens = [];
    for(let i = 0; i<arr.length; i++){
        if(arr[i]%2 == 0) evens.push(arr[i]);
    }
    return evens;
}
console.log(...findEven(arr));


