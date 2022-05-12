/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

function parensValid(str) {
    let countP = 0
    let countC = 0
    let countB = 0
    brackets = {')': '(', ']': '[', '}': '{'}
    for(var i = 0; i < str.length;i++){
        if(str[i] === '(' ){
            countP++
        }
        if(str[i] === '{' ){
            countC++
        }
        if(str[i] === '[' ){
            countB++
        }
        if(str[i] === ')' || str[i] === '}' || str[i] === ']'){
            count--
        }
        if(count < 0){
            return false
        }
    }
    return count === 0
}

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
// function bracesValid(str) {
//     for(let i = 0; i > str.length; i++){

//     }
// }

console.log(parensValid(str1))
console.log(parensValid(str2))
console.log(parensValid(str3))


// /**
//  const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
//  * - Time: O(n * m) where n = str.length and m = opens.length,
//  *    since opens.length is constant length of 3 -> O(3n) -> O(n) linear.
//  * - Space: O(n) linear.
//  * @param {string} str
//  * @returns {boolean}
//  */
// function bracesValid2(str = "") {}

// console.log(bracesValid2(str1))
// console.log(bracesValid2(str2))
// console.log(bracesValid2(str3))