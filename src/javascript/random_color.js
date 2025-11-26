/**
 * Generates a random hex color.
 * @returns {string} - Hex color.
 */
const randomHexColor = () => {
    return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
};

/**
 * Generates a random RGB color.
 * @returns {string} - RGB string.
 */
const randomRgbColor = () => {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
};

module.exports = {
    randomHexColor,
    randomRgbColor
};
