from pathlib import Path
import zlib
import struct

assets = Path('assets')
assets.mkdir(exist_ok=True)
projects = [
    ('bodometer.png', (40, 44, 52), 'Bodometer'),
    ('soleway.png', (32, 40, 54), 'SoleWay'),
    ('travel.png', (24, 30, 43), 'Travel Explorer'),
]

def chunk(chunk_type, data):
    return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', zlib.crc32(chunk_type + data) & 0xFFFFFFFF)

for name, color, label in projects:
    path = assets / name
    if path.exists():
        continue
    width, height = 900, 540
    raw = b''.join(b'\x00' + bytes(color) * width for _ in range(height))
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    compressor = zlib.compressobj()
    png += chunk(b'IDAT', compressor.compress(raw) + compressor.flush())
    png += chunk(b'IEND', b'')
    path.write_bytes(png)
