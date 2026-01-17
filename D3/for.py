# for i in range(5):
#     print(i)

# range didalam for itu bisa terima 3 argument dalam int yaitu stop  jika hanya satu argument start dan stop jika terima dua argument start stop  step jiak terima 3 argument
# for i in range(1, 11):
#     print(i)
# # print angka genap dari 0-10 start nya 0 end nya 10 step nya 2
# for i in range(0, 10, 2):
#     print(i)

# tugas print angka 1-100 
for i in range(0, 100):
#print angak genap saja 
    if i == 7:
        break
# jika ketemu angka 7 stop loop
    if i % 2 !=0:
        continue
    print(i)
