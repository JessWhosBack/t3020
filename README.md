
# T3020   Repo for ELEN3020

Name: Jesse van der Merwe
Date: 8 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.


## Errors Found
### ERROR 1
    for c in curr[2:9]: #E1

This line loops through the numbers stored in the curr array. However, these numbers are from the columns of the table, of which we need to add only columns T1 through T8 (inclusive). These are columns 1 and 8 respectively. Thus, this line should rather be: 

    for c in curr[1:9]:

### ERROR 2
    if curr[i] <=  prev[i]:  #E2

This line checks for monotonicity, however it is okay for the two fields to have the SAME value.
Thus, the line should rather be: 

    if curr[i] < prev[i]

### ERROR 3
    for d in curr_str: #E3
        try:
            v = int(d)

These line checks for missing data in all of the columns, however, it doesn't matter if there is missing data in the "OTHER" column.
This was therefore changed to only check for values in the TALL and T1-T8 columns: 
    
    for c in range(9): #E3
        try:
            v = int(curr_str[c])


### OTHER CHANGES
line 26:             for i in range(9) 
Was changed to:      for i in range(8)
Since column T8 does not need to be monotonic, and therefore shouldn't be checked

The prev array only needs 8 entries, since only columns TALL and T1 - T7 need to be monotonic. 

Line 61 was therefore changed from: 
    prev = [0,0,0,0,0,0,0,0,0,0]
To:
    prev = [0,0,0,0,0,0,0,0]

### CHANGES TO FACILITATE TESTING
Added the following two functions:

    if __name__ == "__main__":

    def datamungerMain(inp, warning_total, warning_mono):

The first function only runs if the user is running the program (as apposed to a unittest being performed on it). If this is the case, then the program looks for the second argument in the terminal line (that opens the correct data.csv file). 

The second function is called by the datamunger.py script automatically when the user runs it, OR is called by the unittest functions manually. This allows the unittests to access the other functions and functionality of the script. 

The datamungerMain function now returns the amount of lines that are missing entries and True if there are no missing entries. The program can now simply print this result with the appropriate text. This makes testing a lot easier as the number of missing entries can be compared immediately.

I have added a few arrays (namely warning_total, warning_mono) to store the results - instead of printing them directly to the console. This makes testing a lot easier, and is better coding practice in general (in case the user wants to store the results instead of just printing them. 








