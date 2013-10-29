
import sys
import binascii


def xorsum(val1, val2):
    """Create xor sum between two strings"""
    password = ''
    for a, b in zip(val1, val2):
        password = ''.join([password, chr(ord(a) ^ ord(b))])
    return password


def encode_xor(password):
    """Encode a password into the xor format, useful if importing script into larger automated"""
    cipher = '_' * len(password)
    return '{xor}' + binascii.b2a_base64(xorsum(password, cipher))


def decode_xor(xor_str):
    """Will decode am xor'ed password from the format stored in the security.xml"""
    xor_str = xor_str.replace('{xor}', '')
    value1 = binascii.a2b_base64(xor_str)
    value2 = '_' * len(value1)
    return xorsum(value1, value2)


if __name__ == '__main__':
    if len(sys.argv) > 1:  # python
        print decode_xor(sys.argv[1])
    elif len(sys.argv) > 0 and sys.executable is None:  # wsadmin
        print decode_xor(sys.argv[0])
    else:
        print "Usage: decode_xor.py <xor'ed string>"
        print "Example: wsadmin.sh -f xor_decode.py {xor}Lz4sLCgwLTs="
        print "or"
        print "Example: python xor_decode.py {xor}Lz4sLCgwLTs="
