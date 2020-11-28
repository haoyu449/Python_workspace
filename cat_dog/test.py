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

    def __init__(self, n, c, a, g):
        self.name = n
        self.color = c
        self.age = a
        self.gender = g

    def cry(self):
        print(self.name + '会叫')

    def run(self):
        print(self.name + '会跑')


class Cat(Animal):
    def cry(self):
        print(self.name + '喵喵叫')

    def __init__(self, n, c, a, g):  # 复写父类的__init__方法，继承父类的属性，
        super().__init__(n, c, a, g)
        self.hair = '短发'  # 添加一个新的属性，毛发=短毛，

    # def  catch(self):
    #     print(self.name + '会捉老鼠')
    def catch(self):  # 添加一个新的方法， 会捉老鼠，
        print(f'{self.name},{self.color},{self.age}岁,{self.gender},{self.hair},捉到了老鼠')


class Dog(Animal):
    def __init__(self, n, c, a, g):
        super().__init__(n, c, a, g)
        self.hair = '长发'

    def watch(self):
        print(f'{self.name},{self.color},{self.age}岁,{self.gender},{self.hair},会看家')

    def cry(self):
        print(self.name + '汪汪叫')


if __name__ == '__main__':
    with open('attribute.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    # print(datas)
    # cat的配置数据
    name = datas['use']['name']
    age = datas['use']['age']
    color = datas['use']['color']
    gender = datas['use']['gender']
    # dog的配置数据
    name2 = datas['use1']['name']
    age2 = datas['use1']['age']
    color2 = datas['use1']['color']
    gender2 = datas['use1']['gender']
c = Cat(name, color, age, gender)
c.catch()
d = Dog(name2, color2, age2, gender2)
d.watch()
