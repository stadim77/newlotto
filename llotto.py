filename = ['lotto_2018.xlsx', 'lotto_2019.xlsx', 'lotto_2020.xlsx', 'lotto_2021.xlsx']

ans = 3
# wb = load_workbook(filename[ans])
data = pd.read_excel(filename[ans])
df1 = data.dropna()

print(df1)
