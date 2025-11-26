/**
 * Converts a string to a URL-friendly slug.
 * @param {string} str - The string to slugify.
 * @returns {string} - The slugified string.
 */
const slugify = (str) => {
    return str
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, '')
        .replace(/[\s_-]+/g, '-')
        .replace(/^-+|-+$/g, '');
};

/**
 * Capitalizes the first letter of each word in a string.
 * @param {string} str - The input string.
 * @returns {string} - The capitalized string.
 */
const capitalize = (str) => {
    return str.replace(/\b\w/g, (char) => char.toUpperCase());
};

/**
 * Truncates a string to a specified length and adds an ellipsis.
 * @param {string} str - The string to truncate.
 * @param {number} length - The maximum length.
 * @returns {string} - The truncated string.
 */
const truncate = (str, length) => {
    if (str.length <= length) return str;
    return str.slice(0, length) + '...';
};

module.exports = {
    slugify,
    capitalize,
    truncate
};
