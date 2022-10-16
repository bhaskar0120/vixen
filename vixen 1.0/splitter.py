import os

OUT_PREFIX = "chunk_part_"

def get_filename(prefix, idx):
    return prefix + str(idx)

def split(FILE):
    bytes_per_file=307200
    # 25MB = 26214400bytes
    # 300KB = 307200bytes
    idx=0
    in_fil=p=open(FILE,"rb")
    out_filename = get_filename(OUT_PREFIX,idx)
    out_fil=open(out_filename,"wb")

    byte_count=file_count=cnt=0
    c=in_fil.read(1)
    file_stat=os.stat(FILE)
    tot_size=file_stat.st_size

    while c!='' and cnt<=tot_size:
        byte_count+=1
        out_fil.write(c)
        cnt+=1
        if byte_count>=bytes_per_file:
            byte_count=0
            file_count+=1
            out_fil.close()
            idx+=1
            out_filename = get_filename(OUT_PREFIX,idx)
            out_fil=open(out_filename,"wb")
        c=in_fil.read(1)
    in_fil.close()
    if not out_fil.close:
        out_fil.close()
    if byte_count == 0:
        os.remove(out_filename)
