# 定义工资查询模块 select_money，用来展示工资数额

from tast import money
from tast.money import save_money


def select_money():
    final_money = money.save_money
    if final_money == 2000:
        print(f'发工资了，当前工资余额为{final_money}')
    else:
        print(f'没发工资，当前工资余额为{save_money}')
