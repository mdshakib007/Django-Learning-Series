const recognize = (year) => {
    if (year % 4 == 0) return "Leap Year!";
    else return "Not a Leap Year!";
}


let n = 2024;
console.log(recognize(n));