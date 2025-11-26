/**
 * Copies text to clipboard (Browser only).
 * @param {string} text - Text to copy.
 * @returns {Promise}
 */
const copyToClipboard = async (text) => {
    if (!navigator.clipboard) {
        return Promise.reject('Clipboard API not available');
    }
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        console.error('Failed to copy: ', err);
        return false;
    }
};

/**
 * Reads text from clipboard (Browser only).
 * @returns {Promise<string>}
 */
const readFromClipboard = async () => {
    if (!navigator.clipboard) {
        return Promise.reject('Clipboard API not available');
    }
    try {
        const text = await navigator.clipboard.readText();
        return text;
    } catch (err) {
        console.error('Failed to read: ', err);
        return null;
    }
};

module.exports = {
    copyToClipboard,
    readFromClipboard
};
