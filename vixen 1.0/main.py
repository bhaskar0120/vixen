from sys import argv
from combiner import combine
from encrypter import encrypt
from splitter import split

def main():
    USAGE = 'Bad arguments \nUsage: \nFor encryption: vixen.py -e [FILE NAME] \nFor decryption: vixen.py -d [FILE NAME]'
    if len(argv) < 3:
        print(USAGE)
        exit(1)

    MODE = argv[1]

    if MODE == '-e':
        FILE = argv[2]
        print("Please set the password for the file")
        pw = input('Password: ')
        encrypt(pw,FILE)
        split(FILE)

    elif MODE == '-d':
        FILE = argv[2]
        print("Please input the password for the file")
        pw = input('Password: ')
        combine(FILE)
        encrypt(pw,FILE)
    
    elif MODE == '-r':
        FILE=argv[2]
        print("Please input the password for the file")
        pw = input('Password: ')
        encrypt(pw,FILE)
    else:
        print(USAGE)
        exit(1)

if __name__ == "__main__":
    main()
