# 1) За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750
# **Output:**
# # 2
n = int(input('Какое расстояние машина проезжает за день? '))
m = int(input('Какова вторая дистанция? '))
time = (m - 1) // n + 1
print(time)
# ===========================================================
# 2) 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32
class1 = int(input('Сколько человек в первом классе? '))
class2 = int(input('Сколько человек во втором классе? '))
class3 = int(input('Сколько человек в третьем классе? '))
tables1 = (class1 + 1) // 2
tables2 = (class2 + 1) // 2
tables3 = (class3 + 1) // 2
print(tables1 + tables2 + tables3)
