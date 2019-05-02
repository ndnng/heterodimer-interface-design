import numpy as np
import pandas as pd
import struct
import csv
import os,sys
import argparse

#parser = argparse.ArgumentParser(description="Analyze a sc score file.", formatter_class=argparse.RawTextHelpFormatter)
#parser.add_argument("-f", "--file", type=str, nargs="+", help="input a sc file")
#args = parser.parse_args()

file = sys.argv[1]
#basename= os.path.splitext(args.files[0])

newname = os.path.splitext(file)[0]
tag = os.path.splitext(file)[1]
os.rename(file, newname + '.txt')

newname = os.path.splitext(file)[0]
data = pd.read_fwf(newname+'.txt',sep=" ",skiprows = 1)


index = np.argmin(np.array(data['total_score']))
#data['description'][index]
print(data['description'][index], 'with the best slowest score = ',data['total_score'][index])
file = newname + '.txt'
#os.chdir('newoutput')
#oldext = os.path.splitext(file)[1]
os.rename(file, newname +'.sc')
