/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];
    const stack = [{ list: arr, depth: 0, index: 0 }];
    while (stack.length) {
        const frame = stack[stack.length - 1];
        if (frame.index >= frame.list.length) {
            stack.pop();
            continue;
        }
        const elem = frame.list[frame.index++];
        if (Array.isArray(elem) && frame.depth < n) {
            stack.push({ list: elem, depth: frame.depth + 1, index: 0 });
        } else {
            result.push(elem);
        }
    }
    return result;
};
