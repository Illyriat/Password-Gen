MIN_PW=8

import hashlib

def ValidateStrongPassword(password):

    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    noRpt = True

    rng = True

    pwLen = len(password)
    if pwLen >= MIN_PW:
        cnt = True

    for eachChar in password:
        if eachChar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp = True
        elif eachChar in "abcdefghijklmnopqrstuvwxyz":
            low = True
        elif eachChar in "0123456789":
            num = True
        elif eachChar in "!@#£$%^&*()_-=+/\';><,.>":
            spc = True
        else:
            continue
    
    pos = 0
    for eachChar in password:
        if pos < pwLen-2:
            if eachChar == password[pos+1] and eachChar == password[pos+2]:
                noRpt = False
            else:
                pos += 1
    
    for eachChar in password:
        val = ord(eachChar)
        if val < 0x20 or val > 0x7f:
            rng = False
    
    if upp and low and num and spc and cnt and rng and noRpt:
        return True
    else:
        return False
    

def gen_pass_hash(password, salt):
    try:
        import binascii
        dk = hash_obj = hashlib.pbkdf2_hmac('sha512', password.encode(), salt.encode(), 1000000)
        return True, binascii.hexlify(dk)
    except:
        return False, "Hashing Failure"
    

if __name__ == '__main__':

    thePass = input("Enter Password: ")
    salt = "@##4$0808098ljalfj"
    if ValidateStrongPassword(thePass):
        print(thePass, " Meets the Criteria")
        result, resultingHash = gen_pass_hash(thePass, salt)
        if result:
            print("Hash: ", resultingHash)
        else:
            print(resultingHash)
    else:
        print(thePass, " Does not Meet the Criteria")