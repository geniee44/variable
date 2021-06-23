import pymysql
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

connection = pymysql.connect(host='localhost', user='root', password='pw', db='artdb', charset='utf8mb4', autocommit=True)

cursor = connection.cursor(pymysql.cursors.DictCursor)
sql = "SELECT Genre, COUNT(*) AS Num FROM CONCERT WHERE StartDate > 20210000 GROUP BY Genre ORDER BY Num"
cursor.execute(sql)

x = np.arange(5)
genre = []
num = []

rows = cursor.fetchall()
for row in rows:
    for value in row.values():
        if type(value) == str:
            genre.append(value)
        elif type(value) == int:
            num.append(value)

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'gulim'

plt.bar(x, num, width=0.5, color='skyblue')
plt.xticks(x, genre)
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
plt.title("2021년 서울시 예술단 장르별 공연 수")
plt.ylabel('<공연 수>')
plt.xlabel('<장르>')
plt.show()
