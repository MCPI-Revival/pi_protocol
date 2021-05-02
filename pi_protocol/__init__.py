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
import json
import os
from typing import Union

def get_data_folder() -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")

protocol: dict = json.load(open(get_data_folder() + "/protocol.json", "rt"))

def get_packet_fields(packet_id: int) -> dict:
    for packet in protocol.values():
        if packet["id"] == packet_id:
            return packet["fields"]

def decode_data_type(data_type: str, stream: object) -> Union[int, float, str, list]:
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
    if data_type == "Metadata":
        result: list = []
        while True:
            b: int = stream.read_unsigned_byte()
            if b == 127:
                break
            m_type: int = int(b / 32)
            if m_type == 0:
                m_value: int = stream.read_byte()
                result.append([m_type, m_value])
            elif m_type == 1:
                m_value: int = stream.read_short_le()
                result.append([m_type, m_value])
            elif m_type == 2:
                m_value: int = stream.read_int_le()
                result.append([m_type, m_value])
            elif m_type == 3:
                m_value: float = stream.read_float_le()
                result.append([m_type, m_value])
            elif m_type == 4:
                m_value: str = stream.read(stream.read_unsigned_short_le())
                result.append([m_type, m_value])
            elif m_type == 5:
                m_value: list = []
                m_value.append(stream.read_short_le())
                m_value.append(stream.read_byte())
                m_value.append(stream.read_short_le())
                result.append([m_type, m_value])
            elif m_type == 6:
                m_value: list = []
                m_value.append(stream.read_int_le())
                m_value.append(stream.read_int_le())
                m_value.append(stream.read_int_le())
                result.append([m_type, m_value])
        return result
    if data_type == "Records":
        records: list = []
        count: int = stream.read_int_be()
        for i in range(0, count):
            index: list = []
            index.append(stream.read_byte())
            index.append(stream.read_byte())
            index.append(stream.read_byte())
            records.append(index)
        return records
    if data_type == "ChunkData":
        pass
    if data_type == "Items":
        count: int = stream.read_unsigned_short_be()
        items: list = []
        for i in range(0, count):
            item: list = []
            item.append(stream.read_short_be())
            item.append(stream.read_byte())
            item.append(stream.read_short_be())
            items.append(item)
        return items
    if data_type == "Armor":
        items: list = []
        for i in range(0, 4):
            item: list = []
            item.append(stream.read_short_be())
            item.append(stream.read_byte())
            item.append(stream.read_short_be())
            items.append(item)
        return items
    if data_type == "Item":
        item: list = []
        item.append(stream.read_short_be())
        item.append(stream.read_byte())
        item.append(stream.read_short_be())
        return item

def encode_data_type(data_type: str, value: Union[int, float, str, list], stream: object) -> None:
    if data_type == "UnsignedByte":
        stream.write_unsigned_byte(value)
    elif data_type == "Byte":
        stream.write_byte(value)
    elif data_type == "UnsignedShortBE":
        stream.write_unsigned_short_be(value)
    elif data_type == "ShortBE":
        stream.write_short_be(value)
    elif data_type == "UnsignedShortLE":
        stream.write_unsigned_short_le(value)
    elif data_type == "ShortLE":
        stream.write_short_le(value)
    elif data_type == "UnsignedTriadBE":
        stream.write_unsigned_triad_be(value)
    elif data_type == "TriadBE":
        stream.write_triad_be(value)
    elif data_type == "UnsignedTriadLE":
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
    elif data_type == "Metadata":
        for m_type, m_value in value:
            stream.write_unsigned_byte((m_type & 0x1f) | (m_type * 32))
            if m_type == 0:
                stream.write_byte(m_value)
            elif m_type == 1:
                stream.write_short_le(m_value)
            elif m_type == 2:
                stream.write_int_le(m_value)
            elif m_type == 3:
                stream.write_float_le(m_value)
            elif m_type == 4:
                stream.write_unsigned_short_le(len(m_value))
                stream.write(m_value.encode())
            elif m_type == 5:
                stream.write_short_le(m_value[0])
                stream.write_byte(m_value[1])
                stream.write_short_le(m_value[2])
            elif m_type == 6:
                stream.write_int_le(m_value[0])
                stream.write_int_le(m_value[1])
                stream.write_int_le(m_value[2])
        stream.write_byte(0x7f)
    elif data_type == "Records":
        stream.write_int_be(len(value))
        for index in value:
            stream.write_byte(index[0])
            stream.write_byte(index[1])
            stream.write_byte(index[2])
    elif data_type == "ChunkData":
        pass
    elif data_type == "Items":
        stream.write_unsigned_short_be(len(value))
        for item in value:
            stream.write_short_be(item[0])
            stream.write_byte(item[1])
            stream.write_short_be(item[2])
    elif data_type == "Armor":
        for item in value:
            stream.write_short_be(item[0])
            stream.write_byte(item[1])
            stream.write_short_be(item[2])
    elif data_type == "Item":
        stream.write_short_be(value[0])
        stream.write_byte(value[1])
        stream.write_short_be(value[2])
    
def decode_packet(data: bytes) -> dict:
    stream: object = binary_stream(data)
    packet_id: int = stream.read_unsigned_byte()
    packet_fields: dict = get_packet_fields(packet_id)
    if packet_fields is not None:
        packet: dict = {"id": packet_id}
        for field_name, field_type in packet_fields.items():
            packet[field_name]: Union[int, float, str, list] = decode_data_type(field_type, stream)
        return packet
    else:
        return {}

def encode_packet(packet: dict) -> bytes:
    stream: object = binary_stream()
    packet_fields: dict = get_packet_fields(packet["id"])
    if packet_fields is not None:
        stream.write_unsigned_byte(packet["id"])
        for field_name, field_type in packet_fields.items():
            encode_data_type(field_type, packet[field_name], stream)
        return stream.data
    else:
        return b""
