/**
 * Selects an element from the DOM.
 * @param {string} selector - CSS selector.
 * @returns {Element}
 */
const $ = (selector) => document.querySelector(selector);

/**
 * Selects all elements from the DOM.
 * @param {string} selector - CSS selector.
 * @returns {NodeList}
 */
const $$ = (selector) => document.querySelectorAll(selector);

/**
 * Adds an event listener to an element.
 * @param {Element} element - DOM element.
 * @param {string} event - Event name.
 * @param {Function} handler - Event handler.
 */
const on = (element, event, handler) => {
    if (element) {
        element.addEventListener(event, handler);
    }
};

module.exports = {
    $,
    $$,
    on
};
