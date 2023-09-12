def dectobin16(n):
    s=[False]*16
    if n<0:
        s[0]=True
        n=32768-n
        for i in range(15,-1,-1):
            if 1==n%2:
                s.append(True)
            else:
                s.append(False)
            n//=2
    else:
        s[0]=False
        for i in range(15,-1,-1):
            if 1==n%2:
                s[i]=True
            else:
                s[i]=False
            n//=2
    return s
def dectobin4(n):
    s=[False]*4
    for i in range(3,-1,-1):
        if 1==n%2:
            s[i]=True
        else:
            s[i]=False
        n//=2
    return s
def arraytoint(n,s):
    a=0
    for i in range(0,s):
        a+=int(n[i])*(10**(s-i))
    return a
def address(n):
    s=[]
    if n[0]=="p":
        s.append(True)
    else:
        s.append(False)
    for i in dectobin4(arraytoint(n[1:],2)):
        s.append(i)
    return s
def func(n):
    pass

    
