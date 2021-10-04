# rsa-keygen

![Style Check](https://github.com/alanyee/rsa-keygen/actions/workflows/linter.yml/badge.svg)

Generate textbook integer-type RSA schema for fun/[CTF](https://ctftime.org/)s. Tested for primes numbers up to 300 digits.

## usage

```text
usage: rsa-keygen [-h] [-m MESSAGE] [-l prime_length] [-ls prime_lengths prime_lengths] [-p prime prime] [-e exponent]

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
                        Load from two big prime numbers. Takes precedence over prime_length and prime_lengths.
  -e exponent, --exponent exponent
                        Load from exponent
 ```

## Examples

For all the examples, the message to be encrypted and decrypted is provided by passing the `-m` or the `--message` flag.

- To generate the keys by specifying the two prime numbers to be used, pass the `-p` or the `--primes` flag:

    ```console
    $ rsa-keygen -m "The message goes here" -p 17 13
    m:
    123362127776045355325184496631186371083667333542501
    n:
    221
    phi:
    192
    d:
    65
    c:
    21
    ```

    This example uses the two prime numbers 17 and 13 to generate the keys.

    The order in  which the arguments are passed don't matter. The command below will work just like the above example.  
        `$ rsa-keygen -p 17 13 -m "The message goes here"`

- To generate the keys by specifying the lengths(the size in bytes) of two prime numbers to be used, pass the `-ls` or the `--prime-lengths` flag.

    ```console
    $ rsa-keygen -m "The message goes here" -ls 32 64 
    m:
    123362127776045355325184496631186371083667333542501
    Generating 1st prime of length 32 ... Done.
    Generating 2nd prime of length 64 ... Done.
    n:
    47556891592590489208054307657
    phi:
    47556891576510580051989125316
    d:
    17786395004834686171999106621
    c:
    21952363551535066551250980471
    ```

    This example uses one prime number having the size of 32 bytes while the other prime number having the size of 64 bytes.

- If length of the two prime numbers being used is the same, we can pass the `-l` or the `--prime-length` flag.

    ```console
    $ rsa-keygen -m "The message goes here" -l 256 
    m:
    123362127776045355325184496631186371083667333542501
    Generating 1st prime of length 256 ... Done.
    Generating 2nd prime of length 256 ... Done.
    n:
    5582826894363286377472569981239943370180566271496343561506135521040753567699648883542943641090961494366588907876500582592466309738990834922788665356802131
    phi:
    5582826894363286377472569981239943370180566271496343561506135521040753567699497243467916597156172216800437440457198218821636002629632191399098338937620872
    d:
    1307603229145008863606877782199873822913341963584980601326261199749386869465909069491013011983265079693710647588659728991441668681277051710883310232273073
    c:
    1957840327725554014766627662755023947129607290378923521502432676947466991128225062897106936657555488818065445667019180444456599814566964260723515825205380
    ```

- If the key is to be generated from a specified exponent, pass the `-e` or the `--exponent` flag:

    ```console
    $ rsa-keygen -m "The message goes here" -l 32 -e 65537
    m:
    123362127776045355325184496631186371083667333542501
    Generating 1st prime of length 32 ... Done.
    Generating 2nd prime of length 32 ... Done.
    n:
    12962843795152722343
    phi:
    12962843787936417760
    d:
    10493184396506017953
    c:
    6233734676688870585
    ```
