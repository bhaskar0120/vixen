password = "dugdeep madarchod"

def encrypt(password, inputstr):
    j = 0
    res = ""
    for i in range(len(inputstr)):
        res += chr(ord(inputstr[i]) ^ ord(password[j%(len(password))]))
        j+=1
    return res


res = (encrypt(password, input()))
print(res)
print(encrypt(password, res))