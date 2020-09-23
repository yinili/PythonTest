'''
游戏：
1、选择人物
2、购买武器、金币
3、打仗 赢得金币
4、选择删除武器
5、查看武器
6、退出游戏
'''

print('*'*30)
print('欢迎进入王者荣耀')
print('*'*30)

coins = 1000
weapon_list = []
role = input('请输入想要选择的游戏角色：1、鲁班 2、后裔 3、貂蝉 4、妲己 5、诸葛亮 6、曹操：')
print('欢迎{1}来到王者荣耀，当前金币是：{0}'.format(coins,role))

import random

while True:
    choice = int(input('请选择：\n 1、购买武器\n 2、进入对战\n 3、删除武器\n 4、查看武器\n 5、退出游戏\n'))

    if choice ==1:
        # 购买武器
        print('欢迎来到武器商店：')
        weapons = [['影刀',500],['利刃',400],['战靴',500],['护甲', 1000],['手榴弹',800],['鹅毛扇',700]]
        for weapon in weapons:
            print(weapon[0],weapon[1], sep=' ')

        # 提示输入要购买的武器
        weaponname = input('请输入要购买的武器名称：')
        # 判断：1、原来是否购买过武器 2、输入的武器名称是否存在武器库
        if weaponname not in weapon_list:
            for weapon in weapons:
                if weaponname == weapon[0]:
                    # 判断金币数量 并购买武器
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        weapon_list.append(weapon[0])
                        print('{}购买武器{}成功'.format(role,weaponname))
                    else:
                        print('金币不足，请参加对战挣金币！')
                        break
                else:
                    print('输入的武器名称不在武器库内！')
        else:
            print('已经拥有该武器')

    elif choice ==2:
        print('进入战场........')
        if len(weapon_list) > 0:
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                choice_weapon = input('请选择：')
                if choice_weapon in weapon_list:
                    # 进入战斗 默认和张飞对战
                    ran1 = random.randint(1,20) # 张飞随机数
                    ran2 = random.randint(1,20) # role 随机数
                    if ran1 > ran2:
                        print('对战失败')
                    else:
                        print('对战胜利')
                        coins += 200
                        print('当前金币数量：', coins)
                    break
                else:
                    print('输入有误，请重新选择！')
        else:
            print('没有武器，请先购买武器！')
    elif choice ==3:
        # 删除武器
        if len(weapon_list) >0:
            print('武器太多，很沉，扔几个.......')
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)

            while True:
                del_weaponname = input('请输入要删除的武器名称：')
                if del_weaponname in weapon_list:
                    # 删除武器,并退款
                    weapon_list.remove(del_weaponname)
                    for weapon in weapons:
                        if del_weaponname == weapon[0]:
                            coins += weapon[1]
                            break
                    break
                else:
                    print('武器名称输入错误，请重新输入！')
        else:
            print('武器库内没有武器，无法删除')
    elif choice ==4:
        print('{}拥有的武器如下：'.format(role))
        for weapon in weapon_list:
            print(weapon)
    elif choice ==5:
        answer = input('确定要离开游戏吗？（y/n）')
        if answer == 'y':
            break
    else:
        print('输入有误，请重新选择！')