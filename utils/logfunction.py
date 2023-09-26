from functools import wraps
import inspect

def mylog(logger, level):
    lineno = inspect.getframeinfo(inspect.currentframe().f_back).lineno + 1
    def wrapper(func):
        func_name = func.__name__
        @wraps(func)
        def decorator(*args,**kwargs):
            logger.log(level,f'[{lineno}]---start({func_name}) {args} {kwargs}')
            result = func(*args,**kwargs)
            logger.log(level,f'---end({func_name}) {result}')
            return result
        return decorator
    return wrapper