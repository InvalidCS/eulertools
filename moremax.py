
def mcsum(arr: list) -> int:
    '''
    Returns the maximum contiguous sum within a list. Uses Kadane's algorithm.
    Will raise an error on lists of length 0.
    '''
    assert len(arr) > 0, "Length of list is zero"
    maxtotal = maxhere = arr[0]
    for i in range(len(arr)):
        if i == 0:  continue
        maxhere = max(maxhere+arr[i], arr[i])
        if maxhere > maxtotal:
            maxtotal = maxhere
    return maxtotal
        

if __name__ == '__main__':
    print(mcsum([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(mcsum([-2,-3,-2,-4,-9,-6,-7]))
