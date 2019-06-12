import hashlib
import time

WARNING_ORANGE = '\033[93m'

counter = 1

# Get the hashed password we're trying to find
sha256_pass = input("Please give a sha256 hash: \n\n").lower()
sha256_file = "./passwords.txt"

# try except for file
try:
    sha256_file = open(sha256_file,'r')
except:
    print("\nFile not there \n Exiting...")
    exit()

# Start time
start = time.time()

# Loop through the file and try to match hashes
for password in sha256_file:
    print("%d : %s" % (counter,password.strip()))
    hash_object = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
    counter += 1
    
    if hash_object == sha256_pass:
        end = time.time()
        print("\n\n%sPassword was --->%s<--- and was found in %f" % (WARNING_ORANGE, password.strip(), end-start))
        break
else:
    print("no password found")