
#How to override class methods in Python?
    class Parent(object):
        def __init__(self):
            self.value = 4
        def get_value(self):
            return self.value
    
    class Child(Parent):
        def get_value(self):
            return self.value + 1
    
    Now Child objects behave differently

    >>> c = Child()
    >>> c.get_value()
    5

#class inheritance python class function override
    class Country:
        """Super Class"""

        name = '국가명'
        population = '인구'
        capital = '수도'

        def show(self):
            print('국가 클래스의 메소드입니다.')


    class Korea(Country):
        """Sub Class"""

        def __init__(self, name):
            self.name = name

        def show_name(self):
            print('국가 이름은 : ', self.name)

#메소드 오버라이딩 (Method overriding)
    class Korea(Country):
        """Sub Class"""

        def __init__(self, name,population, capital):
            self.name = name
            self.population = population
            self.capital = capital

        def show(self):
            print(
                """
                국가의 이름은 {} 입니다.
                국가의 인구는 {} 입니다.
                국가의 수도는 {} 입니다.
                """.format(self.name, self.population, self.capital)
            )
        ... 생략

#부모 메소드 호출하기   
    class Korea(Country):

        ... 생략

        def show(self):
            super().show()
            print(
                """
                국가의 이름은 {} 입니다.
                국가의 인구는 {} 입니다.
                국가의 수도는 {} 입니다.
                """.format(self.name, self.population, self.capital)
            )

        ... 생략