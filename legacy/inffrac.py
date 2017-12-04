def fracgen(firstnum: int, series: list, numiter: int) -> [int, int]:
    '''Returns numerator and denominator for fraction.'''
    if numiter == 1:
        return [firstnum, 1]
    s_len = len(series)
    index = (numiter - 2)%s_len
    numer = 1
    denom = series[index]
    for i in range(1,numiter-1):
        numer += series[(index-i)%s_len]*denom
        temp = numer
        numer = denom
        denom = temp
    numer += firstnum*denom
    return [numer,denom]

def eseries(n: int) -> list:
    '''Returns a list usable to calculate the nth convergent for e.'''
    completeloop = n//3
    partial = n%3
    elist = []
    for i in range(completeloop):
        elist += [1,2*(i+1),1]
    for x in range(partial):
        if not x == 1:
            elist += [1]
        else:
            elist += [2*(completeloop+1)]
    return elist
