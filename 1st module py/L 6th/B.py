import re
def prep_ip(ip_address):
    ip_address = ip_address.split('.')
    match = [str(int(x)) for x in ip_address]

    return match[0]+'.'+match[1]+'.'+match[2]+'.'+match[3]

print(prep_ip("216.008.0904.196"))

