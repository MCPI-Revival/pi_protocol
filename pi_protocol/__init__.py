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

def get_data_folder() -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")

def decode_data_type(data_type: str, stream: object) -> object:
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

def decode_packet(data: bytes) -> dict:
    pass
