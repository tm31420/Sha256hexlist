from hashlib import sha256
ra = open('sha256ofaddrs.txt', 'w')


def convert(aa):
    hash = sha256(bytes.fromhex(aa))
    hx = hash.hexdigest()
    ra.write("%s \n" % hx)    
    print(aa)
    
with open("btc_h160.txt") as file:
    for line in file:

        ss = str.strip(line)
        print("__________________________________________________\n")
        print("Converting string: " + ss)
        
        convert(ss)

