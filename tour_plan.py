X,Y,Z=map(int,input().split())
if Z<=50:
    print(X)
else:
    Z=Z-50
    cost=Z*Y
    total=X+cost
    print(total)
