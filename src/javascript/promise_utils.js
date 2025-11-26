/**
 * Delays execution for a specified number of milliseconds.
 * @param {number} ms - Milliseconds to delay.
 * @returns {Promise}
 */
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

/**
 * Times out a promise if it takes too long.
 * @param {Promise} promise - The promise to timeout.
 * @param {number} ms - Timeout in milliseconds.
 * @returns {Promise}
 */
const timeout = (promise, ms) => {
    return Promise.race([
        promise,
        new Promise((_, reject) => setTimeout(() => reject(new Error('Timeout')), ms))
    ]);
};

module.exports = {
    delay,
    timeout
};
