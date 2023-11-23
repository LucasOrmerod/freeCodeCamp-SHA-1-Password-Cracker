import hashlib

def hash_input(input):
  sha1 = hashlib.sha1()
  sha1.update(input.encode("utf-8"))
  return sha1.hexdigest()

def crack_sha1_hash(hash, use_salts=False):
  return_password = False
  
  # Make a list with the 10000 passwords
  unhashed_passwords = []
  with open("top-10000-passwords.txt", "r") as file:
    unhashed_passwords = [str(line).strip() for line in file.readlines()]

  # Make a list of the known salts
  known_salts = []
  with open("known-salts.txt", "r") as file:
    known_salts = [str(line).strip() for line in file.readlines()]

  if use_salts:
    # If salts should be used, loop through the salts and try all of the passwords
    for salt in known_salts:
      for password in unhashed_passwords:
        if hash_input(salt + password) == hash or hash_input(password + salt) == hash:
          return_password = password
  else:
    # If salts should not be used
    for password in unhashed_passwords:
      if hash_input(password) == hash:
        return_password = password

  if return_password is False:
    return "PASSWORD NOT IN DATABASE"
  else:
    return return_password
