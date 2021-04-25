set1=set()
set2=set()
set3=set()
set1={10,150,6,32,28}
set2={32,200,15,10,3}
set3=set1|set2
print(set3)
set3.pop()
print(set3)
print(f'Maximum- {max(set3)}\nMinimum- {min(set3)}\nLength- {len(set3)}')
set4=set3.copy()
for i in range(1000,5000,1500):
    set4.add(i)
print(set4)
set1.clear()
set2.clear()
set3.clear()

