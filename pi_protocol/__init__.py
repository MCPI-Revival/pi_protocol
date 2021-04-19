################################################################################
#                                                                              #
#  __  __ _____ ____   ____                 _                                  #
# |  \/  |  ___|  _ \ / ___| __ _ _ __ ___ (_)_ __   __ _                      #
# | |\/| | |_  | | | | |  _ / _` | '_ ` _ \| | '_ \ / _` |                     #
# | |  | |  _| | |_| | |_| | (_| | | | | | | | | | | (_| |                     #
# |_|  |_|_|   |____/ \____|\__,_|_| |_| |_|_|_| |_|\__, |                     #
#                                                    |___/                     #
# Copyright 2021 MFDGaming                                                     #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from binary_utils.binary_stream import binary_stream
import os
from typing import Union

def get_data_folder() -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")

def decode_data_type(data_type: str, stream: object) -> Union[int, float, str]:
    if data_type == "UnsignedByte":
        return stream.read_unsigned_byte()
    if data_type == "Byte":
        return stream.read_byte()
    if data_type == "UnsignedShortBE":
        return stream.read_unsigned_short_be()
    if data_type == "ShortBE":
        return stream.read_short_be()
    if data_type == "UnsignedShortLE":
        return stream.read_unsigned_short_le()
    if data_type == "ShortLE":
        return stream.read_short_le()
    if data_type == "UnsignedTriadBE":
        return stream.read_unsigned_triad_be()
    if data_type == "TriadBE":
        return stream.read_triad_be()
    if data_type == "UnsignedTriadLE":
        return stream.read_unsigned_triad_le()
    if data_type == "TriadLE":
        return stream.read_triad_le()
    if data_type == "UnsignedIntBE":
        return stream.read_unsigned_int_be()
    if data_type == "IntBE":
        return stream.read_int_be()
    if data_type == "UnsignedIntLE":
        return stream.read_unsigned_int_le()
    if data_type == "IntLE":
        return stream.read_int_le()
    if data_type == "UnsignedLongBE":
        return stream.read_unsigned_long_be()
    if data_type == "LongBE":
        return stream.read_long_be()
    if data_type == "UnsignedLongLE":
        return stream.read_unsigned_long_le()
    if data_type == "LongLE":
        return stream.read_long_le()
    if data_type == "FloatBE":
        return stream.read_float_be()
    if data_type == "FloatLE":
        return stream.read_float_le()
    if data_type == "DoubleBE":
        return stream.read_double_be()
    if data_type == "DoubleLE":
        return stream.read_double_le()
    if data_type == "String":
        return stream.read(stream.read_unsigned_short_be()).decode()

def encode_data_type(data_type: str, value: Union[int, float, str], stream: object) -> None:
    if data_type == "UnsignedByte":
        stream.write_unsigned_byte(value)
    if data_type == "Byte":
        stream.write_byte(value)
    if data_type == "UnsignedShortBE":
        stream.write_unsigned_short_be(value)
    if data_type == "ShortBE":
        stream.write_short_be(value)
    if data_type == "UnsignedShortLE":
        stream.write_unsigned_short_le(value)
    if data_type == "ShortLE":
        stream.write_short_le(value)
    if data_type == "UnsignedTriadBE":
        stream.write_unsigned_triad_be(value)
    if data_type == "TriadBE":
        stream.write_triad_be(value)
    if data_type == "UnsignedTriadLE":
        stream.write_unsigned_triad_le(value)
    elif data_type == "TriadLE":
        stream.write_triad_le(value)
    elif data_type == "UnsignedIntBE":
        stream.write_unsigned_int_be(value)
    elif data_type == "IntBE":
        stream.write_int_be(value)
    elif data_type == "UnsignedIntLE":
        stream.write_unsigned_int_le(value)
    elif data_type == "IntLE":
        stream.write_int_le(value)
    elif data_type == "UnsignedLongBE":
        stream.write_unsigned_long_be(value)
    elif data_type == "LongBE":
        stream.write_long_be(value)
    elif data_type == "UnsignedLongLE":
        stream.write_unsigned_long_le(value)
    elif data_type == "LongLE":
        stream.write_long_le(value)
    elif data_type == "FloatBE":
        stream.write_float_be(value)
    elif data_type == "FloatLE":
        stream.write_float_le(value)
    elif data_type == "DoubleBE":
        stream.write_double_be(value)
    elif data_type == "DoubleLE":
        stream.write_double_le(value)
    elif data_type == "String":
        stream.write_unsigned_short_be(len(value))
        stream.write(value.encode())
    
def decode_packet(data: bytes) -> dict:
    pass
