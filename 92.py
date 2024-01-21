fname = ('mbox-short.txt')#input("Enter file name: ")
with open (fname,'r') as fn:
    counts=dict()
    lst=list()
    for line in fn:
          if not line.startswith('%@% ') :  
               continue
          words=line.split()
          lst.append(words) 
    print(words)