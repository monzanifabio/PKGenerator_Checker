import sha3
from ecdsa import SigningKey, SECP256k1

keccak = sha3.keccak_256()
private = SigningKey.generate(curve=SECP256k1)
public = private.get_verifying_key().to_string()
keccak.update(public)
address = "0x{}".format(keccak.hexdigest()[24:])
