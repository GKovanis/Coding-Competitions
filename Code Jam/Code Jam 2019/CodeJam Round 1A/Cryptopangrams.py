#import sympy
#from math import floor

#Find primes using the Sieve of Eratosthenes
#def all_primes(start, end):
#    return list(sympy.sieve.primerange(start, end))

def all_primes(lower_limit,upper_limit):
    candidate = lower_limit
    r = []
    while(candidate <= upper_limit):
        trial_divisor = 2
        prime = 1 # assume it's prime
        while(trial_divisor**2 <= candidate and prime):
            if(candidate%trial_divisor == 0):
                prime = 0 # it isn't prime
            trial_divisor+=1
        if(prime):
            r += [candidate]
        candidate += 2
    return r


#Read input
t = int(input())
primes = []
for i in range(1, t + 1):
    cypher_primes = []
    n, l = [int(s) for s in input().split(" ")]
    cyphertext = input().split(" ")
    cyphertext = [int(x) for x in cyphertext]
    #Get all the prime numbers up to n
    primes = all_primes(3,int(floor(cyphertext[0]/2)))
    #find which primes divide the first semiprime
    for prime in primes:
        if cyphertext[0] % prime == 0:
            x = prime
            y = int(cyphertext[0]/x)
            #Find which of the 2 primes found, divides the second semiprime
            if cyphertext[1] % x == 0:
                next_prime = int(cyphertext[1]/x)
                cypher_primes.append(y)
                cypher_primes.append(x)
            else:
                next_prime = int(cyphertext[1]/y)
                cypher_primes.append(x)
                cypher_primes.append(y)
            cypher_primes.append(next_prime)
            break

    #find all the rest of the primes
    for j in range(2,len(cyphertext)):
        next_prime = int(cyphertext[j]/next_prime)
        cypher_primes.append(next_prime)

    #sort the primes
    cyphered_text = cypher_primes
    cypher_primes = sorted(list(set(cypher_primes)))

    #Match letters with prime numbers
    decyphered_text = []
    for j in range(len(cyphered_text)):
        decyphered_text.append(chr(65 + cypher_primes.index(cyphered_text[j])))
    decyphered_text = ''.join(decyphered_text)

    #Print solution
    print("Case #{}: {}".format(i,decyphered_text))
