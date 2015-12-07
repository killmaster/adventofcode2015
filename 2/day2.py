import heapq
total = 0
totalribbon = 0

f = open('day2input.txt','r')

for line in f:
    splitline = line.split('x')
    l = int(splitline[0])
    w = int(splitline[1])
    h = int(splitline[2])
    """wrapping paper"""
    a1 = l*w
    a2 = w*h
    a3 = h*l
    a4 = min(a1,a2,a3)
    area = 2*a1 + 2*a2 + 2*a3 + a4
    total += area
    #print("area: "+str(area)+" extra: "+str(a4)+" total: "+str(total))
    """ribbon"""
    smallest = min(l,w,h)
    second_smallest = heapq.nsmallest(2,[l,w,h])[1]
    wrapping_ribbon = 2*smallest+2*second_smallest
    bow = l*w*h
    totalribbon += wrapping_ribbon+bow

print(total)
print(totalribbon)
