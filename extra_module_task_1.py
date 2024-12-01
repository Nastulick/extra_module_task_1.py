students={'Jonny','Bilbo','Steve','Khendrik','Aaron'}
print(students)
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
print(grades)

s=students
print(sorted(s))
aaron_points=[5,3,3,5,4]
a=aaron_points
print('ср.арифметическое Аарона',sum(a)/len(a))
bilbo_points=[2,2,2,3]
b=bilbo_points
print('ср.арифметическое Билбо ',sum(b)/len(b))
jonny_points=[4,5,5,2]
c=jonny_points
print('ср.арифметическое Джони ',sum(c)/len(c))
khendrik_points=[4,4,3]
d=khendrik_points
print('ср.арифметическое Кендрик ',sum(d)/len(d))
steve_points=[5,5,5,4,5]
e=steve_points
print('ср.арифметическое Стив ',sum(e)/len(e))

print(dict([['Aaron',4.0],['Bilbo',2.25],['Jonny',4.0],['Khendrik',3.6666666666666665],['Steve',4.8]]))
