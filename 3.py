f = open('1.txt')
cnt=0

for i in range(16000):
    mas = [int(i) for i in f.readline().split()]
    mas.sort()
    if mas[0]==mas[1] and mas[2]==mas[3] and (mas[0]**2+mas[2]**2)%2==0:
        cnt+=1
print(cnt)
  
