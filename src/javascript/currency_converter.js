/**
 * Converts an amount from one currency to another using mock rates.
 * @param {number} amount - The amount to convert.
 * @param {string} fromCurrency - The source currency code (e.g., 'USD').
 * @param {string} toCurrency - The target currency code (e.g., 'EUR').
 * @returns {number} The converted amount.
 */
function convertCurrency(amount, fromCurrency, toCurrency) {
    const rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'CAD': 1.25
    };

    if (!rates[fromCurrency] || !rates[toCurrency]) {
        throw new Error('Invalid currency code');
    }

    const amountInUSD = amount / rates[fromCurrency];
    return amountInUSD * rates[toCurrency];
}

module.exports = convertCurrency;
