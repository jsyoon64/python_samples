class Singleton(type):
    # 클래스들의 인스턴스를 저장
    __instances = {}

    # def __new__(mcs, *args, **kwargs):
    #     # print('메타클래스 __new__() 호출')
    #     # print(mcs)
    #     instance = super().__new__(mcs, *args, **kwargs)
    #     # print('인스턴스 생성', instance)
    #     # print('--------------------')
    #     return instance

    # def __init__(cls, *args, **kwargs):
    #     # print('메타클래스 __init__() 호출')
    #     # print(cls)
    #     # print('--------------------')
    #     super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        클래스를 인스턴스화 할 때, 호출
        """
        # print('메타클래스 __call__() 호출')
        # print('--------------------')
        # # __instances에 instance가 없으면 생성 후 반환, 존재하면 해당 값을 꺼내서 반환
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        cls.__instances[cls].__init__(*args, **kwargs)
        return cls.__instances[cls]

# 사용 방법
# class Util(metaclass=Singleton):