/**
 * Pauses execution for a specified duration.
 * @param {number} ms - The duration in milliseconds.
 * @returns {Promise} A promise that resolves after the duration.
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

module.exports = sleep;
