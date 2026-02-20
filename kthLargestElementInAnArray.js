/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
  const count = new Int32Array(20001);
  for (const num of nums){
    count[num + 10000]+=1;
  }
  for (let i=20000; i>=0; i--){
    if (count[i] > 0){
      k -= count[i];
      if (k <= 0) return i-10000;
    }
  }
};