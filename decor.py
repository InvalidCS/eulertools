'''
Author: Christopher DiPalma
Description: A collection of useful decorators
'''

class Memoize:
    '''An implementation of memoization.'''
    def __init__(self,f):
        self.f = f
        self.cache = {}
        self.prev = 0
    
    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        ans = self.f(*args)
        self.cache[args] = ans
        return ans
    
    def __getattr__(self,attr):
        return getattr(self.f,attr)
    
    def reset_cache(self, partial: bool=False):
        '''
        Executes either a soft or hard reset on the cache. A soft reset appends '._prev' to
        all currently existing caches and resets self.cache to {}. A hard reset will reset all caches
        including previously saved ones.
        Note: I am planning on trying to implement this with a deque instead for potential
        speed improvement (I don't know if that works, but we'll see)
        '''
        if not partial:
            prev_as_str = ''
            for _ in range(self.prev+1):
                exec(f"self.cache{prev_as_str} = {{}}")
                prev_as_str += '_prev'
            self.prev = 0
        else:
            prev_as_str = '_prev'*self.prev
            for _ in range(self.prev+1):
                exec("self.cache{}_prev = self.cache{}".format(prev_as_str,prev_as_str))
                prev_as_str = prev_as_str[:-5]
            self.cache = {}
            self.prev += 1

if __name__ == '__main__':
    # Testing Memoize
    @Memoize
    def fibonacci(N):
        if N in [0,1]:
            return 1
        return fibonacci(N-1)+fibonacci(N-2)
    
    print(fibonacci.cache)
    print(fibonacci(100))
    print(fibonacci.cache)
    fibonacci.reset_cache(partial = True)
    print(fibonacci.cache_prev)              #Shouldn't fail
    try:    print(fibonacci.cache_prev_prev) #Should fail
    except: print('Previous line raised expected error')
    fibonacci.reset_cache()
    print(fibonacci.cache_prev)
    print(fibonacci.cache)
    