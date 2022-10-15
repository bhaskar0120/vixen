def encrypt(password, FILE):
    file = bytearray(open(FILE,'rb').read())
    size=len(file)
    xored=bytearray(size)
    password_bytes=bytes(password,'utf-8')
    pw=bytearray(password_bytes)
    sz=len(pw)
    for i in range (size):
        xored[i] = file[i]^pw[i%sz]
    open(FILE,'wb').write(xored)
