/**
 * Parses the query string of a URL into an object.
 * @param {string} url - The URL to parse.
 * @returns {Object} An object containing the query parameters.
 */
function parseUrlQuery(url) {
    const query = {};
    const queryString = url.split('?')[1];

    if (!queryString) {
        return query;
    }

    const pairs = queryString.split('&');

    for (let i = 0; i < pairs.length; i++) {
        const pair = pairs[i].split('=');
        query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
    }

    return query;
}

module.exports = parseUrlQuery;
