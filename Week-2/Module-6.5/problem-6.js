var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

const bigName = (names) =>{
    let big = names[0];
    
    for(let i = 1; i<names.length; i++){
        if(big.length < names[i].length){
            big = names[i];
        }
    }
    return big;
}

console.log(bigName(friends));
