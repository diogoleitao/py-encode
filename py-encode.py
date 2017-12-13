from math import ceil, log


def encode_string(s):
    bytes = [ord(c) for c in s]
    num = sum(bytes[i] * 256 ** i for i in xrange(len(bytes)))
    return reduce(num, 0)


def reduce(num, depth):
    def _encode(num, depth):
        if num == 0:
            return "_ - _"
        if num in range(9):
            return "_" * num
        return "(" + reduce(num, depth + 1) + ")"

    result = ""
    while num:
        best_base = best_shift = 0
        best = num
        span = int(ceil(log(abs(num), 1.5))) + (16 >> depth)
        for base in xrange(span):
            for shift in xrange(span):
                diff = abs(num) - (base << shift)
                if abs(diff) < abs(best):
                    best = diff
                    best_base = base
                    best_shift = shift
        if result:
            result += " + " if num > 0 else " - "
        elif num < 0:
            best_base = -best_base
        if best_shift == 0:
            result += _encode(best_base, depth)
        else:
            result += "(%s << %s)" % (_encode(best_base, depth), _encode(best_shift, depth))
        num = best if num > 0 else -best
    return result
