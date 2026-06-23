/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
  const mapped = arr.map(v => ({v, k: fn(v)}));
  mapped.sort((a, b) => a.k - b.k);
  return mapped.map(item => item.v);
};
