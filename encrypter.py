def encrypt(password, byte_input):
    j = 0
    res = bytearray()
    for idx,i in enumerate(byte_input):
        res.append((i ^ ord(password[idx%len(password)])))
    return res
