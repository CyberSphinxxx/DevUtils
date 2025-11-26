/**
 * Formats a date object to YYYY-MM-DD.
 * @param {Date} date - The date object.
 * @returns {string} - Formatted date string.
 */
const formatDate = (date) => {
    return date.toISOString().split('T')[0];
};

/**
 * Adds days to a date.
 * @param {Date} date - The starting date.
 * @param {number} days - Number of days to add.
 * @returns {Date} - The new date.
 */
const addDays = (date, days) => {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
};

/**
 * Calculates the difference in days between two dates.
 * @param {Date} date1 - The first date.
 * @param {Date} date2 - The second date.
 * @returns {number} - Difference in days.
 */
const daysBetween = (date1, date2) => {
    const oneDay = 24 * 60 * 60 * 1000;
    return Math.round(Math.abs((date1 - date2) / oneDay));
};

module.exports = {
    formatDate,
    addDays,
    daysBetween
};
