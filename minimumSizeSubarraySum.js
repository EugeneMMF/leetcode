/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
  first = 0
  last = 0
  sum = 0
  minimum = nums.length;
  for (let i=0; i<nums.length; i++) {
    sum += nums[i];
    last = i+1;
    while (sum >= target) {
      minimum = last-first < minimum ? last-first : minimum;
      sum -= nums[first++];
    }
  }
  return minimum;
};