# 定义一个start.py ，启动文件展示最终存款金额
from tast.select_money import select_money
from tast.send_money import send_money

if __name__ == '__main__':
    send_money()
    select_money()
