/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;


const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

const strA4 = "ABC";
const strB4 = "aBc";
const expected4 = true;
/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(strA, strB) {
    if(strA.length !== strB.length){
        return false
    }
    if(strA.toLowerCase() === strB.toLowerCase()){
        return true
    } else {
        return false
    }
    


}

console.log("func call", caseInsensitiveStringCompare(strA1, strB1))
console.log("func call",caseInsensitiveStringCompare(strA2, strB2))
console.log("func call",caseInsensitiveStringCompare(strA3, strB3))
console.log("func call",caseInsensitiveStringCompare(strA4, strB4))