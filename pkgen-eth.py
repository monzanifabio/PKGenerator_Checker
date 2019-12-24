from eth_keys import keys
pk = keys.PrivateKey(b'\x01' * 32)
signature = pk.sign_msg(b'a message')
pk
#'0x0101010101010101010101010101010101010101010101010101010101010101'
pk.public_key
#'0x1b84c5567b126440995d3ed5aaba0565d71e1834604819ff9c17f5e9d5dd078f70beaf8f588b541507fed6a642c5ab42dfdf8120a7f639de5122d47a69a8e8d1'
signature
#'0xccda990dba7864b79dc49158fea269338a1cf5747bc4c4bf1b96823e31a0997e7d1e65c06c5bf128b7109e1b4b9ba8d1305dc33f32f624695b2fa8e02c12c1e000'
pk.public_key.to_checksum_address()
#'0x1a642f0E3c3aF545E7AcBD38b07251B3990914F1'
signature.verify_msg(b'a message', pk.public_key)
#True
signature.recover_msg(b'a message') == pk.public_key
#True
