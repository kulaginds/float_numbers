import struct


def float_to_int_data(f: float):
    return struct.unpack('<Q', struct.pack('<d', f))[0]