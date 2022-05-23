
console.log("hi mom")

let message = "sup"

let skywalker = fetch("https://swapi.dev/api/people/1/").then( (res) => 
    res.json()
).then(data => document.write(data['name']))

// console.log(skywalker)