class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
# myid_add:
#    - '正整数相加'
#    - '负整数相加'
#    - '小数相加'
#    - '正数与负数相加'
#
# div:
#    - [10,10,1]
#    - [-10,-10,1]
#    - [10,-10,-1]
#    - [0.4,0.2,0.2]
#    - [6,0,'除数不能为零']
#    - [0,2,0]
#
# myid_div:
#    - '正整数相除'
#    - '负整数相除'
#    - '正数与负数相除'
#    - '小数相除'
#    - '被除数为0'
