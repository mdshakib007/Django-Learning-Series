// object distucturing
let person = {
    name : "Anis",
    age : 14,
    friends : ["Shakib", "Hridoy"]
};

let my_age = person.age;
console.log(my_age);

const {age, name} = person;
console.log(age);
console.log(name);

/// array distucturing
const info = ["Shakib", 21, "asdf asd fa sdf qwe r"];

const [name2, age2, description, extra] = info;
console.log(description);
console.log(extra);
