/**
 * Parses a query string into an object.
 * @param {string} queryString - The query string.
 * @returns {object} - The parsed object.
 */
const parseQueryParams = (queryString) => {
    const params = new URLSearchParams(queryString);
    const obj = {};
    for (const [key, value] of params) {
        obj[key] = value;
    }
    return obj;
};

/**
 * Stringifies an object into a query string.
 * @param {object} obj - The object to stringify.
 * @returns {string} - The query string.
 */
const stringifyQueryParams = (obj) => {
    return new URLSearchParams(obj).toString();
};

module.exports = {
    parseQueryParams,
    stringifyQueryParams
};
