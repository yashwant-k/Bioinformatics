import random
integer=int(input("Enter the length of motif"))
file=open("mot.txt","r")
r=file.read()
print("Sequence",r)
size=len(r)
print("size of the sequence",size)
pos=random.randint(0,len(r)-5)
print("position",pos)
motif=r[pos:pos+1]
print("Motif",motif)
i=pos+1
while(i<=size-1):
        if(motif==r[i:i+1]):
                str1=r[i:i+1]
                print("match motif",str1)
                file1=open("motoutput.txt","a")
                file1.write(str1+"")
i+=1
