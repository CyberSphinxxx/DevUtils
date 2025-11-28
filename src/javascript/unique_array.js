/**
 * Returns an array with unique values.
 * @param {Array} arr - The input array.
 * @returns {Array} The array with unique values.
 */
function uniqueArray(arr) {
    return [...new Set(arr)];
}

module.exports = uniqueArray;
