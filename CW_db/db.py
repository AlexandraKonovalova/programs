import sqlite3

with open('nanai.csv', 'r', encoding='utf-8') as f:
    f = f.readlines()

# подключаемся к базе данных
conn = sqlite3.connect('example.db')

# создаем объект "курсор", которому будем передавать запросы
c = conn.cursor()

# создаем таблицу
c.execute("DROP TABLE IF EXISTS nanai")
c.execute("CREATE TABLE IF NOT EXISTS nanai(dictor text, sex text, village text, sound text, f1 float, f2 float)")

for row in f:
    row = row.split(';')
    c.execute("INSERT INTO nanai VALUES (?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5]))

# сохраняем изменения
conn.commit()

for i in c.execute("SELECT * FROM nanai WHERE village='Dzhuen' AND sex='m' AND sound='i'"):
    print(i)

# отключаемся от БД
conn.close()