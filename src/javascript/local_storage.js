const storage = {
    /**
     * Sets an item in local storage.
     * @param {string} key - The key.
     * @param {any} value - The value (will be JSON stringified).
     */
    set: (key, value) => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.error("Error saving to localStorage", e);
        }
    },

    /**
     * Gets an item from local storage.
     * @param {string} key - The key.
     * @returns {any} - The parsed value.
     */
    get: (key) => {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : null;
        } catch (e) {
            console.error("Error reading from localStorage", e);
            return null;
        }
    },

    /**
     * Removes an item from local storage.
     * @param {string} key - The key.
     */
    remove: (key) => {
        localStorage.removeItem(key);
    },

    /**
     * Clears all items from local storage.
     */
    clear: () => {
        localStorage.clear();
    }
};

module.exports = storage;
