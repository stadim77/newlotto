import pandas as pd
import numpy as np
from numpy import int64

filename = ['lotto_2018.xlsx', 'lotto_2019.xlsx', 'lotto_2020.xlsx', 'lotto_2021.xlsx']

#data = pd.DataFrame(columns=['event','date','1st','2nd','3rd','4th','5th','6th','bonus 7th'])
n = np.arange(1,50, dtype=int64)
print(n)
#---print(n.shape)

#print(pd.read_excel(filename[0]).iloc[3:,0:9])
df1 = pd.read_excel(filename[0]).iloc[3:,0:9]
df2 = pd.read_excel(filename[1]).iloc[3:,0:9]
df3 = pd.read_excel(filename[2]).iloc[3:,0:9]
df4 = pd.read_excel(filename[3]).iloc[3:,0:9]

###---RENAME COLUMNS
df1.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2018':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df2.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2019':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df3.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2020':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df4.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2021':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)


###  convert OBJECT to INT types
df11 = df1.iloc[:,2:9].astype(int)
df22 = df2.iloc[:,2:9].astype(int)
df33 = df3.iloc[:,2:9].astype(int)
df44 = df4.iloc[:,2:9].astype(int)


# data = pd.DataFrame(df11.iloc[:,2:9],columns=['1st','2nd','3rd','4th','5th','6th','bonus 7th'])
# print(data)

def occur(df, year):
    '''Return the top 3 numbers with most occurences in each column'''
    a = ((df.iloc[:,0].value_counts()[:3]).to_frame())
    a1 = ((df.iloc[:,0].value_counts()[:3]).tolist())
    b = ((df.iloc[:,1].value_counts()[:3]).to_frame())
    b1 = ((df.iloc[:,1].value_counts()[:3]).tolist())
    c = ((df.iloc[:,2].value_counts()[:3]).to_frame())
    c1 = ((df.iloc[:,2].value_counts()[:3]).tolist())
    d = ((df.iloc[:,3].value_counts()[:3]).to_frame())
    d1 = ((df.iloc[:,3].value_counts()[:3]).tolist())
    e = ((df.iloc[:,4].value_counts()[:3]).to_frame())
    e1 = ((df.iloc[:,4].value_counts()[:3]).tolist())
    f = ((df.iloc[:,5].value_counts()[:3]).to_frame())
    f1 = ((df.iloc[:,5].value_counts()[:3]).tolist())

# get the numbers as a list
    aa = ((df.iloc[:,0].value_counts()[:3]).index.tolist())
    bb = ((df.iloc[:,1].value_counts()[:3]).index.tolist())
    cc = ((df.iloc[:,2].value_counts()[:3]).index.tolist())
    dd = ((df.iloc[:,3].value_counts()[:3]).index.tolist())
    ee = ((df.iloc[:,4].value_counts()[:3]).index.tolist())
    ff = ((df.iloc[:,5].value_counts()[:3]).index.tolist())
    #--- print(f'The most lucky numbers are {aa},{bb},{cc},{dd},{ee} and {ff}')
    #--- print(f'and the freqs are {a1},{b1},{c1},{d1},{e1} and {f1}')
    # print(aa)
    # print(bb)
    # print(cc)
    # print(dd)
    # print(ee)
    # print(ff)
    #---print(f'The most lucky numbers are {aa},{bb},{cc},{dd},{ee} and {ff} for {year}\n and the freqs are {a1},{b1},{c1},{d1},{e1} and {f1}')

    return  [aa, bb, cc,dd, ee, ff]



#---print(occur(df11,2018)[1][:2])
print("MOST FREQ NUMBERS IN EACH YEAR!!!")
print(occur(df11,2018))
best1 = np.array(occur(df11,2018))
print(occur(df22,2019))
best2 = np.array(occur(df22,2019))
print(occur(df33,2020))
best3 = np.array(occur(df33,2020))
print(occur(df44,2021))
best4 = np.array(occur(df44,2021))
#---print(np.append(best1, best2, best3, best4))
bestof1 = np.append(best1, best2)
bestof2 = np.append(best3, best4)
bestof = np.append(bestof1, bestof2)
print(bestof.size)
unique, counts = np.unique(bestof, return_counts=True)
print('-----------------------------')
print(np.asarray((unique, counts)).T)
#print(bestof.shape)
# print(df1.head(7))



# print(df1.columns)


# #data.astype(int)
# print(data)

### SEARCH CONTINUOUS VALUES IN EACH COLUMN ###
# a1 = np.array(df11['1st'].tolist())
# a2 = np.array(df11['2nd'].tolist())
# a3 = np.array(df11['3rd'].tolist())
# a4 = np.array(df11['4th'].tolist())
# a5 = np.array(df11['5th'].tolist())
# a6 = np.array(df11['6th'].tolist())


def positioning(dframe,num):
    '''returns the position of a number in each column'''
    a1 = np.array(dframe['1st'].tolist())
    a2 = np.array(dframe['2nd'].tolist())
    a3 = np.array(dframe['3rd'].tolist())
    a4 = np.array(dframe['4th'].tolist())
    a5 = np.array(dframe['5th'].tolist())
    a6 = np.array(dframe['6th'].tolist())
    sel_num = []
    for i in [a1, a2, a3, a4, a5, a6]:
        print(np.where(i == num)[0])
        n = np.where(i == num)[0]
        sel_num.append(n)
    return sel_num

# positioning(df11,22)
# print('-----------')
# positioning(df22,22)

def indexing(dframe,num):
    ''' get the number that follows in the next event for a number that you want '''
    a1 = np.array(dframe['1st'].tolist())
    a2 = np.array(dframe['2nd'].tolist())
    a3 = np.array(dframe['3rd'].tolist())
    a4 = np.array(dframe['4th'].tolist())
    a5 = np.array(dframe['5th'].tolist())
    a6 = np.array(dframe['6th'].tolist())
    st_next = []
    st_before = []
    for elem in [a1,a2,a3,a4,a5,a6]:
        for n in num:
            print(n)
            indices = [i for i, x in enumerate(elem) if x == n]
            new_list = [x + 1 for x in indices]
            pre_list = [x - 1 for x in indices]
        # print(indices)
        # print('xxxxxxxxxxxxxx')
        # print(new_list)
            print(f'The numbers following {n} are {elem[new_list]}')
            print(f'The numbers before {n} are {elem[pre_list]}.')
            print('--------------')
            st_next.extend(elem[new_list])
            st_before.extend(elem[pre_list])
    #print(f'The numbers after {n} are {st_next}.')

#---indexing(df44,36)
#---print(occur(df44,2021)[1])
#---indexing(df11,occur(df44,2021)[1])

### Print the events where the number is the selected ###
print(f'the more freq number are {occur(df44,2021)[1]}')
print(df44[df44['2nd'] == occur(df44,2021)[1][0]])
print(df44[df44['2nd'] == occur(df44,2021)[1][1]])
print(df44[df44['2nd'] == occur(df44,2021)[1][2]])

# print(df11.columns)
#
# lista = df44['1st'].to_list()
# print(lista)
# print(lista.index(13))
#
# print([i for i,val in enumerate(lista) if val==13])

## Convert dataframe to numpy array ##
## c = pd.DataFrame(df44).to_numpy()
## print(c)

### CONVERT DATAFRAMES TO NUMPY ARRAY ###
cc = df44.iloc[:,:6].values
print(cc)
#print(type(cc))
numm = 15
result = np.where(cc==numm)
print(f'Number {numm} appears in {len(result[0])} events {result[0]} and in position {result[1] + 1} from 1 to 6 in each row.')
print(cc[4])
print(cc[57])
print(cc[76])