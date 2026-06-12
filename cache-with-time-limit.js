var TimeLimitedCache = function() {
    this.store = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existed = this.store.has(key);
    if (existed) {
        clearTimeout(this.store.get(key).timeoutId);
    }
    const timeoutId = setTimeout(() => {
        this.store.delete(key);
    }, duration);
    this.store.set(key, { value: value, timeoutId: timeoutId });
    return existed;
};

TimeLimitedCache.prototype.get = function(key) {
    if (this.store.has(key)) {
        return this.store.get(key).value;
    }
    return -1;
};

TimeLimitedCache.prototype.count = function() {
    return this.store.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */