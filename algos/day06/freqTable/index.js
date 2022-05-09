/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function frequencyTableBuilder(arr) {
  // create an empty object to hold the count. key will be the array element, value will be the element's count.
  var count = {}
  // loop through the array
  for (const char of arr) {
    // check if the key is in the object = count
    if(!count[char]){
      // if not, add to the object
      count[char] = 1
    }else {
      // if it is, increment to the count
      count[char]++
    }
  }
  //return the object
return count
}

// console.log("arr1 returns", frequencyTableBuilder(arr1))
// console.log("arr2 returns:",frequencyTableBuilder(arr2))
// console.log("arr3 returns:",frequencyTableBuilder(arr3))

module.exports = frequencyTableBuilder