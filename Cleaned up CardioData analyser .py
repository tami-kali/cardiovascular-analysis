#helper function for testing functions 
def testing(fx, result):
    """
    purpose:
    testing function, will compare the output of a function to the expected outcome
    
    input parameters:
    1. a function with parameters 
    
    2. expected result of the function put in for parameter 1
    
    output:
    Boolean
    
    True if output is expected, False if not 
    """
    if fx == result:
        print("test passed")
    else: 
        print("test failed, expected " + str(result) + " but got " + str(fx))


# ### DATA DEFINITIONS 
# created a class for CardioData and examples of the data that will be going through the program 

#data definition for the data that will be used by the program to compute desired values 
class CardioData:
    def __init__(cd, sbp, dbp, meanap,  hr, time):
        cd.sbp = sbp
        cd.dbp = dbp
        cd.meanap = meanap
        cd.hr = hr
        cd.time = time 
           
    def output(self):
        return(cd.sbp, cd.dbp, cd.meanap, cd.hr, cd.time)
    
    def __repr__(self):
        return ("\n" + "sbp = " + str(self.sbp ) 
                + "| dbp = " + str(self.dbp) 
                + "| map = " + str(self.meanap)
                + "| hr = " + str(self.hr)
                + "| time = " + str(self.time)) 
    def __eq__(cd, other):
        if not isinstance (other, CardioData):
            return NotImplemented
        return cd.sbp == other.sbp and cd.dbp == other.dbp and cd.meanap == other.meanap and cd.hr == other.hr and cd.time == other.time
    
"""
a data definition for CardioData which includes a  SBP DBP and meanap (systolic, diastolic blood pressure and mean arterial pressire floats in mmHg), HR (heart rate float in BPM), and time (as an integer in seconds)
"""
#examples
C1 = CardioData(124.000, 80.232, 100.323, 567.387, 3144)
C2 = CardioData(145.002, 100.322, 125.323, 435.034, 5094)
C3 = CardioData(145.002, 100.322, 125.323, 435.034, 30)
C4 = CardioData(132.323, 100.323, None, 435.232, 40)
C5 = CardioData(122.323, None, None, 533.131, 60)


#List[CardioData]
"""
#data definition for entire data set represented as rows of CardioData - used by program for calculations
#List[InputCardioData]
"""
#examples
LOCD1 = []
LOCD2 = [C1, C2]
LOCD3 = [C1, C2, C3]

#template function 
def fn_for_locd(locd):
    # description of the acc
    acc = ... # type: ...
    for cd in locd:
        acc = ... (acc, fn_for_cardiodata(cd))
    return acc


#data definition for a list of AD events - an array technically 
#List[List[CardioData]]
#a list of lists of CardioData

#examples
LOAD1 = []
LOAD2 = [LOCD1, LOCD1]
LOAD3 = [LOCD1, LOCD2]
LOAD4 = [LOCD3, LOCD1, LOCD2]


#body - list with reference rule
def fn_for_load(load) -> ...:
    # description of the acc
    acc = ... # type: ...
    for cd in locd:
        acc = ... (acc, fn_for_locd(cd))
    return acc

test_1 = [CardioData(141.115625,None,None,338.726,1), 
          CardioData(141.284375,None,None,340.7056,2), 
          CardioData(141.3671875,None,None,342.9861,3), 
          CardioData(140.23125,None,None,340.0022,4),
          CardioData(140.246875,None,None,351.1132,5)] 
                
test_2 = [CardioData(141.115625,89.740625,106.8656235,338.726,1), 
          CardioData(141.284375,89.184375,106.5510391,340.7056,2), 
          CardioData(141.3671875,88.75,106.2890625,342.9861,3), 
          CardioData(140.23125,88.7,105.8770828,340.0022,4), 
          CardioData(140.246875,89.440625,106.3760422,351.1132,5)]


# ### READ FUNCTION 
# csv conversion to a CardioData format, to be used by the program

import csv
#helper function: convert str in hh:mm:ss format to total seconds
#read function --> similar to the parse_int and parse_float functions

def find_seconds(t):
    """
    purpose:
    take a string, and looking at its time (string in hh:mm:ss format),
    converts to whole seconds, and returns the time in total seconds 
    
    input parameters:
    t which is a string 
    
    output: 
    integer 
    """
    if t is None or t == '': 
        return None
    else:
        h, m, s = t.split(':')
        return int(h)*3600 + int(m)*60 + int(s)

#tests
print("tests for converting time ")
testing(find_seconds('00:00:05'), 5) 
testing(find_seconds('00:01:01'), 61) 
testing(find_seconds('01:00:00'), 3600) 


#helper function: find blank values and gives a place holder 
def read_blanks(s): 
    """
    purpose:
    replaces blank strings with None
    
    input parameters:
    s which is a string 
    
    output:
    integer or None 
    """
    if s is None or s == '': 
        return None
    else:
        return float(s)

#tests
print('')
print("tests for blanks and conversion function")
testing(read_blanks('123'), 123) 
testing(read_blanks(None), None) 
testing(read_blanks(''), None) 



def empty_values(locd):
    """
    purpose: 
    iterates through CardioData and returns a message on location of missing values in data file
    
    input parameter:
    list of cardiodata (locd) a data definition which was defined above 
    
    output:
    string which is a defined below as a error message 

    """
    result = []
    
    for cd in locd:
        if cd.sbp is None:
            result.append("no value for SBP in row " + str(locd.index(cd)+1))
        if cd.dbp is None:
            result.append("no value for DBP in row " + str(locd.index(cd)+1))
        if cd.meanap is None:
            result.append("no value for MAP in row " + str(locd.index(cd)+1))
        if cd.hr is None:
            result.append("no value for HR in row " + str(locd.index(cd)+1))
        if cd.time is None:
            result.append("no value for TIME in row " + str(locd.index(cd)+1))
    if len(result) == 0:
        return "good to go"
    else:
        return result + ['double check your csv']
            
            
print('')
print("tests for empty value checker")
testing(empty_values([]), 'good to go')
testing(empty_values(test_2), 'good to go')
testing(empty_values(test_1), ['no value for DBP in row 1', 'no value for MAP in row 1', 
                           'no value for DBP in row 2', 'no value for MAP in row 2',
                           'no value for DBP in row 3', 'no value for MAP in row 3', 
                           'no value for DBP in row 4', 'no value for MAP in row 4', 
                           'no value for DBP in row 5', 'no value for MAP in row 5',
                           'double check your csv'])


def read(file):
    """    
    purpose: 
    reads information from the specified file and returns a list of cardio data
    
    input parameter:
    file which has to be in string format 
    
    output: 
    list of cardiodata a data type defined above 
    
    important condition:
    file cannot have entirely empty rows 
    """
    #locc contains the result so far
    locd = [] # type: List[CardioData]

    with open(file, 'r') as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            #conversion of files into floats (for blood pressure and heart rate), and seconds (for time)
            cd = CardioData(read_blanks(row[0]), 
                            read_blanks(row[1]), 
                            read_blanks(row[2]), 
                            read_blanks(row[3]), 
                            find_seconds(row[4])
                            )
            locd.append(cd)
            
    return locd



#tests
print('')
print("tests for read csv function")
print("file 1")
t1 = read("small_test_file1.csv")
print(t1)
print('')
print("file 2")
t2 = read("small_test_file2.csv")
print(t2)




def errors(file):
    """
    purpose:
    reads csv file, and reports blank values and their location
    
    input parameter:
    file name which is a string 
    
    output:
    a list of strings 
    """
    return empty_values(read(file))

#tests
print('')
print('tests for error function')
testing(errors("small_test_file2.csv"), 'good to go')
testing(errors("small_test_file1.csv"), ['no value for DBP in row 1', 'no value for MAP in row 1', 
                                        'no value for DBP in row 2', 'no value for MAP in row 2',
                                        'no value for DBP in row 3', 'no value for MAP in row 3', 
                                        'no value for DBP in row 4', 'no value for MAP in row 4', 
                                        'no value for DBP in row 5', 'no value for MAP in row 5',
                                        'double check your csv'])



# ### HELPER FUNCTIONS
# helper functions for calculating cut off values 


from statistics import stdev,mean
from operator import attrgetter, contains


def column_list(locd, t):
    """
    purpose:
    takes a list of cardiodata and returns only the the specified column (bp, or hr)
    t can be one of sbp dbp meanap or hr 
    
    input parameters: 
    1. list of cardiodata (defined data type above) 
    
    2. t which is a string 
    
    output: 
    a list of floats
    """
    bpl = [] # type: List[float]
    for cd in locd:
        a = attrgetter(t)
        bpl.append(a(cd))
        
    return bpl

#testing
testing(column_list(LOCD1, 'sbp'), []) #expect []
testing(column_list(LOCD2, 'hr'), [567.387, 435.034]) 
testing(column_list(LOCD3, 'dbp'), [80.232, 100.322, 100.322])


def average(locd, t):
    """
    purpose: 
    takes a list of cardiodata and returns the average of a single column ie - blood pressures and heart rates
    
    input parameter:
    1. list of cardiodata (defined in data definitions) 
    
    2. t which is a string (can be one of sbp, dbp, map, hr)
    
    output:
    float 
    """
    return mean(column_list(locd, t))


#testing
testing(average(LOCD2, 'hr'), 501.21049999999997) 
testing(average(LOCD3, 'dbp'), 93.62533333333333)

#TODO:
#edge cases where t is not one of the columns 

def deviation(locd, t):
    """
    purpose:
    takes a list of cardiodata and returns the standard deviation of a single column ie - blood pressures and heart rates
    
    input parameters: 
    
    1. list of cardiodata 
    
    2. t which is a string (can be one of sbp, dbp, map, hr)
    
    output: 
    float 
    """
    return stdev(column_list(locd, t))

#testing
testing(deviation(LOCD2, 'hr'), 93.58770381038309)
testing(deviation(LOCD3, 'dbp'), 11.598966908019582)


#note for use later:
#adjust number of standard deviations for cutoff, 0 if you don't want to use this criteria for baseline
#sd = int(input('number of standard deviations: ')) #as a standard, 1 stdev is used for calculation
sd = 1

def generate_cutoff(locd, atr, sd):
    """ 
    purpose:
    takes a list of cardiodata, calculated averages, standard deviations, 
    and produces cut off values (min and max) (inclusive), based on desired atribute (atr)
    that will be used to determine the baseline
    
    input parameters: 
    
    1. list of cardiodata
    
    2. atr (which can be one of sbp, dbp, map, hr)
    
    3. sd which is the number of standard deviations away - currently defined right above the function 
    
    
    output: 
    a list of floats (will always be two)
    """
 
    avg  = average(locd, atr)
    sd = deviation(locd, atr) * sd
    return (avg - sd, avg + sd)


#testing 
testing(generate_cutoff(LOCD2, 'sbp', sd), (119.65034338152013, 149.3516566184799))
testing(generate_cutoff(LOCD2, 'hr', sd), (407.6227961896169, 594.798203810383))
testing(generate_cutoff(LOCD2, 'dbp',sd), (76.07122476596226, 104.48277523403775))
testing(generate_cutoff(LOCD2, 'meanap', sd), (95.1453304703363, 130.5006695296637))

def above_or_below(cd, atr, co):
    """
    purpose:
    takes a cardiodata, and a cutoff value and returns True if value is within the range
    only works with one particular attibute at a time 
    
    input parameters:
    
    1. cd which is cardiodata (not a list) but a single row 
    
    2. atr which is the desired column to test on (can be one of sbp, dbp, map, hr)
    
    3. co which is a cutoff value that can be generated using the generate cutoff function 
    
    output:
    boolean 
    true if value within range, false otherwise 
    """
    a = attrgetter(atr)
    return a(cd) >= co[0] and a(cd) <= co[1]

testing(above_or_below(CardioData(5,5,5,5,5), 'sbp', (1,8)), True)
testing(above_or_below(CardioData(5,10,5,5,5), 'dbp', (1,8)), False)
testing(above_or_below(CardioData(5,5,5,0,5), 'hr', (1,8)), False)
testing(above_or_below(CardioData(5,5,5,1,5), 'hr', (1,8)), True)
testing(above_or_below(CardioData(5,5,5,8,5), 'hr', (1,8)), True)



""" NEED TO BE TIDIED 
def sbp_filt(sbpf, cd, locd):
    if sbpf == 'y':
        if cd.sbp is None:
            print("no value for sbp filter")
            return False
        else: 
            return above_or_below(cd, 'sbp', generate_cutoff(locd, 'sbp', sd))
    elif sbpf == 'n':
            return True
            
            
def dbp_filt(dbpf, cd, locd):
    if dbpf == 'y':
        if cd.dbp is None:
            print("no value for dbp filter")
            return False
        else: 
            return above_or_below(cd, 'dbp', generate_cutoff(locd, 'dbp', sd))
    elif dbpf == 'n':
        return True
        
def map_filt(mapf, cd, locd):
    if mapf == 'y':
        if cd.meanap is None:
            print("no value for map filter")
            return False
        else: 
            return above_or_below(cd, 'meanap', generate_cutoff(locd, 'meanap', sd))
    elif mapf == 'n':
        return  True
        
        
def hr_filt(hrf, cd, locd):
    if hrf == 'y':
        if cd.hr is None:
            print("no value for hr filter")
            return True
        else:
            return above_or_below(cd, 'hr', generate_cutoff(locd, 'hr', sd))
    elif hrf == 'n':
        return True 
"""      
        
def baseline(locd):
    """
    purpose:
    based on cutoff values, create a list of cardio data that is within the cutoff bounds
    ie - at least the minimum and at most the maximum
    
    input: 
    list of cardiodata 
    
    output: 
    list of cardiodata 
    """
    
    #filters, y/n if you wish to filter using a specific attribute - 
    #saying no to all, will just give the original list of cardiodata and use it as a baseline 
    #sbpf = input('filter by sbp? ')
    #dbpf = input('filter by dbp? ')
    #mapf = input('filter by map? ')
    #hrf = input('filter by hr? ')
    
    sbpf = 'y'
    dbpf = 'n'
    mapf = 'n'
    hrf = 'n'
    
    #list of cardiodata in the cutoff range seen so far 
    filtered = [] # type: List[CardioData]
    for cd in locd:   
        if sbp_filt(sbpf, cd, locd) and dbp_filt(dbpf, cd, locd) and map_filt(mapf, cd, locd) and hr_filt(hrf, cd, locd):
            filtered.append(CardioData(cd.sbp, cd.dbp, cd.meanap, cd.hr, cd.time))
    return filtered



#examples for testing 
L1 = [CardioData(-20,-20,-20,-20,-20),
      CardioData(30,30,30,30,30), 
      CardioData(5,5,5,5,5), 
      CardioData(5,5,5,5,5),
      CardioData(5,5,5,5,5)]

L2 = [CardioData(-50,-50,-50,-50,-50),
      CardioData(50,50,50,50,50), 
      CardioData(0,0,0,0,0), 
      CardioData(0,0,0,0,0)]

L3 = [CardioData(None,-50,None,-50,-50),
      CardioData(None,50,None,50,50), 
      CardioData(None,0,None,0,0), 
      CardioData(None,0,None,0,0)]

L4 = [CardioData(-50,None,-50,-50,-50),
      CardioData(50,None,50,50,50), 
      CardioData(0,None,0,0,0), 
      CardioData(0,None,0,0,0)]

#R1 = [L1[2], L1[3], L1[4]]
R1 = [CardioData(5,5,5,5,5), 
      CardioData(5,5,5,5,5),
      CardioData(5,5,5,5,5)]
R2 = [CardioData(0,0,0,0,0), 
      CardioData(0,0,0,0,0)]
R4 = [CardioData(0,None,0,0,0), 
      CardioData(0,None,0,0,0)]

testing(baseline(L2), R2)
testing(baseline(L1), R1)
testing(baseline(L3), [])
testing(baseline(L4), R4)


# In[14]:


def find_criteria(locd): 
    """
    takes a list of  CardioData, a minimum SBP value, HR value and duration, 
    and returns a criteria to identify cardiovascular events, where p will always be p_crit, 
    b will always be b_crit, and n will always be n_crit 
    
    input: 
    list of cardiodata 
    
    output: 
    cardiodata 
    """
    
    #classification event: 
    #### make into user input (convert to float)
    #SBP has to be at least mmHg higher than the baseline SBP
    sbp_crit = 20.000 #set at 20 mmHg by default 
    
    #DBP has to be at least mmHg higher than the baseline DBP
    dbp_crit = 20.000 #default at 20 mmHg
    
    #MAP has to be at least mmHg higher than the baseline MAP
    map_crit = 10.000 #default at 10 mmHg
    
    #HR has to be at least (b_crit) BPM lower than the baseline HR
    hr_crit = -40.000 #set at -40 BPM by default -> MUST include a negative sign (-)
    
    #the event has to last at least (n_crit) seconds 
    time_crit = 30 #set at 30 seconds minimum  
    
    #systolic blood pressure
    if sbp_crit == 0 or sbp_crit is None:
        sbp = 0
    else: 
        sbp = average(baseline(locd), 'sbp') + sbp_crit
    
    #diastolic blood pressure
    if dbp_crit == 0 or dbp_crit is None: 
        dbp = 0
    else: 
        dbp = average(baseline(locd), 'dbp') + dbp_crit
        
    #mean arterial pressure
    if map_crit == 0 or map_crit is None:
        meanap = 0
    else: 
        meanap = average(baseline(locd), 'meanap') + map_crit
    
    #heart rate
    if hr_crit == 0 or hr_crit is None:
        hr = 0
    else: 
        hr = average(baseline(locd), 'hr') + hr_crit
        
    return (sbp, dbp, meanap, hr, time_crit)
    

#testing
print("testing for criteria finder")
testing(find_criteria(L1), (25,25,15,-35,30))
testing(find_criteria(L2), (20,20,10,-40,30))


def ad_event_crit(cd, crit) -> bool:
    """
    purpose:
    takes a cardiodata and returns True if a blood pressure and heart rate meet the criteria, 
    False otherwise
    
    input: 
    1. cardiodata 
    
    2. criteria which was found using find_criteria function (which is a cardiodata) 
    
    output: 
    boolean 
    true if parameter 1 is within parameter 2 criteria, false otherwise 
    """
    if cd.sbp is None: 
        cd.sbp = crit[0]
    if cd.dbp is None:
        cd.dbp = crit[1]
    if cd.meanap is None:
        cd.meanap = crit[2]
    if cd.hr is None:
        cd.hr = crit[3]

    return cd.sbp >= crit[0] and cd.dbp >= crit[1] and cd.meanap >= crit[2] and cd.hr <= crit[3]  

#testing 

#testing(ad_event_crit(CardioData(10,None,10,None,10), (10,10,10,10,10)), True)

testing(ad_event_crit(CardioData(0, 0, 0, 0, 0), (10, 10, 10, 10, 5)), False)
testing(ad_event_crit(CardioData(10, 10, 10, 10, 10), (10, 10, 10, 10, 10)), True)
testing(ad_event_crit(CardioData(10, 10, 10, 8, 10), (9, 9, 9, 9, 9)), True) 
testing(ad_event_crit(CardioData(10, 10, 10, 10, 10), (11, 11, 11, 11, 11)), False)
testing(ad_event_crit(CardioData(10, 0, 0, 0, 10), (10, 10, 10, 10, 10)), False)
testing(ad_event_crit(CardioData(10, None, None, 10, 10), (10, 10, 10, 10, 10)), True)
testing(ad_event_crit(CardioData(None, None, None, None, 10), (10, 10, 10, 10, 10)), True)

def time_diff(cd1, cd2) -> int:
    """
    purpose: 
    finds the time difference between two cardiodatas
    
    input: 
    1. cardiodata 
    
    2. cardiodata 
    
    output: 
    integer
    """
    return cd2.time - cd1.time 

#testing
C3 = CardioData(145.002, 112.323, 129.323, 435.034, 30)
C4 = CardioData(124.000, 100.323, 114.323, 405.123, 15)
C5 = CardioData(140.234, 120.332, 133.332, 560.384, 13)

testing(time_diff(C5, C4), 2)
testing(time_diff(C4, C3), 15)



def event_duration(locd, crit) -> bool:
    """
    purpose: 
    takes a list of cardio data and returns True if the list is equal or greater than the criteria duration, 
    False otherwise
    
    input: 
    1. list of cardiodata 
    
    2. criteria duration 
    
    output: 
    boolean 
    
    """
    #give interval that you're taking time points at (every 5 seconds, every 1 etc...)
    time_interval = 5
    
    first = locd[0].time
    last = locd[-1].time
    
    return last - first + time_interval >= 30
   
    
def event_length(locd) -> int:
    """
    gives the total duration of an event 
    """
    return locd[-1].time - locd[0].time + time_interval


#testing
L1 = [CardioData(10, 10, 10, 10, 10), CardioData(10, 10, 10, 10, 20)]
L2 = [CardioData(10, 10, 10, 10, 10), CardioData(10, 10, 10, 10, 60)]
C1 = (10, 10, 10, 10, 30)
testing(event_duration(L1, C1), False)
testing(event_duration(L2, C1), True)


# In[17]:


def separate_events(locd, crit):
    """
    takes a list of cardio data and gives an array of cardiovascular events based on criteria
    """
    count = [] #type: array[int]
    index = 0
    for cd in locd: 
        position = index
        previous = locd[position-1]
        if ad_event_crit(cd, crit):
            if ad_event_crit(previous, crit) == False :
                count.append([cd])
            elif ad_event_crit(previous, crit) == True:
                count[-1].append(cd)
        else:
            count = count
        index = index + 1
    return count

#testing
C1 = CardioData(124.000, None, None, 567.387, 3144)
C2 = CardioData(145.002, None, None, 435.034, 5094)
C3 = CardioData(145.002, None, None, 435.034, 30)
C4 = CardioData(124.000, None, None, 405.123, 15)
C5 = CardioData(140.234, None, None, 560.384, 13)
C6 = CardioData(155.7486, None, None, 440.2924, 30)
C7 = CardioData(156.6476, None, None, 439.5924, 100)
C8 = CardioData(155.5476, None, None, 439.5924, 30)
CRIT1 = (155.6476, 0, 0, 440.5924,30)
FEL1 = [C1, C6, C7, C8, C1, C1, C1, C5, C6, C1, C8, C7]
testing(separate_events(FEL1, CRIT1), [[C6, C7], [C6], [C7]])

def filter_by_time(locd, crit):
    """
    takes an array and returns an array only containing events equal to or longer than the criteria
    """
    count = [] #type: array[]
    for lst in locd:
        if event_duration(lst, crit) == True:
            count.append(lst)
        elif event_duration(lst, crit) == False:
            count = count 
    return count 

#testing
FEL2 = separate_events(FEL1, CRIT1)
testing(filter_by_time(FEL2, CRIT1), [[C6, C7]])


def num_events(locd):
    """
    returns number of events 
    """
    return len(locd)

#testing
FEL3 = filter_by_time(FEL2, CRIT1)
testing(num_events(FEL3), 1)


def filter_events(locd, crit):
    return filter_by_time(separate_events(locd, crit), crit)



#errors = errors('T17 ON.csv')
test1 = read('T17 ON.csv')

print(test1)



criteria = baseline(test1)
criteria




