/**
 * Flattens a nested array.
 * @param {Array} arr - The array to flatten.
 * @param {number} [depth=1] - The depth to flatten.
 * @returns {Array} The flattened array.
 */
function flattenArray(arr, depth = 1) {
    return arr.flat(depth);
}

module.exports = flattenArray;
