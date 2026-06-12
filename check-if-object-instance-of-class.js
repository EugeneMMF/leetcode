/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
  if (typeof classFunction !== 'function') return false;
  if (obj === null || obj === undefined) return false;
  if (typeof obj === 'object' || typeof obj === 'function') {
    return obj instanceof classFunction;
  }
  const type = typeof obj;
  if (classFunction === Number && type === 'number') return true;
  if (classFunction === String && type === 'string') return true;
  if (classFunction === Boolean && type === 'boolean') return true;
  if (classFunction === Symbol && type === 'symbol') return true;
  if (classFunction === BigInt && type === 'bigint') return true;
  if (classFunction === Object && type !== 'object' && type !== 'function') return true;
  return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
