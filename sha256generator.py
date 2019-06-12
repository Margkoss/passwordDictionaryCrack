import hashlib
import os
WARNING_ORANGE = '\033[93m'

to_hash = input("Give word to hash: ")
hashed = hashlib.sha256(to_hash.strip().encode('utf-8')).hexdigest()
os.system("echo %s | xclip -sel clip" % (hashed))
print("\n%sAlready copied to clipboard\n%s" % (WARNING_ORANGE, hashed))
