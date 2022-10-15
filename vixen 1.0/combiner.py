import os
def combine(FILE):
    # no,FILENAME,
    namesofiles=[]
    for root,dirs,files in os.walk("C:/Users/Himanshu Srivastava/OneDrive/Desktop/ML/vixen",topdown=True):
        for name in files:
            if(name.startswith('chunk_part_')):
                namesofiles.append(name)
    # for i in range(0,no):
    #     namesofiles.append(FILENAME+str(i))
    with open(FILE,"wb") as new_file:
        for name in namesofiles:
            with open(name,"rb") as file:
                for line in file:
                    new_file.write(line)
                new_file.write(b'\n')
