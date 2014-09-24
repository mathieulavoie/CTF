import itertools


def xor_strings(*args):
    xored_string_bytes = xor_bytes(*map(lambda s: [ord(c) for c in s], args))
    return "".join(map(chr, xored_string_bytes))


def xor_bytes(*args):
    assert (len(args) >= 2)

    bytes_list = sorted(args,key=len, reverse=True)
    xored_result = bytes_list[0]
    bytes_list = bytes_list[1:]
    for byte_list in bytes_list:
        xored_result = [x ^ y for x, y in zip(xored_result, itertools.cycle(byte_list))]
    return xored_result


def unit_test():
    assert(xor_strings("AAA","A") == "\x00"*3)  # Basic test
    assert(xor_strings("AAA","A","B") == "BBB")  # Multiple xor result
    assert(xor_strings("AAA","A") == xor_strings("AA","AAA"))  # Result always the len of the longest string
    assert(xor_strings("AAA","A") == xor_strings("AA","AAA","\x00"))  # A null string should not change xor result


if __name__ == "__main__":
    unit_test()  # Run Unit Test