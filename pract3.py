set1=input("Enter the 1st Sequence-->  ")
set2=input("Enter the 2nd Sequence-->  ")
similarity_calculation=int(input('Type the no. of element for similarity calculation-->  '))
similarities=[]
for i in range(0,similarity_calculation):
    element=input('Enter an Element-->  ')
    similar_element=int(input('No. of element it is similar-->  '))
    similarities.append([])
    similarities[i].append(element)

    for j in range(0,similar_element):
        b=input('What is it similar to-->  ')
        similarities[i].append(b)
        
def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score=score+1
    similarity=(score*100)/len(o)
    return similarity

print(compare(list(set1),list(set2),similarities),'%')

