from typing import Any

class folder1class:
    def __init__(self) -> None:
        pass

    def folder1_fcn(self):
        print('folder1 function')

if __name__ == "__main__":
    
    #__package__ is used to support relative imports for main modules.
    if __package__ is None:
        import sys
        from os import path
        cur_path = path.abspath(__file__)

        # ../..
        exec_path = path.dirname( path.dirname(cur_path))         
        print(f'{__package__=}\n{exec_path=}')
        sys.path.append(exec_path)
		
    # 도트(.) 연산자를 사용해 import하는 경우 가장 마지막 항목은 반드시 모듈이거나 패키지여야 한다.
    # __main__에서는 절대 path로 import 되어야 한다.        
    from folder2 import folder2_test
    from folder2.folder3 import folder3_test

    for arg in sys.argv:
        print(arg)

    f2class = folder2_test.folder2class()
    f2fcn = f2class.folder2_fcn()

    f3class = folder3_test.folder3class()
    f3fcn = f3class.folder3_fcn()



