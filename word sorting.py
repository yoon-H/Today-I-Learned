word = []
n = int(input())

for i in range (n) :
    a = input()
    word.append(a)


word1=set(word)

word2=list(word1)

word2.sort(key=len)

for i in word2 :
    print(i)
