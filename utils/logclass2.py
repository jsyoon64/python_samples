from functools import wraps
import inspect
import logging
import os

class myLogger(object):
    logger = logging.getLogger('decolog')        
    # print("a")

    @classmethod
    def log(cls,level=logging.INFO):
        # print("b")
        selectedlog = {logging.INFO:cls.logger.info,logging.WARN:cls.logger.warn}.get(level,cls.logger.debug)
        caller_info = inspect.getframeinfo(inspect.currentframe().f_back)
        lineno = caller_info.lineno + 1
        fullname = os.path.basename(caller_info.filename)
        # filename = fullname.split('.',1)
        # # function = os.path.basename(caller_info.function)
        # extrainfo={'decoline':lineno,'deconame':filename[0]}
        extrainfo={'decoline':lineno,'deconame':fullname}
        def wrapper(func):
            def get_function_call_args(func, *args, **kwargs):
                """Return a string containing function name and list of all argument names/values."""
                # func_args = inspect.signature(func).bind(*args, **kwargs)
                # func_args.apply_defaults()
                # func_args_str = ", ".join(f"{arg}={val}" for arg, val in func_args.arguments.items())

                margs = args
                if args and args[0].__class__:
                    margs = args[1:]

                args_repr = [repr(a) for a in margs]
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)

                return f'-start {func.__name__}({signature})', \
                       f'---end {func.__name__}'

            @wraps(func)
            def decorator(*args,**kwargs):
                start_string, end_string = get_function_call_args(func, *args, **kwargs)
                
                selectedlog(f'{start_string}',extra=extrainfo)
                result = func(*args,**kwargs)
                selectedlog(f'{end_string} {result}',extra=extrainfo)
                return result
            return decorator
        return wrapper

    @classmethod
    def setconfig(cls,level=logging.INFO):
        decofmter = logging.Formatter(fmt="%(asctime)s.%(msecs)03d [%(deconame)12s:%(decoline)5d] %(message)s",datefmt="%H:%M:%S")
        decohandler = logging.StreamHandler()
        decohandler.setFormatter(decofmter)
        cls.logger.addHandler(decohandler)
        cls.logger.setLevel(level)
        cls.logger.propagate = False
        cls.logger.disabled = False
        # self.logger.manager.loggerDict['decolog'].disabled = False
        # self.logger.manager.loggerDict['decolog'].propagate = False
        # # self.logger.manager.loggerDict['decolog'].parent.propagate = False

