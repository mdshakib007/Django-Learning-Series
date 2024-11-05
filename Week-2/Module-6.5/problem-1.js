const gradeCalculator = (mark) => {
    if (mark >= 80) return "A+";
    else if (mark >= 70) return "A";
    else if (mark >= 60) return "A-";
    else if (mark >= 50) return "B";
    else if (mark >= 40) return "C";
    else if (mark >= 33) return "D";
    else return "F";
}

const mark = 78;
console.log(gradeCalculator(mark));
