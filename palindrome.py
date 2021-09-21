pac =[]

while 1 :

    num = input()
    if num == '0':
        break
    pac.append(num)

result=[]

for num2 in pac :
    res = True
    for i in range(len(num2)//2):
        if num2[i] !=num2[-1-i]:
            res=False
            break
        
    if res == True:
        result.append('yes')
    else :
        result.append('no')

for num3 in result :
    print(num3)
