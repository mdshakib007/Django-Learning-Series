const MonthlySavings = (payments, living_cost) => {
    if((typeof payments != typeof [1, 2]) || (typeof living_cost != typeof 100)){
        return "Invalid Input!"
    }

    let total_earn = 0;
    for(let i = 0;i<payments.length; i++){
        if(payments[i] >= 3000){
            total_earn += (payments[i] - (payments[i]*0.2));
        }
        else{
            total_earn += payments[i];
        }
    }
    total_earn -= living_cost;

    if(total_earn >= 0) return total_earn;
    else return "Earn More!";
}


const p = [1000, 2000, 2500];
const c = 5000;

console.log(MonthlySavings(p, c));