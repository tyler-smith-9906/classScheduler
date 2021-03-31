import pandas as pd
import numpy as np
import json



#build the dataframe from the csv
df = pd.read_csv ('master_list.csv')    


#read the requested class list from the json and put into a dictonary
#with open('request.json') as f:
    #myClasses =  json.load(f)

#Code goes here to build a nice list of requested classes

#Temp lists, A holds letters, B holds codes, C hold indecies for the dataframe
listA = ["CIS", "COP", "ENG", "CDA"]
listB = [4250, 4960, 3250, 4212]
listC = []

#build dataframe of requested classes
for i in range(0, len(listA)):
    for j in range(0, len(df)):
        if (df['Letter'][j] == listA[i] and df['Number'][j] == listB[i]):
            listC.append(j)

print(listC)


