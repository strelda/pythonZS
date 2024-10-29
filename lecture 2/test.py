a = 5
b = 9
c = 8
d = 6

def fraction (a:float, b:float, c:float, d:float) -> float:
    """Vynásobíme čitatel"""
    x = a*d+c*b
    return x

def divisor (b:float, d:float) -> float:
    """Vynásobíme jmenovatel"""
    y = b*d
    return y

def nvd(p,q):
    while q != 0:
        p,q = q,p%q
    return p

m=fraction(a,b,c,d)
n=divisor(b,d)
nvd_resault = nvd(m,n)

print(int(m/nvd_resault))
print(int(n/nvd_resault))
