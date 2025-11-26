/**
 * Wrapper for fetch API with error handling.
 * @param {string} url - URL to fetch.
 * @param {object} options - Fetch options.
 * @returns {Promise}
 */
const request = async (url, options = {}) => {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            return await response.json();
        } else {
            return await response.text();
        }
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    }
};

module.exports = {
    request
};
