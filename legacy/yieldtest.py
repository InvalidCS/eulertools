  #NOTE: This is not a real tool. I just was lazy and didn't want to open the
  #testing folder.

def rec(n):
    for i in range(n):
        yield i*i

if __name__ == '__main__':
    g=rec(15)
    for i in g:
        print(i)
        if i==7:
            break
    for i in g:
        print(i)
