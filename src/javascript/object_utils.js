/**
 * Merges two objects deeply.
 * @param {object} target - Target object.
 * @param {object} source - Source object.
 * @returns {object} - Merged object.
 */
const merge = (target, source) => {
    for (const key in source) {
        if (source[key] instanceof Object && key in target) {
            Object.assign(source[key], merge(target[key], source[key]));
        }
    }
    Object.assign(target || {}, source);
    return target;
};

/**
 * Picks keys from an object.
 * @param {object} obj - Source object.
 * @param {Array} keys - Keys to pick.
 * @returns {object} - New object with picked keys.
 */
const pick = (obj, keys) => {
    const result = {};
    keys.forEach(key => {
        if (key in obj) {
            result[key] = obj[key];
        }
    });
    return result;
};

module.exports = {
    merge,
    pick
};
