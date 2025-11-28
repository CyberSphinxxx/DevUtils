/**
 * Truncates a string to a specified length.
 * @param {string} str - The string to truncate.
 * @param {number} length - The maximum length.
 * @param {string} [ending='...'] - The string to append if truncated.
 * @returns {string} The truncated string.
 */
function truncate(str, length, ending = '...') {
    if (str.length > length) {
        return str.substring(0, length - ending.length) + ending;
    }
    return str;
}

module.exports = truncate;
