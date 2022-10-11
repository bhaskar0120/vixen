from sys import argv

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

        with open(FILE, 'b') as f:



    elif MODE == '-d':
        pass 
    else:
        print(USAGE)
        exit(1)

if __name__ == "__main__":
    main()
