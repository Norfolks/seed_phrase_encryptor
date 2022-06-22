import argparse
import math
from bitarray import bitarray

from Crypto.Hash import SHA256
from Crypto.Cipher import ChaCha20

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['encrypt', 'decrypt'])
parser.add_argument('--password', type=str, required=True)
parser.add_argument("-i", help="Input file path.", type=str)
parser.add_argument("-o", help="Output file path.", type=str)

SALT = b"BIG_CRYPTO_SALT_FROM_NOWHERE_IT_IS_VERY_SECURE_TO_SALT_YOUR_PASSWORD_FOR_SEED_PHRASE"
NONCE = b"qm7ybd[."

with open('words', 'r') as words_file:
    i2w_dict = {index: line.strip() for index, line in enumerate(words_file)}
    w2i_dict = {v: k for k, v in i2w_dict.items()}


def seed_to_bytes(seed):
    bits = bitarray()
    [
        [bits.append(int(x)) for x in '{0:011b}'.format(w2i_dict[word])]
        for word in seed
    ]
    return bits.tobytes()


def bytes_to_seed(in_bytes):
    bits = bitarray()
    bits.frombytes(in_bytes)
    seed = []
    for i in range(math.floor(len(bits) / 11)):
        seed.append(
            i2w_dict[
                int(bits[i * 11: (i + 1) * 11].to01(), 2)
            ]
        )
    return seed


if __name__ == "__main__":
    args = vars(parser.parse_args())
    args = {k: v for k, v in args.items() if v is not None}
    mode = args['mode']
    in_path = None
    out_path = None
    if mode == 'encrypt':
        in_path = args.get('i', 'origin_seed')
        out_path = args.get('o', 'encrypted_seed')
    if mode == 'decrypt':
        in_path = args.get('i', 'encrypted_seed')
        out_path = args.get('o', 'decrypted_seed')

    password = SHA256.new(data=str.encode(args['password']))
    password.update(SALT)
    key = password.digest()

    with open(in_path, 'r') as inf:
        seed = inf.readline().split()

    cryptor = ChaCha20.new(key=key, nonce=NONCE)
    msg = seed_to_bytes(seed)
    precessed = cryptor.encrypt(msg)
    new_seed = bytes_to_seed(precessed)

    with open(out_path, 'w') as outf:
        outf.write(" ".join(new_seed))

    print("Done.")
