#!/usr/bin/env node

// JS Implementation
// See 1.py for problem details
// To run this, `node 1.js` and will error if any tests do not pass

const assert = require('assert')

function is_sum(n, k) {
    solns = {}
    for(let i in n) {
        if(solns[n[i]]) return true
        solns[k - n[i]] = true
    }
    return false
}

assert(is_sum([10, 15, 3, 7], 17))
assert(!is_sum([1, 2, 3, 4, 5, 6, 7], 1))
assert(!is_sum([1, 2, 3, 4, 5, 6, 7], 2))
assert(is_sum([1, 2, 3, 4, 5, 6, 7], 3))