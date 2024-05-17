# Welcome

This set of files is for meeting the requirements laid out for the advanced homework project. This project accomplishes
three things.

1) This project modifies existing code that originally was able to print out a blockchain with a random hash. The
modified program adds on to be able to dynamically read from a list of product information and create product IDs for
each of them, storing the results in the same blockchain format.

2) This project is able to generate QR codes from the blockchain information, which when scanned give the common name
of the product and its hash, securely created and salted for added unbreakability. The project can also generate 
imposter QR codes that could be used to try to mimic the data on there and mix the correct QR codes in to the pile.

3) This project can read all QR codes generated, and using the information stored in the blockchain correctly identify
which QR codes are valid.

# Important Files

* Main.py
  * This file contains all the logic used in the program. It consists of one class and three additional functions.
  * The "Block" class is used to represent the attributes of a block in a blockchain. 
    * It records the location in the 
      blockchain, the time of creation, the core data stored within the block (such as a transaction), the hash of the
      block that comes before it, and the current hash generated from all the core information.
    * This class was modified to also hold the information taken in from a list of products, and a randomly generated
      salt that further strengthens the hash.
    * This class can return its information in a json-formatted string, generate information needed for a qr code,
      generate a 64-character hash output, and generate a salt.
  * The "make_genesis_block" function is used to create the block that starts the blockchain.
  * The "next_block" function is used to append a new block to a blockchain.
  * The "generate_product_id" function is used to create a GTIN-12 Apple Serial Number for the products.
* Products.json
  * This file contains the products that will be read into the program in the format of a JSON file. 
  * Product info revolves around Apple products and are retried from the Apple website.

# Requirements to Run

* Libraries used (some come with Python and do not need to be installed. Look at installation-specific requirements to
  know what to install):
  * datetime
  * hashlib
  * json
  * qrcode
  * cv2
  * pandas
  * random
  * os
  * pathlib
  * ast
* Installation-specific requirements (you may not have to install pypng)
  * Python 3.11
  * python-dateutil 2.8.2
  * opencv-python 4.8.1.78
  * pandas 2.1.4
  * qrcode 7.4.2
  * pypng 0.20220715.0

# Steps to run

1) Ensure Products.json is in the same folder as the python program, and formatted correctly.
2) Run Main.py

# Results

The output should be as follows.

1) The json file is ingested as a Pandas Dataframe. The Dataframe is printed below.
2) The apple blockchain is initialized and populated by iterating through the Dataframe.
3) The verification information and product data in the blockchain are extracted into lists. Product data is saved into
   a new file called 'Product Info.txt'
4) Fake QR Code information is randomly generated and added to the list of verification information.
5) The verification information list is shuffled to lose track of which sets of information are valid.
6) The reason for this becomes clear when creating QR codes. Multiple versions of QR codes are created, meaning there
   are numbers appended to some names. This ensures we can't figure out which is which based on the number.
7) Retrieve all QR Code filepaths and look at each one by one
   1) Retrieve JSON string from QR code.
   2) Transform JSON string into verification dictionary.
   3) Scan through blocks to identify which block the hash matches. Save this information in a new results list.
8) Results list is saved in a new file called 'Results.txt'.

Thus, two new files should be created, 'Product Info' and 'Results' respectively. If the "Secure" folder didn't exist
before, it should be created and populated with QR codes. Used the newly generated files to help manually review if
the code correctly identified the valid QR codes for the product and returned the product ID.

Lastly, A QR code folder called 'Actual' is created that reflects the data show in 'Product Info.txt.' Ideally, this
data would scan to fit the resulting file exactly.

All QR codes will be color coded, so you will be able to visually kind of see which codes are the right ones as well.

One more thing - if you forget to clear your Secure folder before running, do not worry. This program will not break 
scanning a few old QR codes. Think of it like testing if the analysis will still recognize depreciated versions of 
things!

