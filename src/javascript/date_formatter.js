/**
 * Formats a date object into a readable string.
 * @param {Date} date - The date to format.
 * @param {string} format - The format string (e.g., 'YYYY-MM-DD').
 * @returns {string} The formatted date string.
 */
function formatDate(date, format = 'YYYY-MM-DD') {
    const map = {
        'MM': ('0' + (date.getMonth() + 1)).slice(-2),
        'DD': ('0' + date.getDate()).slice(-2),
        'YYYY': date.getFullYear(),
        'HH': ('0' + date.getHours()).slice(-2),
        'mm': ('0' + date.getMinutes()).slice(-2),
        'ss': ('0' + date.getSeconds()).slice(-2)
    };

    return format.replace(/MM|DD|YYYY|HH|mm|ss/gi, matched => map[matched]);
}

module.exports = formatDate;
