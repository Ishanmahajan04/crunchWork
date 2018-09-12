import time, os

#Set the filename and open the file
filename = 'fake.log'
file = open(filename,'r')

logfile='access.log'

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

def write_log(text, file):
    f = open(file, 'a')           # 'a' will append to an existing file if it exists
    f.write("{}".format(text))  # write the text to the logfile and move to next line
    return 

while True:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        write_log(line,logfile)
        print line
		