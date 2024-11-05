var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

const bigNum = (nums) =>{
    let big = nums[0];
    
    for(let i = 1; i<nums.length; i++){
        if(big < nums[i]){
            big = nums[i];
        }
    }
    return big;
}

console.log(bigNum(numbers));