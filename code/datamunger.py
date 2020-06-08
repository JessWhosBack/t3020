import urllib
import urllib.request
import ssl
import sys


#e.g. run as
# python3 datamunger.py https://raw.githubusercontent.com/shaze/t3020/master/data.csv
# fetches the data from the repo
# or
# python3 datamunger.py see.csv
# gets data from same directory

origin=sys.argv[1]

def calc_total(curr):
    computed=0
    for c in curr[1:9]: #E1 Corrected the range
        computed=computed+c
    return computed


def check_monotonic(prev,curr):
   # Now check monotonicity and update  prev so next time round we compare
   # against this row
    for i in range(8): #CHANGE: Range changed since T8 does not need to be monotonic
        if curr[i] <  prev[i]:  #E2 removed "=" since entries can be equal
            print("Monotonic error at column %d comparing lines %d and %d  "%(i,n-1,n),
                     "values %d and %d"%(curr[i],prev[i]))
        prev[i]=curr[i]  


def check_row(n, prev, curr_str):
    curr = []
    for c in range(9): #E3 only need to check for values in TALL and T1-T8 columns (not the OTHER column)
        try:
            v = int(curr_str[c])
            curr.append(v)
        except ValueError:  # missing data so can't convert
            return False
    computed = calc_total(curr)
    if computed != curr[0]:
        print("Sum error at line ",n, curr_str,
              "computed %d and expected %d"%(computed, curr[0]))
    check_monotonic(prev, curr)
    return True # if there all data was there




if "http" in origin:
   ctx = ssl._create_unverified_context()
   inp = urllib.request.urlopen(origin, context=ctx)
   def get_text(x):  # for URL we need to convert from byte to string
       return x.decode('utf-8')
else:
    inp = open(origin)
    def get_text(x): # does nothing in case of local files
        return x
inp.readline() # skip the header
prev = [0,0,0,0,0,0,0,0] #CHANGE: only need 8 entries since only columns TALL and T1-T7 need to increase monotonically
missing=0
n=1
for  line in inp:
     n=n+1
     str_vals  = get_text(line).strip().split(",")
     ok = check_row(n,prev,str_vals)
     if not ok:
         missing = missing+1
print("There were ",missing," missing lines")
