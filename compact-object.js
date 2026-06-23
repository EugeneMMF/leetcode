/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        const res = [];
        for (const v of obj) {
            if (Boolean(v)) {
                if (v && typeof v === 'object') {
                    res.push(compactObject(v));
                } else {
                    res.push(v);
                }
            }
        }
        return res;
    }
    if (obj && typeof obj === 'object') {
        const res = {};
        for (const key in obj) {
            if (Object.prototype.hasOwnProperty.call(obj, key)) {
                const v = obj[key];
                if (Boolean(v)) {
                    if (v && typeof v === 'object') {
                        res[key] = compactObject(v);
                    } else {
                        res[key] = v;
                    }
                }
            }
        }
        return res;
    }
    return obj;
};