l = [1, 5, 6.3, 6, None, 2.0, -4, None]
s = 0
for i in l:
    if i != None:
        s += i
aver = s / len(l)
print(aver)
for i in range(len(l)):
    if l[i] == None:
        l[i] = aver
print(l)
    
  
