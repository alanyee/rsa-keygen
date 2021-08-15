# rsa-keygen
Generate textbook integer-type RSA schema for fun/[CTF](https://ctftime.org/)s. Tested for primes numbers up to 300 digits.

## usage

```
usage: rsa-keygen [-h] [-m MESSAGE] [-p prime prime] [-e exponent]

CTF RSA Generator

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Message to be encrypted and decrypted
  -p prime prime, --primes prime prime
                        Load from two big prime numbers
  -e exponent, --exponent exponent
                        Load from two big prime numbers
 ```
