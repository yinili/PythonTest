'''
掷骰子
1、欢迎进入XXXX游戏
2、输入用户名，默认用户是没有币
3、提示用户充值买币（100块钱30个币，充值必须是100的倍数，充值不成功可以再次充值）
4、玩一局游戏扣除2个币，猜大小
5、猜对奖励1个币，可以继续玩（提示想不想继续玩），也可以没有金币自动退出
'''
import  random

print('*'*10)
print('欢迎进入掷骰子游戏')
print('*'*10)

name = input('请输入玩家姓名:')
money = 0

answer = input('确定进入游戏吗？(y/n)')

if answer=='y':
    # 判断游戏币是否充足
    # 做到反复充值
    while money<2:
        n = int(input('金币不足，请充值（100块钱30个币，充值必须是100的倍数，充值不成功可以再次充值）'))
        # 充值金额判断
        if n%100==0 and n>0:
            money=(n//100)*30

    print(f'当前剩余游戏币：{money}，玩一局游戏扣除2个币')

    print('--------->开始游戏')

    # 模拟骰子的值
    while True:
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)
        money-=2
        print('系统洗牌完毕，请猜大小')

        guess = input('请输入大或者小')

        # 判断
        if ((t1+t2)>6 and guess =='大') or ((t1+t2)<=6 and guess =='小'):
            print(f'恭喜{name}! 本局游戏获得奖励1个游戏币')
            money+=1
        else:
            print('很遗憾！本局游戏输了o(╥﹏╥)o')

        answer = input('是否再来一局游戏，要扣除2枚游戏币？(y/n)')
        if answer != 'y' or money <2:
            break

else:
    print('退出游戏！再见！')

