set1=list(input("Enter the 1st Sequence-->  "))
set2=list(input("Enter the 2nd Sequence-->  "))
def find_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score=0
    length=len(a)
    total_element=len(a)*len(b)
    for i in range(0, length):
        for j in range (0, length):
            if(a[i]==b[j]):
                score=score+1
    identity=(score/total_element)*100
    print('Matching Score--> ',score)
    print('Identity of the sequence--> ',identity)
    
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
find_identity(set1,set2)
