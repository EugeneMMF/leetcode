/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let resolvedCount = 0;
        for (let i = 0; i < functions.length; i++) {
            let p;
            try {
                p = functions[i]();
            } catch (e) {
                reject(e);
                return;
            }
            Promise.resolve(p).then(value => {
                results[i] = value;
                resolvedCount++;
                if (resolvedCount === functions.length) {
                    resolve(results);
                }
            }).catch(err => {
                reject(err);
            });
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
