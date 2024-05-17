import re
from random import randint


def get_working_ip(addr_string, mtd_status=False):
    # Parse address
    if '.' in addr_string:
        ip_addr = addr_string.split('.')
    elif '-' in addr_string:
        ip_addr = addr_string.split('-')
    elif ':' in addr_string:
        ip_addr = addr_string.split(':')
    elif ',' in addr_string:
        ip_addr = addr_string.split(',')
    else:
        ip_addr = addr_string.split('_')

    ip_addr = [int(num) for num in ip_addr]

    if mtd_status:
        l_bound = 0
        u_bound = 200
        # Create a virtual address
        if ip_addr[0] < 128:  # Class A
            ip_addr = [ip_addr[0], randint(l_bound, u_bound), randint(l_bound, u_bound), randint(l_bound, u_bound)]
        elif ip_addr[0] < 192:  # Class B
            ip_addr = [ip_addr[0], ip_addr[1], randint(l_bound, u_bound), randint(l_bound, u_bound)]
        else:
            ip_addr = [ip_addr[0], ip_addr[1], ip_addr[2], randint(l_bound, u_bound)]

    return ip_addr


def get_ip_class(ip_addr):
    if ip_addr[0] >= 240:
        ip_class = 'E'
    elif ip_addr[0] >= 224:
        ip_class = 'D'
    elif ip_addr[0] >= 192:
        ip_class = 'C'
    elif ip_addr[0] >= 128:
        ip_class = 'B'
    else:
        ip_class = 'A'

    return ip_class


def generate_ip_address(addr):
    # Verify format
    ip_format = re.compile('[0-9]{1,3}[-.:,_][0-9]{1,3}[-.:,_][0-9]{1,3}[-.:,_][0-9]{1,3}')
    match = ip_format.match(addr)
    if match is None:
        exit()

    # Parse address
    if '.' in addr:
        ip_addr = addr.split('.')
    elif '-' in addr:
        ip_addr = addr.split('-')
    elif ':' in addr:
        ip_addr = addr.split(':')
    elif ',' in addr:
        ip_addr = addr.split(',')
    else:
        ip_addr = addr.split('_')

    print(ip_addr)
    ip_addr = [int(num) for num in ip_addr]
    print(ip_addr)

    # Validate address
    ip_check = [0 <= num <= 255 for num in ip_addr]
    if False in ip_check:
        print("Number check failed")
        exit()

    # Analyze grouping
    if ip_addr[0] >= 240:
        ip_class = 'E'
    elif ip_addr[0] >= 224:
        ip_class = 'D'
    elif ip_addr[0] >= 192:
        ip_class = 'C'
    elif ip_addr[0] >= 128:
        ip_class = 'B'
    else:
        ip_class = 'A'

    print(ip_class)

    # Create a virtual address
    if ip_class == 'A':
        new_address = [ip_addr[0], randint(0, 255), randint(0, 255), randint(0, 255)]
    if ip_class == 'B':
        new_address = [ip_addr[0], ip_addr[1], randint(0, 255), randint(0, 255)]
    else:
        new_address = [ip_addr[0], ip_addr[1], ip_addr[2], randint(0, 255)]

    print("Virtual Address:", new_address)
