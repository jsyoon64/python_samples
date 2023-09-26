from typing import Any

class folder2class:
    def __init__(self) -> None:
        pass

    def folder2_fcn(self):
        print('folder2 function')

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        cur_path = path.abspath(__file__)
        # ../..
        exec_path = path.dirname( path.dirname(cur_path) )
        print(f'{__package__=}\n{exec_path=}')
        sys.path.append(exec_path)
		
    # 도트(.) 연산자를 사용해 import하는 경우 가장 마지막 항목은 반드시 모듈이거나 패키지여야 한다.
    # __main__에서는 절대 path로 import 되어야 한다.           
    from folder1 import folder1_test

    for arg in sys.argv:
        print(arg)

    f1class = folder1_test.folder1class()
    f1fcn = f1class.folder1_fcn()