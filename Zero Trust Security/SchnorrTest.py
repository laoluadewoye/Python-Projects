import random


def zero_proof_example(P=89, g=3):
    PRIMENO = P
    generator = g

    secretVal = random.randint(1, 97)

    X = pow(generator, secretVal) % PRIMENO
    y = random.randint(1, 97)
    Y = pow(generator, y) % PRIMENO

    print("Sanchita (the Prover) generates these values:")
    print("secretVal(secret)= ", secretVal)
    print("PRIMENO= ", PRIMENO)
    print("X= ", X)

    print("\nSanchita generates a random value (y):")
    print("y=", y)

    print("\nSanchita computes Y = generator^y (mod PRIMENO) and passes to Sachin:")

    print("Y=", Y)

    print("\nSachin generates a random value (c) and passes to Sanchita:")

    c = random.randint(1, 97)

    print("c=", c)
    print("\nSanchita calculates z = y.secretVal^c (mod PRIMENO) and send to Sachin (the Verifier):")

    z = (y + c * secretVal)

    print("z=", z)

    print("\nSachin now computes val=generator^z (mod PRIMENO) and (Y X^c (mod PRIMENO)) and",
          "determines if they are the same primeNo")

    val1 = pow(generator, z) % PRIMENO
    val2 = (Y * (X ** c)) % PRIMENO

    print("val1= ", val1, end=' ')
    print(" val2= ", val2)

    if val1 == val2:
        print("Sanchita has proven that she knows x")
    else:
        print("Failure to prove")


def generate_test(P, g, x, y):
    prime_no = P
    generator = g

    secret_val = x
    sv_result = pow(generator, secret_val) % prime_no

    paired_val = y
    pv_result = pow(generator, paired_val) % prime_no

    return sv_result, pv_result


def generate_validation():
    verifier_num = random.randint(1, 97)
    return verifier_num


def send_verify_num(y, c, x):
    paired_val = y
    verifier_num = c
    secret_val = x
    expo_to_match = (paired_val + verifier_num * secret_val)

    return expo_to_match


def verification_test(g, z, P, c, X, Y):
    generator = g
    expo_to_match = z
    prime_no = P
    verifier_num = c
    sv_result = X
    pv_result = Y

    val1 = pow(generator, expo_to_match) % prime_no
    val2 = (pv_result * (sv_result ** verifier_num)) % prime_no

    print("val1= ", val1, end=' ')
    print(" val2= ", val2)

    if val1 == val2:
        return True
    else:
        return False


if __name__ == '__main__':
    zero_proof_example()
