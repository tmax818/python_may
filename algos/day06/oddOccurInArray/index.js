
  const frequencyTableBuilder = require("../freqTable")
  // // https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

  
  /* 
  Given a non-empty array of odd length containing ints where every int but one
  has a matching pair (another int that is the same)
  return the only int that has no matching pair.
  */

  // function frequencyTableBuilder(arr) {
  //   // create an empty object to hold the count. key will be the array element, value will be the element's count.
  //   var count = {}
  //   // loop through the array
  //   for (const char of arr) {
  //     // check if the key is in the object = count
  //     if(!count[char]){
  //       // if not, add to the object
  //       count[char] = 1
  //     }else {
  //       // if it is, increment to the count
  //       count[char]++
  //     }
  //   }
  //   //return the object
  // return count
  // }
  
  const nums1 = [1];
  const expected1 = 1;
  
  const nums2 = [5, 4, 5];
  const expected2 = 4;
  
  const nums3 = [5, 4, 3, 4, 3, 4, 5];
  const expected3 = 4; // there is a pair of 4s but one 4 has no pair.
  
  const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
  const expected4 = 1;
  
  function oddOccurrencesInArray(nums) {
    const freqTable = frequencyTableBuilder(nums)
    // console.log('our table', freqTable)
    for(let i in freqTable){
      // console.log(i, freqTable[i])
      if(freqTable[i] % 2 !== 0){
        return(i)
      }
    }
  }


  console.log(oddOccurrencesInArray(nums1))
  console.log(oddOccurrencesInArray(nums2))
  console.log(oddOccurrencesInArray(nums3))
  console.log(oddOccurrencesInArray(nums4))
  