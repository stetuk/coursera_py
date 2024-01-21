
fname = input("Enter file name: ")
with open (fname,'r') as fn:
    lst=list()
    for line in fn:
        words=line.split()
        for word in words: 
          lst.append(word)  
    y=set(lst)            
    u=sorted(y)           

    print(u)
    #print(set(lst))
   # print(len(lst), len(set(lst)))
  