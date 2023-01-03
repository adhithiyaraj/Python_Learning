# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
array=[ 1,4,2,-8,4,23,-98]
for i in range(0,len(array)):
    print(i,"*")
    small=array[i]
    for j in range(i+1,len(array)):
        if(array[j]<small):
            small=array[j]
            index=j
            print(small)
        else:
            {}
    if(small!=array[i]):
        temp=array[i]
        array[i]=small
        array[index]=temp
print(array)
    

i=2
j=3
small=7