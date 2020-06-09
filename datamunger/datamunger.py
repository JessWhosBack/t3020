#Jesse van der Merwe
#1829172
#9 June
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

origin = ""

def calc_total(curr):
    computed=0
    for c in curr[1:9]: #CHANGE: E1 Corrected the range
        computed=computed+c
    return computed


def check_monotonic(prev,curr, n, warning_mono):
   # Now check monotonicity and update  prev so next time round we compare
   # against this row
    for i in range(8): #CHANGE: Range changed since T8 does not need to be monotonic
        if curr[i] <  prev[i]:  #CHANGE: E2 removed "=" since entries can be equal
            message = ("Monotonic error at column " + str(i) + " comparing lines " + str(n-1) + " and " + str(n) + ", values " + str(curr[i]) + " and " + str(prev[i]))
            warning_mono.append(message)
        prev[i]=curr[i]  

def check_row(n, prev, curr_str, warning_total, warning_mono):
    curr = []
    for c in range(9): #CHANGE: E3 only need to check for values in TALL and T1-T8 columns (not the OTHER column)
        try:
            v = int(curr_str[c])
            curr.append(v)
        except ValueError:  # missing data so can't convert
            return False
    computed = calc_total(curr)
    if computed != curr[0]:
        warningMessageTotal = "Sum error at line " + str(n) + " " + str(curr_str) + " " + str(computed) + " computed " + str(curr[0]) + " expected"
        warning_total.append(warningMessageTotal)
    check_monotonic(prev, curr, n, warning_mono)
    return True # if there all data was there

def datamungerMain(inp, warning_total, warning_mono):
    def get_text(x): # does nothing in case of local files
        return x
    prev = [0,0,0,0,0,0,0,0] #CHANGE: only need 8 entries since only columns TALL and T1-T7 need to increase monotonically
    missing=0
    n=1
    for  line in inp:
         n=n+1
         str_vals  = get_text(line).strip().split(",")
         ok = check_row(n,prev,str_vals, warning_total, warning_mono)
         if not ok:
             missing = missing+1
    if(missing == 0):
        return True
    else:
        return missing

if __name__ == "__main__":
    origin  = sys.argv[1]
    if "http" in origin:
       ctx = ssl._create_unverified_context()
       inp = urllib.request.urlopen(origin, context=ctx)
       def get_text(x):  # for URL we need to convert from byte to string
           return x.decode('utf-8')
    else:
        inp = open(origin)

    inp.readline() # skip the header
    warning_total = []
    warning_mono = []
    result = datamungerMain(inp, warning_total, warning_mono)
    for wt in warning_total:
        print(wt)
    for wm in warning_mono:
        print(wm)
    if result != True:
        print("There were ",result," missing lines")
    

