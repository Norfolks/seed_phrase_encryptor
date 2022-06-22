# Seed phrase encryptor
Allows to encrypt seed phrase and receive as result encrypted seed phrase. 
The idea of the project is that storing unencrypted seed phrase on the paper not secure enough.
Any rummage of the place where you store your seed could make your funds leak.
So the project adds additional layer of protection for your funds.

## Requirements
Use `python3+`

Run:
```bash
pip install -r requirements.txt
```

## Usage
Store your seed phrase on in the file `origin_seed`. Then run:
```bash
python main.py encrypt --password [your_password]
```
You receive encrypted seed in the `encrypted_seed` file. To decrypt run:
```bash
python main.py decrypt --password [your_password]
```
You decrypted seed now stores in the `decrypted_seed` file.

## Example
The seed phrase:

```shuffle history cushion gain space prosper chicken proof enjoy absorb market light```

Encrypted with password "io":

```dragon oven barrel book basket obscure pet close chronic order cost silent```