import fileinput
import re
from time import strptime

f_names = ['access.log'] # names of log files
lines = list(fileinput.input(f_names))
t_fmt = '%a %b %d %H:%M:%S %Y' # format of time stamps
t_pat = re.compile(r'\[(.+?)\]') # pattern to extract timestamp


for l in sorted(lines, key=lambda l: strptime(t_pat.search(l).group(1), t_fmt)):
    if not l.isspace():
    	print l,