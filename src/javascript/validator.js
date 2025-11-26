/**
 * Validates an email address.
 * @param {string} email - The email to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
const isEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
};

/**
 * Validates a URL.
 * @param {string} url - The URL to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
const isURL = (url) => {
    try {
        new URL(url);
        return true;
    } catch (_) {
        return false;
    }
};

/**
 * Checks if a string contains only numbers.
 * @param {string} str - The string to check.
 * @returns {boolean} - True if numeric, false otherwise.
 */
const isNumeric = (str) => {
    return /^\d+$/.test(str);
};

module.exports = {
    isEmail,
    isURL,
    isNumeric
};
