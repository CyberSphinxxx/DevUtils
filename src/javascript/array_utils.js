/**
 * Splits an array into chunks of a specific size.
 * @param {Array} array - The array to process.
 * @param {number} size - The size of each chunk.
 * @returns {Array[]} - An array of chunks.
 */
const chunk = (array, size) => {
    const chunked = [];
    let index = 0;
    while (index < array.length) {
        chunked.push(array.slice(index, index + size));
        index += size;
    }
    return chunked;
};

/**
 * Returns a new array with unique values.
 * @param {Array} array - The input array.
 * @returns {Array} - Array with unique values.
 */
const unique = (array) => {
    return [...new Set(array)];
};

/**
 * Flattens a nested array structure.
 * @param {Array} array - The array to flatten.
 * @returns {Array} - Flattened array.
 */
const flatten = (array) => {
    return array.reduce((acc, val) =>
        Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []
    );
};

module.exports = {
    chunk,
    unique,
    flatten
};
