t = int(input())
inp = []
while t>0:
    m = int(input())
    inp.append(m)
    t -= 1
 
out = []
for n in inp:
    flagAparna = True
    first_n = n
    if(first_n == 1):
        out.append("Sheetal")
    while(n>1 and first_n != 1):
        if n&n-1 == 0:
            n -= int(n/2)
        else:
            #find previous power of 2
            x = int(n)
            while(x&x-1):
                x = x&x-1
            n -= x
        if(n>1):
            if(flagAparna == True):
                flagAparna = False
            else:
                flagAparna = True
    if(first_n != 1):
        if(flagAparna):
            out.append("Arpana")
        else:
            out.append("Sheetal")
            
print(*out, sep="\n")
