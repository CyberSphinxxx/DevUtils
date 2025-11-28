/**
 * Deep merges two objects.
 * @param {Object} target - The target object.
 * @param {Object} source - The source object.
 * @returns {Object} The merged object.
 */
function mergeObjects(target, source) {
    for (const key in source) {
        if (source[key] instanceof Object && key in target) {
            Object.assign(source[key], mergeObjects(target[key], source[key]));
        }
    }
    Object.assign(target || {}, source);
    return target;
}

module.exports = mergeObjects;
