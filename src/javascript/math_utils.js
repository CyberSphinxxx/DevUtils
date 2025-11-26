/**
 * Clamps a number between a minimum and maximum value.
 * @param {number} num - The number to clamp.
 * @param {number} min - The minimum value.
 * @param {number} max - The maximum value.
 * @returns {number} - The clamped value.
 */
const clamp = (num, min, max) => {
    return Math.min(Math.max(num, min), max);
};

/**
 * Generates a random integer between min and max (inclusive).
 * @param {number} min - The minimum value.
 * @param {number} max - The maximum value.
 * @returns {number} - The random integer.
 */
const randomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

/**
 * Calculates the factorial of a number.
 * @param {number} n - The number.
 * @returns {number} - The factorial.
 */
const factorial = (n) => {
    if (n < 0) return -1;
    if (n == 0) return 1;
    return n * factorial(n - 1);
};

module.exports = {
    clamp,
    randomInt,
    factorial
};
