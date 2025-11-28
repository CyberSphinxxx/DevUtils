/**
 * Checks if a value is empty (null, undefined, empty string, empty array, empty object).
 * @param {*} value - The value to check.
 * @returns {boolean} True if empty, false otherwise.
 */
function isEmpty(value) {
    if (value === null || value === undefined) return true;
    if (typeof value === 'string' && value.trim() === '') return true;
    if (Array.isArray(value) && value.length === 0) return true;
    if (typeof value === 'object' && Object.keys(value).length === 0) return true;
    return false;
}

module.exports = isEmpty;
