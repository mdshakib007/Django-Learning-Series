var status = "raining";

if (status == "raining") {
    console.log("Don't go outside!");
} else if (status == "hot") {
    console.log("Too hot outside! Don't go outside!");
} else {
    console.log("Can go outside!");
}

var res = 78;
if (res < 33) {
    console.log("Fail!");
} else if (res >= 33 && res <= 50) {
    console.log("C");
} else if (res >= 51 && res <= 70) {
    console.log("B");
} else if (res >= 71) {
    console.log("A");
}