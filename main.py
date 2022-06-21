import argparse

from Crypto.Hash import SHA256
from Crypto.Cipher import ChaCha20

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['encrypt', 'decrypt'])
parser.add_argument('--password', type=str, required=True)
parser.add_argument("-i", help="Input file path.", type=str, default="origin_seed")
parser.add_argument("-o", help="Output file path.", type=str, default="encrypted_seed")

SALT = b"BIG_CRYPTO_SALT_FROM_NOWHERE_IT_IS_VERY_SECURE"

def seed_to_bytes(seed, convert_dict):
    [

    ]
    [int(x) for x in '{0:07b}'.format(12)]

if __name__ == "__main__":
    args = parser.parse_args()
    mode = args.mode
    in_path = args.i
    out_path = args.o
    password = SHA256.new(data=str.encode(args.password))
    password.update(SALT)
    key = password.digest()

    with open('words', 'r') as words_file:
        i2w_dict = {index: line for index, line in enumerate(words_file)}
        w2i_dict = {v: k for k, v in i2w_dict.items()}
