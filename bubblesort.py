# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
array=[ 4,2,0,1,-94,100]
sorted=False
while(sorted==False):
    sorted=True
    for j in range(1,len(array)):
        if(array[j-1]>array[j]):
            temp=array[j-1]
            array[j-1]=array[j]
            array[j]=temp
            sorted=False
print(array)