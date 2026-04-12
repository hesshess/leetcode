/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;

    const count = {};

    for (let ch of s){
        count[ch] = (count[ch] || 0) + 1;
    }

    for (let ch of t){
        if (!count[ch]) return false;
        count[ch]--;
    }

    return true;
};