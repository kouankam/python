def multiplication_egyptienne(n,p):
    
    r =0

    while n != 0:

        if n%2 == 1:

            r+=p
        n = n // 2
        p += p
        
    print(r)
    return r
    
n = int(input())
p = int(input())
    
multiplication_egyptienne(n,p)