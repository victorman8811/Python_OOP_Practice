import random


class Monster:

    def __init__(self, name, health_point, attack, defense):  # 客製化魔物

        self.name = name
        self.health_point = health_point
        self.attack = attack
        self.defense = defense


class Boss:

    def __init__(self, health_point, attack, defense):  # 客製化魔獸

        self.health_point = health_point
        self.attack = attack
        self.defense = defense


goblin = Monster("哥布林", 40, 15, 0)
fire_elf = Monster("火精靈", 80, 15, 35)
evil_wolf = Monster("惡狼犬", 50, 20, 15)


my_monsters = [goblin, fire_elf, evil_wolf]


random.shuffle(my_monsters)  # 隨機打亂魔物出場順序


boss = Boss(220, 30, 0)


print("戰鬥開始!")


def fight(boss, my_monsters):

    turn = 0  # turn是0的話為魔物攻擊，1的話是魔獸攻擊

    for i in range(0, len(my_monsters)):

        print(my_monsters[i].name + "上場!")

        while my_monsters[i].health_point > 0:

            if turn == 0:

                if boss.defense > 0:

                    boss.defense = boss.defense - my_monsters[i].attack

                    if boss.defense < 0:

                        boss.defense = 0
                        boss.health_point = boss.health_point - \
                            (my_monsters[i].attack - boss.defense)

                else:
                    boss.health_point = boss.health_point - \
                        my_monsters[i].attack

                    if boss.health_point < 0:

                        boss.health_point = 0

                print("對敵方進行攻擊，敵方所剩血量 ", boss.health_point, "，護盾 ", boss.defense)

                turn = 1

                if boss.health_point == 0:

                    print("戰鬥勝利!")

                    return  # 魔獸血量歸零時，跳出函式

            if turn == 1:

                if my_monsters[i].defense > 0:

                    my_monsters[i].defense = my_monsters[i].defense - \
                        boss.attack

                    if my_monsters[i].defense < 0:

                        my_monsters[i].defense = 0
                        my_monsters[i].health_point = my_monsters[i].health_point - \
                            (boss.attack - my_monsters[i].defense)

                else:
                    my_monsters[i].health_point = my_monsters[i].health_point - boss.attack

                    if my_monsters[i].health_point < 0:

                        my_monsters[i].health_point = 0

                print("敵方襲擊猛烈，"+my_monsters[i].name+"所剩血量 ",
                      my_monsters[i].health_point, "，護盾 ", my_monsters[i].defense)

                turn = 0

    print("戰鬥失敗!")


fight(boss, my_monsters)
