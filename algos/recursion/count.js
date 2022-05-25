

function count(n){
    if(n >= 2){
        count(n - 1)
    }
    console.log(n)
}

count(5)


// function countNoRec(n){
//     for(let i = 1; i <= n; i++)
//     console.log(i)
// }

// countNoRec(5)