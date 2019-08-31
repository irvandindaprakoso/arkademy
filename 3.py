prime = []
for num in range(2,30):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        prime.append(num)

inp = int(input("Masukkan panjang alas: "))
if inp>0 and inp < 10:
    for i in range(1,inp+1):
        print(prime[:i])
else:
    print("Silahkan coba lagi dengan rentang nilai 1 - 9")