"""
JS implementation
let isPrime = (x) => {
    for (let y = 2; y < x; y++)
      if (x % y === 0) return false;
    return true;
};
"""


def isPrime(x):
    if(x % 2 == 0):
        return True
    else:
        return False
