fname='mbox-short.txt'#= input("Enter file name: ")
with open (fname,'r') as fn:
    lst=list()
    count=0
    for line in fn:
          line=line.rstrip()
          if not line.startswith('From ') :  
               continue
          count+=1
          words=line.split()
          w=words[1]
          lst.append(w)
          print (w)
    print (count)
    print(len(lst))
    print(lst)
