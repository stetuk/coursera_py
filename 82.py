"""  total=0
count=0
# while True:
#     inp=input('Enter a number: ')
#     if inp=='done': break
#     i=float(inp)
#     total +=i
#      count +=1
#     average = total / count
# """

p=list()
while True:
    inp=input('Enter a number: ')
    if inp=='done' : break
    d=float(inp)
    p.append(d)
    average=sum(p) / len(p)
    print ('Average: ', average)