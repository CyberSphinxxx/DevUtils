/**
 * Creates a throttled function that only invokes func at most once per every wait milliseconds.
 * @param {Function} func - The function to throttle.
 * @param {number} wait - The number of milliseconds to throttle.
 * @returns {Function} - The throttled function.
 */
const throttle = (func, wait) => {
    let inThrottle, lastFn, lastTime;
    return function (...args) {
        const context = this,
            now = Date.now();
        if (!inThrottle) {
            func.apply(context, args);
            lastTime = now;
            inThrottle = true;
        } else {
            clearTimeout(lastFn);
            lastFn = setTimeout(function () {
                if (Date.now() - lastTime >= wait) {
                    func.apply(context, args);
                    lastTime = Date.now();
                }
            }, Math.max(wait - (now - lastTime), 0));
        }
    };
};

module.exports = throttle;
