from SchnorrTest import *
from PasswordGen import *
import random


class Person:
    def __init__(self, name):
        self.name = name
        self.generator = None
        self.prime_no = None
        self.secret_val = None
        self.paired_val = None
        self.expo_to_match = None
        self.sv_result = None
        self.pv_result = None
        self.verifier_num = generate_validation()

    def set_challenge_var(self, g, P, x, y):
        self.generator = g
        self.prime_no = P
        self.secret_val = x
        self.paired_val = y

    def set_verification_num(self, c):
        self.verifier_num = c

    def get_verification_num(self):
        return self.verifier_num

    def set_prime_number(self, P):
        self.prime_no = P

    def get_prime_number(self):
        return self.prime_no

    def set_test(self, X, Y):
        self.sv_result = X
        self.pv_result = Y

    def get_test(self):
        self.sv_result, self.pv_result = generate_test(self.prime_no, self.generator, self.secret_val, self.paired_val)
        return self.sv_result, self.pv_result

    def calc_matching_expo(self):
        self.expo_to_match = send_verify_num(self.paired_val, self.verifier_num, self.secret_val)

    def set_matching_expo(self, z):
        self.expo_to_match = z

    def get_matching_expo(self):
        return self.expo_to_match

    def get_result(self):
        return verification_test(
            self.generator,
            self.expo_to_match,
            self.prime_no,
            self.verifier_num,
            self.sv_result,
            self.pv_result
        )


# Create two people that will do the test
print("Bucky needs to send a message to Steve.")
Steve = Person('Steve')
Bucky = Person('Bucky')

# Create someone that would try to intercept messages
print("Tony wants to trick Bucky that he is Steve.\n")
Tony = Person('Tony')

# Steve wants to send a message to Bucky, first he creates a message and generates a key
print("Bucky has written down the message below:")
message = "Meet me in Ukraine before Tony gets there."
print("The original message: {}".format(message))
3
# Steve encrypts the message
key = random.randint(1, 97) % 26
print("\nBucky uses the key {} to encrypt the message.".format(str(key)))
cipher = CeaserCipher(key)
encrypted = cipher.encrypt_password(message)
print("The encrypted message is:", encrypted)

print("\nBucky sends out an alert and gets two different responses.")
print("Bucky needs a way to know that Steve is the one asking for the message.")
print("Bucky sends the public key out but not the message.\n")

print("Bucky asks the two respondents to verify themselves.")
print("Bucky and Steve beforehand talked about a way to confirm without Tony figuring it out.\n")

print("Steve prepares the Zero-Knowledge Proof test. Steve knows the generator and prime number beforehand.")
print("Tony has no idea what to do, so he just waits and hopes for information to mimic.")
Steve.set_challenge_var(3, 89, key, random.randint(1, 97))
Bucky.set_challenge_var(3, 89, None, None)  # Bucky doesn't need a key for this.
X, Y = Steve.get_test()
Bucky.set_test(X, Y)
Tony.set_test(X, Y)
print("Result X equals", str(X))
print("Result Y equals", str(Y))

print("\nSteve sends the results to Bucky, knowing Tony will probably intercept it too.")
print("Bucky sends a random number to Steve, knowing Tony will probably intercept that too.")
c = Bucky.get_verification_num()
Steve.set_verification_num(c)
Tony.set_verification_num(c)
print("Random number is", str(c))

print("\nSteve uses all the information to calculate an exponent.")
print("Steve sends that to Bucky, knowing Tony will probably intercept that too.")
Steve.calc_matching_expo()
z = Steve.get_matching_expo()
Bucky.set_matching_expo(z)
Tony.set_matching_expo(z)
print("This exponent is {}.".format(str(z)))

print("Bucky computes the result and compares it.")
outcome = Bucky.get_result()
print("The fact that Steve sent a response is {}.".format(str(outcome)))
print("\nBucky can now send the encrypted information to a specific place and know Steve is on the other side.")
print("Steve uses the key sent to decrypt the message.")

decrypted = cipher.decrypt_password(encrypted)
print("The uncovered message is:", decrypted)
