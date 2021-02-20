set1=list(input("Enter the 1st Sequence-->  "))
set2=list(input("Enter the 2nd Sequence-->  "))
score=[]
def Pairwise_alignment(a,b):
    gap(a,b)
    print(a)
    print(b)
    value=0
    length=len(a)
    for i in range(0, length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    print(score)
    print(value)
    
def gap(a,b):
    while len(a)!=len(b):
        if(len(a)==len(b)):
            print()
        else:
            k=int(input('Enter the position to insert-->  '))
            if(len(a)>len(b)):
                b.insert(k,'-')
            else:
                a.insert(k,'-')    
    return(a,b)
Pairwise_alignment(set1,set2)
