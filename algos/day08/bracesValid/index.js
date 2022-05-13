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

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    const stack = []
    const opens = "({[";
    const closeToOpen = { ")": "(", "}": "{", "]": "[" };
    for(let i = 0; i < str.length; i++){
        if(opens.includes(str[i])){
            console.log('stackbefore = ', stack, "strEl =", str[i])
            stack.push(str[i])
            console.log('stack = ', stack, "strEl =", str[i])
        } else if (str[i] in closeToOpen) {
            if(closeToOpen[str[i]] === stack[stack.length -1]){
                console.log("stackafter=", stack, "i=", str[i])
                stack.pop();

            } else {
                return false
            }
        }
    }
    return stack.length === 0;
}

console.log(bracesValid(str1))
// console.log(bracesValid2(str2))
// console.log(bracesValid2(str3))



// /**
//  const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
//  * - Time: O(n * m) where n = str.length and m = opens.length,
//  *    since opens.length is constant length of 3 -> O(3n) -> O(n) linear.
//  * - Space: O(n) linear.
//  * @param {string} str
//  * @returns {boolean}
//  */
// function bracesValid2(str = "") {}



let mystr = "Hello Yo Han"

console.log(mystr.includes("Hell"))