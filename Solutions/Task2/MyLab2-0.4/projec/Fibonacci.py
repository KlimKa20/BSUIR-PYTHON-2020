class CacheDecorate:

    _func_values_=dict()

    def cache(function):
        def wrapper(*args, **kwargs):
            if CacheDecorate._func_values_.get(function.__name__):
                if CacheDecorate._func_values_[function.__name__][0] == args and\
                        CacheDecorate._func_values_[function.__name__][1] == kwargs:
                    return CacheDecorate._func_values_[function.__name__][2]
            result = 0
            try:
                result = function(*args, **kwargs)
            except Exception:
                try:
                    result = function(*args)
                except:
                    result = function(**kwargs)
            CacheDecorate._func_values_[function.__name__]=(args, kwargs, result)
            return result
        return wrapper


@CacheDecorate.cache
def fib(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return list()
    return fib(n-1) + fib(n-2)


