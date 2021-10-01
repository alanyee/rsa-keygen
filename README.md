# rsa-keygen
Generate textbook integer-type RSA schema for fun/[CTF](https://ctftime.org/)s. Tested for primes numbers up to 300 digits.

## usage

```
usage: rsa.py [-h] [-m MESSAGE] [-l prime_length] [-ls prime_lengths prime_lengths]
              [-p prime prime] [-e exponent]

CTF RSA Generator

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Message to be encrypted and decrypted
  -l prime_length, --prime-length prime_length
                        Generate both prime numbers with the given length (in bytes)
  -ls prime_lengths prime_lengths, --prime-lengths prime_lengths prime_lengths
                        Generate prime numbers from the given length (in bytes). Takes precedence over prime_length.
  -p prime prime, --primes prime prime
                        Load from two big prime numbers. Takes  precedence over prime_length and prime_lengths.
  -e exponent, --exponent exponent
                        Load from exponent
 ```
