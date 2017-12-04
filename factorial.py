def fac(n):
    if n<0:
        raise ValueError("Sorry... I haven't gotten around to implementing negative values for factorials yet. Please try again later.")
    elif n<2:
        return 1
    else:
        #Naive multiplication (find something more efficient later)
        f=1
        for i in range(n,1,-1):
            f*=i
        return f
