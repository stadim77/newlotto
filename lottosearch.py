import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = ['/home/stavros/PycharmProjects/newlotto/lotto_2018.xlsx',
            '/home/stavros/PycharmProjects/newlotto/lotto_2019.xlsx',
            '/home/stavros/PycharmProjects/newlotto/lotto_2020.xlsx',
            '/home/stavros/PycharmProjects/newlotto/lotto_2021.xlsx']

#---num = [36,24,46,30,27,21,11,22,48,14,35,40,34,47]
#num = [22,23,30,34,36,38,48]
#num = [4,5,9,17,35,37,46]
num = [36,48,34,38,30,23,22,1]

### CREATE DATAFRAMES ###
df1 = pd.read_excel(filename[0]).iloc[3:,0:9]
df2 = pd.read_excel(filename[1]).iloc[3:,0:9]
df3 = pd.read_excel(filename[2]).iloc[3:,0:9]
df4 = pd.read_excel(filename[3]).iloc[3:,0:9]

df1.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2018':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df2.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2019':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df3.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2020':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)
df4.rename(columns={'ΑΠΟΤΕΛΕΣΜΑΤΑ ΛΟΤΤΟ 2021':'event','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd','Unnamed: 4':'3rd','Unnamed: 5':'4th','Unnamed: 6':'5th','Unnamed: 7':'6th','Unnamed: 8':'bonus number'}, inplace=True)

###  convert OBJECT to INT types ###
df11 = df1.iloc[:,2:9].astype(int)
df22 = df2.iloc[:,2:9].astype(int)
df33 = df3.iloc[:,2:9].astype(int)
df44 = df4.iloc[:,2:9].astype(int)

### CONVERT DATAFRAMES TO NUMPY ARRAY ###
a1 = df11.iloc[:,:6].values
a2 = df22.iloc[:,:6].values
a3 = df33.iloc[:,:6].values
a4 = df44.iloc[:,:6].values

print(a1.shape)
print(a2.shape)
print(a3.shape)
print(a4.shape)
# print('------')
# print(a1)
# print('------')
#---print(a1 - a2)
ag = df44.iloc[1].to_list()

#---result = [np.where(a1==num[0]),np.where(a2==num[0]),np.where(a3==num[0]),np.where(a4==num[0])]
#---print(f'Number {num[0]} appears in {len(result[0][0])+len(result[1][0])+len(result[2][0])+len(result[3][0])} events {result[0][0]},{result[1][0]},{result[2][0]},{result[3][0]} \n and in position {result[0][1] + 1} 2018, {result[1][1] +1} 2019, {result[2][1]} 2020, {result[3][1]} 2021 from 1 to 6 in each row.')

def appear(number):
    for i in number:
        result = [np.where(a1 == i), np.where(a2 == i), np.where(a3 == i), np.where(a4 == i)]
        print(f'Number --{i}--- appears in {len(result[0][0])+len(result[1][0])+len(result[2][0])+len(result[3][0])} events.')
        print(f'{df1.iloc[result[0][0]]["date"]},\n{df2.iloc[result[1][0]]},\n{df3.iloc[result[2][0]]},\n{df4.iloc[result[3][0]]}')
# appear([20,30])
#-print(result[0][1])

### CHANGE DIMENSIONS OF NUMPY ARRAYS ###
lotto2018 = np.reshape(a1,(1,624))
lotto2019 = np.reshape(a2,(1,624))
lotto2020 = np.reshape(a3,(1,534))
lotto2021 = np.reshape(a4,(1,582))

#-print(lotto2018)
unique, counts = np.unique(lotto2018, return_counts=True)
print(np.asarray((unique, counts)).T) # prints the occurences of numbers
os1 = np.asarray((unique, counts)).T
#---print(np.where(lotto2018 == num[0]))
print('----------')
unique, counts = np.unique(lotto2019, return_counts=True)
print(np.asarray((unique, counts)).T) # prints the occurences of numbers
os2 = np.asarray((unique, counts)).T
#---print(np.where(lotto2019 == num[0]))
print('----------')
unique, counts = np.unique(lotto2020, return_counts=True)
print(np.asarray((unique, counts)).T) # prints the occurences of numbers
os3 = np.asarray((unique, counts)).T
#---print(np.where(lotto2020 == num[0]))
print('----------')
unique, counts = np.unique(lotto2021, return_counts=True)
print(np.asarray((unique, counts)).T) # prints the occurences of numbers
os4 = np.asarray((unique, counts)).T
#---print(np.where(lotto2021 == num[0]))
print('----------')

freqs1 = np.append(os1, os2)
freqs2 = np.append(os3, os4)
total_freqs = np.append(freqs1, freqs2, axis=0)
print(total_freqs)
print(total_freqs.shape)
# print(num[0])
# print(np.where(lotto2018 == num[0])[1]) #εμφανίζει πότε κληρώθηκαν οι αριθμοί
# print(num[1])
# print(np.where(lotto2018 == num[1])[1]) #εμφανίζει πότε κληρώθηκαν οι αριθμοί
# print(num[2])
# print(np.where(lotto2018 == num[2])[1]) #εμφανίζει πότε κληρώθηκαν οι αριθμοί

for i in range(1,49):
    if i in num:
        print(i)
        print(np.where(lotto2018 == i)[1])
        print(f'Total number is : {len(np.where(lotto2018 == i)[1])} for 2018.')
        print('-----')
        print(np.where(lotto2019 == i)[1])
        print(f'Total number is : {len(np.where(lotto2019 == i)[1])} for 2019.')
        print('-----')
        print(np.where(lotto2020 == i)[1])
        print(f'Total number is : {len(np.where(lotto2020 == i)[1])} for 2020.')
        print('-----')
        print(np.where(lotto2021 == i)[1])
        print(f'Total number is : {len(np.where(lotto2021 == i)[1])} for 2021.')


rythm = []
for i in range(1,624,49):
    rythm.append(i)
#---print(rythm)

def appearances(num):
    '''return the expected positions of the selected number'''
    rt = []
    for i in range(num,624,49):
        rt.append(i)
    return rt
#---print(appearances(93))


### FIND THE POSITIONS OF NUMBER IN ALL EVENTS ###
# print(np.where(lotto2018 == 1)[1]) # return the occurences of 1 in sequence of 2018
# print(np.where(lotto2019 == 1)[1]) # return the occurences of 1 in sequence of 2019
# print(np.where(lotto2020 == 1)[1]) # return the occurences of 1 in sequence of 2020
# print(np.where(lotto2021 == 1)[1]) # return the occurences of 1 in sequence of 2021

def mynums(nums):
    '''returns the list of positions of number occurence every year'''
    for i in nums:
        print(f' Number {i} occurs in positions.')
        print(f'2018 :{np.where(lotto2018 == i)[1]} for {len(np.where(lotto2018 == i)[1])} times')  # return the occurences of 1 in sequence of 2018
        print(f'2019 :{np.where(lotto2019 == i)[1]} for {len(np.where(lotto2019 == i)[1])} times')  # return the occurences of 1 in sequence of 2019
        print(f'2020 :{np.where(lotto2020 == i)[1]} for {len(np.where(lotto2020 == i)[1])} times')  # return the occurences of 1 in sequence of 2020
        print(f'2021 :{np.where(lotto2021 == i)[1]} for {len(np.where(lotto2021 == i)[1])} times')  # return the occurences of 1 in sequence of 2021

mynums(num)

def my_selected_nums(event):
    '''prints the numbers of a given event each year '''
    assert event != 0
    print('SIMILAR EVENTS EACH YEAR')
    print(f'2018 {df1.date.iloc[len(df1.date) - event]} :{a1[event]}.')
    print(f'2019 {df2.date.iloc[len(df2.date) - event]} :{a2[event]}.')
    print(f'2020 {df3.date.iloc[len(df3.date) - event]} :{a3[event]}.')
    print(f'2021 {df4.date.iloc[len(df4.date) - event]} :{a4[event]}.')

my_selected_nums(1)

### PLOT THE OCCURENCES OF A NUMBER EACH YEAR ###
# plt.plot(np.where(lotto2018 == 2)[1], 'o')
# plt.plot(np.where(lotto2019 == 2)[1], 'x')
# plt.plot(np.where(lotto2020 == 2)[1], 'v')
# plt.plot(np.where(lotto2021 == 2)[1], '+')
# plt.show()

sub = np.where((a1 == 17)[0] & (a1 == 23)[0])
print(np.argwhere(a1 == 17))
print(a1[sub])

plt.plot(np.argwhere(a1 == 17),'o')
plt.plot(np.argwhere(a1 == 23),'x')
plt.show()
