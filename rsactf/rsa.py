import argparse
import math
import sys
from Cryptodome.Util import number


N_LENGTH = 2048


def _parse_args():
    parser = argparse.ArgumentParser(description='CTF RSA Generator')
    parser.add_argument("-m", "--message", type=str,
                        help="Message to be encrypted and decrypted")
    parser.add_argument("-l", "--prime-length", nargs=1, type=int, metavar="prime_length", default=N_LENGTH,
                        help="Generate both prime numbers with the given length (in bytes)")
    parser.add_argument("-ls", "--prime-lengths", nargs=2, type=int, metavar="prime_lengths",
                        help="Generate prime numbers from the given length (in bytes). Takes precedence over prime_length.")
    parser.add_argument("-p", "--primes", nargs=2, type=int, metavar="prime", default=[0, 0],
                        help="Load from two big prime numbers. Takes precedence over prime_length and prime_lengths.")
    parser.add_argument("-e", "--exponent", type=int, metavar="exponent", default=65537,
                        help="Load from exponent")

    return parser, parser.parse_args()


def main():
    parser, args = _parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    e = args.exponent
    if args.message:
        m = int(args.message.encode().hex(), 16)
        print("m:")
        print(m)

    for i in range(2):
        if args.primes[i] == 0:
            p_len = args.prime_lengths[i] if args.prime_lengths else args.prime_length[0]
            print(
                f"Generating {'1st' if i==0 else '2nd'} prime of length {p_len}", end=" ... ")
            sys.stdout.flush()  # force sys to print
            args.primes[i] = number.getPrime(p_len)
            print("Done.")

    if args.primes:
        n = math.prod(args.primes)
        print("n:")
        print(n)
        phi = (args.primes[0]-1) * (args.primes[1]-1)
        print("phi:")
        print(phi)

        d = pow(e, -1, phi)
        print("d:")
        print(d)

    if args.message and args.primes:
        c = pow(m, e, n)
        print("c:")
        print(c)


if __name__ == "__main__":
    main()
