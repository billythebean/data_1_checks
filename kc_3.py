from tarfile import LENGTH_NAME
import pandas as pd
import operator
import csv


#assign dataset
df = pd.read_csv(r'C:\Users\Julie\Downloads\Python\Code Louisville\Knowledge Checks\1st Data Check\kc_3\16P.csv',  encoding= 'unicode_escape')

 
#mapping is equal to personalities
# 0 = ESTJ - The Supervisor
# 1 = ENTJ - The Commander 
# 2 = ESFJ - The Provider 
# 3 = ENFJ - The Giver
# 4 = ISTJ - The Inspector
# 5 = ISFJ - The Nurturer 
# 6 = INTJ - The Mastermind
# 7 = INFJ - The Counselor
# 8 = ESTP - The Doer
# 9 = ESFP - The Performer
# 10 = ENTP - The Visionary
# 11 = ENFP - The Champion 
# 12 = ISTP - The Craftsman
# 13 = ISFP - The Composer 
# 14 = INTP - The Thinker 
# 15 = INFP - The Idealist 

#returning length as 0x0000026BC1E8FC70
def length(df):
      return(length)
print(length)

#sorting lines in data in order
def sort(df):
    sorted(df,key=operator.itemgetter)
for eachline in sort:
    print(eachline) 
    