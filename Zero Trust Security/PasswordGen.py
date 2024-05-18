from random import randint, choice

"""

Password Generator Rules

1) A password must have at least ten characters.
2) A password consists of only letters and digits.
3) A password must contain at least two digits.


"""


def check_password(passwd):
    is_good = True

    # Rule 1
    if len(passwd) < 10:
        is_good = False
        print("Password must be ten characters or longer.")

    # Rule 2 & 3
    num_digits = 0

    for c in passwd:
        if ord('a') <= ord(c) <= ord('z'):
            pass
        elif ord('A') <= ord(c) <= ord('Z'):
            pass
        elif ord('0') <= ord(c) <= ord('9'):
            num_digits += 1
        else:
            is_good = False
            print("Password must contain only letters and digits.")

    if num_digits < 2:
        is_good = False
        print("Password must contain two or more numbers.")

    return is_good


def generate_password():
    new_pass = ''

    # Length of password
    length = randint(1, 20)

    # The letters
    key_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    key_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    key_num = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    key_invalid = ['.']
    keys = key_lower + key_upper + key_num + key_invalid

    # For i in range
    for i in range(length):
        key = choice(keys)
        if key == '.':
            new_pass = new_pass + chr(randint(0, 382))
        else:
            new_pass = new_pass + key

    return new_pass


class CeaserCipher:
    def __init__(self, shift_number):
        self.shift_number = shift_number
        self.plaintext = ''
        self.ciphertext = ''

    # Increment/Decrement function
    def old_n_crement(self, ascii_code, sn, lower_bound, upper_bound):
        change = ascii_code + sn

        if change < lower_bound:  # Check if it's less than the lower bound
            diff = lower_bound - change
            new_ascii = upper_bound - diff
            return new_ascii
        elif change > upper_bound:  # Check if it's more than the upper bound
            diff = change - upper_bound
            new_ascii = lower_bound + diff
            return new_ascii
        else:
            return change

    def n_crement(self, ascii_code, sn, lower_bound, upper_bound):
        placement = (ascii_code - lower_bound)
        range = (upper_bound - lower_bound) + 1
        change = (placement + sn) % range
        final = lower_bound + change
        return final

    # Shifting a single number
    def ceaser_shift(self, ascii_code, decrypt=False):
        # Check decrypt status
        if decrypt:
            sn = self.shift_number * -1
        else:
            sn = self.shift_number

        # Check if upper, lowercase, or digit
        if ord('a') <= ascii_code <= ord('z'):
            new_ascii = self.n_crement(ascii_code, sn, ord('a'), ord('z'))
        elif ord('A') <= ascii_code <= ord('Z'):
            new_ascii = self.n_crement(ascii_code, sn, ord('A'), ord('Z'))
        elif ord('0') <= ascii_code <= ord('9'):
            sn = abs(sn) % 10
            if decrypt:
                sn = sn * -1

            new_ascii = self.n_crement(ascii_code, sn, ord('0'), ord('9'))
        else:
            new_ascii = ascii_code

        return chr(new_ascii)

    def encrypt_password(self, plaintext):
        # prepare ciphertext
        self.ciphertext = ''
        self.plaintext = plaintext

        # Go through doing the shift
        for i in range(len(plaintext)):
            self.ciphertext = self.ciphertext + self.ceaser_shift(ord(self.plaintext[i]))

        return self.ciphertext

    def decrypt_password(self, ciphertext):
        # prepare plaintext
        self.plaintext = ''
        self.ciphertext = ciphertext

        # Go through doing the shift
        for i in range(len(ciphertext)):
            self.plaintext = self.plaintext + self.ceaser_shift(ord(self.ciphertext[i]), decrypt=True)

        return self.plaintext


def try_ceaser(password):
    print("------------------")
    print("Password entered: {}\n".format(password))

    if check_password(password):
        # Create a Ceaser Shift object that moves letters five places over
        number = 5
        shifter = CeaserCipher(number)

        print("Original Password: {}".format(password))

        code = shifter.encrypt_password(password)
        print("Encrypted Password: {}".format(code))

        decrypted_code = shifter.decrypt_password(code)
        print("Decrypted Code: {}".format(decrypted_code))
    else:
        print("Password is invalid.")


if __name__ == '__main__':
    for i in range(10):
        try_ceaser(generate_password())
