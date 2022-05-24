

function count(n){
    if(n >= 0){
        count(n - 1)
    }
    console.log(n)
}

count(5)