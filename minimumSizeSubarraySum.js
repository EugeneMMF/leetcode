/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
  let first = 0
  let last = 0
  let sum = 0
  let minimum = nums.length;
  let hit = false
  for (let i=0; i<nums.length; i++) {
    sum += nums[i];
    last = i+1;
    while (sum >= target) {
      hit = true
      minimum = last-first < minimum ? last-first : minimum;
      sum -= nums[first++];
    }
  }
  return hit ? minimum : 0;
};