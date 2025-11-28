/**
 * Retries a function a specified number of times.
 * @param {Function} fn - The function to retry.
 * @param {number} retries - The number of retries.
 * @param {number} delay - The delay between retries in ms.
 * @returns {Promise} A promise that resolves with the function result.
 */
async function retry(fn, retries = 3, delay = 1000) {
    try {
        return await fn();
    } catch (err) {
        if (retries <= 0) throw err;
        await new Promise(resolve => setTimeout(resolve, delay));
        return retry(fn, retries - 1, delay);
    }
}

module.exports = retry;
