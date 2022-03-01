from pyzbar.pyzbar import decode, ZBarSymbol
from cv2 import imread
from base45 import b45decode
import zlib
import cbor2
import json

# reading QR image
qrInfo = decode(imread('QR_Example1.png'), symbols=[ZBarSymbol.QRCODE])
# removing HC1: prefix
data = qrInfo[0][0].decode().replace("HC1:", "")
# decoding Base45
decodeData = b45decode(data)
# decompressing using zlib
decompressed = zlib.decompress(decodeData)
# decoding message
decoded = cbor2.loads(decompressed) # hasta aqui igual
# decode load json from message
dictResult = cbor2.loads(decoded.value[2])
# printing decoded message in Json format
print((json.dumps(dictResult, ensure_ascii=False, indent=2).encode('utf8')).decode())