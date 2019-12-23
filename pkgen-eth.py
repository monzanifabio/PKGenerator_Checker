from ecdsa import SigningKey, SECP256k1
import sha3
from ethplorer.address import Address

i=0

while True:
    #Code taken from Vincent Kobel. License at: https://github.com/vkobel/ethereum-generate-wallet/blob/master/LICENSE.md
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)

    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    address = '0x' + address
    #End of attributed code

    ADD = Address(address = address)

    info = ADD.get_address_info()
    #print(priv.to_string().hex(), address, info['ETH'])
    try:
        if info['ETH']['balance'] != 0:
            print(priv.to_string().hex(), address, info['ETH'])
    except:
        print('An error occured')

    if (i % 100) == 0:
        print(i)
    i=i+1
