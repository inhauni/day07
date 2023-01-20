# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def info(self):
#         print(self.name)
#
# class Childeren(Parent):
#     pass
#
#
# c1=Childeren('지현')
# c1.info()


# <데코레이터 이용한 property>

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name=input_name
#     @property # 이미 만들어진 decorator 사용
#     def name(self):
#         print('inside the getter', end=' ')
#         return self.hidden_name # return 이 있는 쪽에 property
#     @name.setter
#     def name(self, input_name): #함수 이름도 set_name에서 name으로 변경
#         print('inside the setter')
#         self.hidden_name=input_name
#     # name = property(get_name,set_name) # property
#
# # don=Duck('Donald')
# # # print(don.get_name())
# # print(don.name)
# # # don.set_name('Donna')
# # don.name='Donna'
# # # print(don.get_name())
# # print(don.name)
#
# fowl=Duck('Howard')
# print(fowl.name)
# fowl.name ='Happy'
# print(fowl.name)

# <맹글링>
# class Duck():
#     def __init__(self, input_name):
#         self.__name=input_name # __name : <맹글링> : 외부코드에서 이 속성을 우연히 발견하는 것을 막아줌\
#                                         # (단, 속성이 private해지는 것은 아님)
#     @property
#     def name(self):
#         print('inside the getter', end=' ')
#         return self.__name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.__name=input_name
#
# fowl=Duck('Howard')
# print(fowl.name)
# fowl.name ='Happy'
# print(fowl.name)
# # print(fowl.__name) -> 바로 접근하는 건 불가능
# print(fowl._Duck__name)  # -> 이런식으로 접근하면 출력은 가능 (완벽한 private이 아니기 때문) ,
#                             # 단 이때 'inside the getter는 출력되지 않음 (속성의 의도적인 접근을 어렵게 만듦)



class Duck():

    color= 'red' # 클래스 속성

    def __init__(self, input_name):
        self.__name=input_name # __name : <맹글링> : 외부코드에서 이 속성을 우연히 발견하는 것을 막아줌\
                                        # (단, 속성이 private해지는 것은 아님)
    @property
    def name(self):
        print('inside the getter', end=' ')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name=input_name

    @staticmethod
    def test():
        return '정적메서드'

    @classmethod
    def ace(cls):
        return '동적메서드'


don=Duck('Donald')

# <클래스메서드, 정적메서드>

# print(Duck.ace(), Duck.test(), don.ace(), don.test()) # 정적method는 따로 객체 생성 없이 'Class.정적method()' 형식으로도 접근가능


# <클래스 속성, 개체 속성>

# print(don.color, Duck.color)
# don.color ='blue'
# print(don.color, Duck.color)
# Duck.color ='green' # 클래스 변수 값 변경
# print(don.color, Duck.color)
# d2= Duck('Induk')
# print(don.color, Duck.color, d2.color)


# < 덕 타이핑>

# EX 1)

class Quote:
    def __init__(self,person,words):
        self.person=person
        self.words=words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

class BabblingBrook(): # 전혀 관계x new class
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'


brook= BabblingBrook()
print(brook.who(), 'says: ',brook.says())  # Quote와 관련 없는 객체이지만 who와 says 메서드를 가지고 있으므로 실행됨

hunter =Quote('emma',"i'm hunting wabbits")
print(hunter.who(), 'says: ', hunter.says())

hunted1=QuestionQuote('jack',"what's up, doc")
print(hunted1.who(), 'says: ', hunted1.says())

hunted2=QuestionQuote('lucy',"hello")
print(hunted2.who(), 'says: ', hunted2.says())

# EX 2
# import math
#
# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def get_area(self):
#         print('도형의 면적을 출력합니다')
#
# class Circle(Shape):
#     def __init__(self,x,y,radius):
#         super().__init__(x,y)
#         self.radius=radius
#
#     def get_area(self): # override
#         return math.pi * self.radius * self.radius
#
# class Rectangle(Shape):
#     def __init__(self,x,y,width,length):
#         super().__init__(x,y)
#         self.width=width
#         self.length=length
#
#     def get_area(self): # override
#         return self.width * self.length
#
#
# class Cylinder(Circle):
#     def __init__(self,x,y,radius,height):
#         super().__init__(x,y,radius)
#         self.height=height
#     def get_area(self): #부피 구하기
#         # return math.pi * self.radius * self.radius * self.height
#         return super().get_area() * self.height
#
# c1=Circle(100,100,10.0)
# c2=Circle(50,50,2.0)
# r1=Rectangle(100,50,5,2)
# cy1=Cylinder(50,20, 10.0,2)
# print(f'원 1의 좌표는 x:{c1.x}, y:{c1.y}이고 넓이는 {c1.get_area():.4f} 입니다.')
# print(f'원 2의 좌표는 x:{c2.x}, y:{c2.y}이고 넓이는 {c2.get_area():.4f} 입니다.')
# print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()} 입니다.')
# print(f'실린더의 좌표는 x:{cy1.x}, y:{cy1.y}이고 부피는 {cy1.get_area():.4f} 입니다.')