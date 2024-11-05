var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

const uniqArr = numbers.filter((val, idx, self) => self.indexOf(val) === idx);

console.log(uniqArr);

//==============================//

const uniqArr2 = [...new Set(numbers)];
console.log(uniqArr2);