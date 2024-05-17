"""

Resources:
https://github.com/RaptorMai/Step-by-step-tutorial-of-building-a-small-blockchain-in-Python/tree/master
https://www.youtube.com/watch?v=l4ugfcj7qrI&ab_channel=NeuralNine
https://www.gs1.org/services/how-calculate-check-digit-manually
https://thepythoncode.com/article/generate-read-qr-code-python
https://mehmandarov.com/generating-qr-codes-with-secure-hashes-using-java/
https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/

"""
from ValidColors import retrive_valid_colors
from datetime import datetime
import hashlib as hasher
import json
import qrcode
import segno
import cv2
import pandas as pd
import random
import os
import pathlib
import ast


colors = retrive_valid_colors()
# The block object
class Block:
    # Creation of the initial state of the block object
    def __init__(self, index, timestamp, data, previous_hash, product_data=None):
        if product_data is None:
            product_data = {}

        self.index = index  # Place in blockchain
        self.timestamp = timestamp  # Time of the created block
        self.data = data  # data recorded in block
        self.previous_hash = previous_hash  # The last hash before the block
        self.salt = self.generate_salt()  # Creating a random salt object that stays object side
        self.hash = self.hash_block(salt=self.salt)  # The hash of the block itself
        self.color = self.generate_color()
        self.product_data = product_data  # Data retrieved from json file

    # This function is used to print the block's index
    def show_block(self):
        if self.index != 0:
            prod_data = self.product_data.to_json()
        else:
            prod_data = ''

        return json.dumps({
            'index': self.index,
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),  # Properly sends out a time
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'color': self.color,
            'Product Data': prod_data
        })

    def generate_qr_info(self):
        if self.index != 0:
            # QR code for Name Authentication JSON
            verification = {
                'name': self.product_data["Common_Name"],
                'hash': self.hash,
                'color': self.color
            }

            return verification
        else:
            return None

    # This function generates an SHA-256 hash of the information in string form.
    def hash_block(self, salt=''):
        sha = hasher.sha256()
        seq = [str(self.index), str(self.timestamp), str(self.data), str(self.previous_hash), salt]
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

    def generate_salt(self):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        SALT_LENGTH = 11
        salt_chars = [random.choice(ALPHABET) for i in range(SALT_LENGTH)]
        salt = "".join(salt_chars)

        return salt

    def generate_color(self):
        c = random.choice(colors)
        return c


# This function creates a new block based on the block before it
def next_block(pre_block, product_data=None, data=None):
    """Return next block in a blockchain."""
    idx = pre_block.index + 1

    if data is None:
        data = 'This is block {}'.format(idx)

    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data=data,
                  previous_hash=pre_block.hash,
                  product_data=product_data)

    return block


# This function creates the very first block in the blockchain.
def make_genesis_block():
    """Make the first block in a blockchain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block


def generate_product_id():
    # Apple's Prefix for GTIN-12
    prefix = '0195949'

    # Creating an item number
    item_number = str(random.randint(0, 9999))
    while len(item_number) < 4:
        item_number = '0' + item_number

    # Joining prefix and item id together
    product_id = prefix + item_number

    # Getting a check sum
    sum = 0
    for index in range(len(product_id)):
        num = int(product_id[index])
        if num % 2 == 0:  # Odd index (counting numbers, not integers)
            sum += num * 3
        elif num % 2 == 1:  # Even index (counting numbers, not integers)
            sum += num * 1

    # Finalize check digit
    check_digit = str(10 - (sum % 10))

    # Final 12-digit product id
    product_id = product_id + check_digit

    return product_id


# Import products
products = pd.read_json('Products.json')
print(products)
print()

# Create Apple blockchain
appleBC = [make_genesis_block()]
appleBC[0].data = "Apple Genesis Block"

# Populate Apple blockchain
for rowNum in range(products.shape[0]):
    product_id = generate_product_id()
    product_data = products.iloc[rowNum, :]
    block = next_block(appleBC[rowNum], product_data=product_data, data=product_id)
    appleBC.append(block)

# list of verification codes
verification_list = []
information_output = []

# Create QR codes
for block in appleBC:
    verification_list.append(block.generate_qr_info())
    information_output.append(block.show_block())

# Create Secure folder if needed.
if not os.path.exists('Actual'):
    os.mkdir('Actual')

# Write the results to a file to be able to manually confirm later
with open('Product Info.txt', 'w') as file:
    for line in information_output:
        # Generate Structured Output
        fl = ''
        formatted_line = ast.literal_eval(line)
        output_color = formatted_line['color']
        for key, value in formatted_line.items():
            fl = fl + f'{key}: {value}\n'

        file.write(f'{fl}\n')

        # Output as an additional set of QR codes
        if formatted_line['index'] != 0:
            product = ast.literal_eval(formatted_line['Product Data'])
            title = product['Common_Name']

            img = segno.make_qr(fl)
            img.save(f'Actual/{title}.png', dark=output_color, scale=10)
            # img = qrcode.make(fl)
            # img.save(f'Actual/{title}.png')

# Create Fake QR information
product_names = products['Common_Name']
num_fakes = 30
for i in range(num_fakes):
    # Get a random name
    name = product_names.sample(n=1, random_state=random.randint(1, 1000))
    name = name.values[0]

    sha = hasher.sha256()
    sha.update(''.join([name, generate_product_id()]).encode('utf-8'))

    # QR code for Name Authentication JSON
    verification = {
        'name': name,
        'hash': sha.hexdigest(),
        'color': random.choice(colors)
    }

    verification_list.append(verification)

# Randomize the list to make it unknown to analyze
v_list_shuffled = sorted(verification_list, key=lambda x: random.random())

print(verification_list)
print(v_list_shuffled)

# Create Secure folder if needed.
if not os.path.exists('Secure'):
    os.mkdir('Secure')

# Create the qr codes
for v in v_list_shuffled:
    if v is None:
        continue
    print(v)

    # File path
    filepath = f'Secure/QR Code for {v["name"]}'
    fp = f'{filepath}.png'
    i = 0

    # Account for duplicates
    while os.path.exists(fp):
        i += 1
        fp = f'{filepath}_{i}.png'

    # Extract color and actual info
    v_color = v['color']
    extracted_v = {
        'name': v['name'],
        'hash': v['hash'],
    }

    img = segno.make_qr(json.dumps(extracted_v))
    img.save(fp, dark=v_color, scale=10)
    # img = qrcode.make(json.dumps(extracted_v), color=v_color)
    # img.save(fp)

# Retrieve all paths
directory = 'Secure'
images = pathlib.Path(directory).glob('*')

# Keeping track of correct files
correct_files = []

# Checking QR codes
detector = cv2.QRCodeDetector()
for image in images:
    read_qr = cv2.imread(str(image))
    data, bbox, straight_qrcode = detector.detectAndDecode(read_qr)

    if bbox is not None:
        qr_data = ast.literal_eval(data)
        qr_name = qr_data['name']
        qr_hash = qr_data['hash']

        for block in appleBC:
            if block.index == 0:  # Skip Genesis Block
                continue
            if block.product_data["Common_Name"] != qr_name:  # Skip Blocks that aren't pretending to be real
                continue

            if block.hash == qr_hash:
                # Print which file is right
                info = f'{str(image)} is a valid QR Code file.'
                correct_files.append(info)
                print(info)

                # Print the Product ID
                print(f'Product ID: {block.data}')

# Save results as well for manual confirmation
with open('Results.txt', 'w') as file:
    for line in correct_files:
        file.write(f'{line}\n')
