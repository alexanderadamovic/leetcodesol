/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const root = new Map();
    const RESULT = Symbol("result");

    return function (...args) {
        let current = root;

        for (const arg of args) {
            if (!current.has(arg)) {
                current.set(arg, new Map());
            }

            current = current.get(arg);
        }

        if (current.has(RESULT)) {
            return current.get(RESULT);
        }

        const value = fn.apply(this, args);
        current.set(RESULT, value);

        return value;
    };
}
        




