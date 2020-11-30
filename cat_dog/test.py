'''
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
用捉老鼠的方法调
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、将数据配置到yaml文件里
'''
import yaml


class Animal:
    name = ''
    color = ''
    age = 0
    gender = ''

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print(self.name + '会叫')

    def run(self):
        print(self.name + '会跑')


class Cat(Animal):

    def __int__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def shout(self):
        print(self.name + '在喵喵叫')

    hair = '短发'

    def skill(self):
        print(self.name + '会捉老鼠')

    def catch(self):
        print(f'猫猫的名字是{self.name},颜色是{self.color},年龄是{self.age}岁,'
              f'性别是{self.gender},毛发是{self.hair},捉到了老鼠')
        self.skill()
        self.shout()


class Dog(Animal):
    hair = '长发'

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def shout(self):
        print(self.name + '在汪汪叫')

    def skill(self):
        print(self.name + '会看家')

    def watch(self):
        print(f'狗狗的名字是{self.name},颜色是{self.color},年龄是{self.age}岁,'
              f'性别是{self.gender},毛发是{self.hair}')
        self.shout()
        self.skill()


if __name__ == '__main__':
    with open('attribute.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)

    cat = datas['use']
    dog = datas['use1']

c = Cat(cat['name'], cat['color'], cat['age'], cat['gender'])
c.catch()
d = Dog(dog['name'], dog['color'], dog['age'], dog['gender'])
d.watch()
