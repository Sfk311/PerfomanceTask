n = int(input("Введите число n"))
m = int(input("Введите число обхода m"))

if n <= m:
    print("n не может быть меньше либо равно m")
    while n <= m:
        m = int(input("Введите число обхода m "))
a = ''
for i in range(1, n + 1):
    a += str(i)
end = -1

open = a[0]
start = 0
space = ''
end_1 = m

while open != end:
    space += a[start]
    end = a[end_1]
    a += a
    start += m -1
    end_1 = start + m -1
print(space)