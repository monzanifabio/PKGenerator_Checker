import secrets
import sha3
import eth_keys
from eth_keys import keys

private_key = str(hex(secrets.randbits(256))[2:])
private_key_bytes = bytes.fromhex(private_key)
public_key_hex = keys.PrivateKey(private_key_bytes).public_key
public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
keccak256_of_public_key_bytes = sha3.keccak_256(public_key_bytes).hexdigest()
public_address = keys.PublicKey(public_key_bytes).to_address()
checksum = keys.PublicKey(public_key_bytes).to_checksum_address()

print('\n Private_key:',private_key,
      '\n Private_key_bytes:',private_key_bytes,
      '\n Public_key_hex:',public_key_hex,
      '\n Public_key_bytes:',public_key_bytes,
      '\n Full_Keccak_digest:',keccak256_of_public_key_bytes,
      '\n Ethereum address:',public_address,
      '\n Checksum Format of Above Ethereum:',checksum)
