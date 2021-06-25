# pi_protocol

## How to use

```
import pi_protocol

data: bytes = b"\x82\x05\x00Steve\x09\x00\x00\x00\x09\x00\x00\x00"
decoded_packet: dict = pi_protocol.decode_packet(data)
print("Decoded your packet :)")
print(decoded_packet)
print("let's reencode it :)")
encoded_packet: bytes = pi_protocol.encode_packet(decoded_packet)
print(encoded_packet)
```
