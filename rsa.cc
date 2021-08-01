#include <iostream>
#include <gmp.h>

// g++ rsa.cc -lgmpxx -lgmp -o rsa

int main (int argc, char **argv) {
  mpz_t n, p, q, e, d, phi;

  mpz_init(n);
  mpz_init(d);
  mpz_init_set_str(e, "65537", 10);

  // user input two large primes
  mpz_init_set_str(p, argv[1], 10);
  mpz_init_set_str(q, argv[2], 10);

  // Find n-bit
  mpz_mul(n,p,q);
  std::cout << "n:" << std::endl;
  gmp_printf ("%Zd\n", n);

  // calculate phi(n)
  mpz_sub_ui(p, p, 1UL);
  mpz_sub_ui(q, q, 1UL);
  mpz_mul(phi, p, q);
  std::cout << "phi:" << std::endl;
  gmp_printf ("%Zd\n", phi);

  // private key d
  mpz_invert(d, e, phi);
  std::cout << "d:" << std::endl;
  gmp_printf ("%Zd\n", d);
  return 0;
}
