
const findBig = (names) =>{
    let biggest = names[0];
    
    for(let i = 1; i<names.length; i++){
        if(names[i].length > biggest.length){
            biggest = names[i];
        }
    }
    return biggest;
}

friends = ['rahim', 'karim', 'jabbar', 'barkat', 'anis', 'rony', 'hasan', 'shakibul', 'rakibul'];

console.log(findBig(friends));
