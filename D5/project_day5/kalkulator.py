expr = "1+2+3-5*6/9"
angka =[]
operator = []

temporary = ''
for c  in expr :
    if c.isdigit():
        temporary+=c
    else:
        angka.append(int(temporary))
        operator.append(c)
        temporary=''
angka.append(int(temporary))
i = 0
while i < len(operator):
    if operator[i] == '*':
        angka[i] = angka[i] * angka[i+1]
    elif operator[i] == '/':
        angka[i] = angka[i] / angka[i+1]
    else:
        i += 1
        continue

    angka.pop(i+1)
    operator.pop(i)
hasil = angka[0]

for i in range(len(operator)):
    if operator[i] == '+':
        hasil += angka[i+1]
    else:
        hasil -= angka[i+1]

print(hasil)
