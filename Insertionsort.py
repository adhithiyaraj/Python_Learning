array=[ -9,7,4,1,0,2]
for i in range(1,len(array)):
    j=i-1
    key=array[i]
    while(j>=0 and array[j]>key):
        array[j+1]=array[j]
        j=j-1
        print(j)
    array[j+1]=key
print(array)