/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
  const stack = [{arr: arr, i: 0}];
  while (stack.length) {
    const frame = stack[stack.length - 1];
    if (frame.i >= frame.arr.length) {
      stack.pop();
      continue;
    }
    const el = frame.arr[frame.i++];
    if (Array.isArray(el)) {
      stack.push({arr: el, i: 0});
    } else {
      yield el;
    }
  }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */