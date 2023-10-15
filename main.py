# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    favorite_num = 55
    print(f"我最喜欢的数是：{favorite_num}!")  # ）


def func():
    lis = ['a', 'b', 'c']
    print(lis)
    lis.insert(0, 'd')
    print(lis)
    lis_popped = lis.pop()
    print(lis)
    lis.pop(0)
    print(lis)
    print(lis_popped)

    # 修改/添加（append、insert）/删除（del、pop、remove）


def func():
    dinner = ['a', 'b', 'c']
    name1 = dinner[0]
    name2 = dinner[1]
    name3 = dinner[2]
    print(f"{name1}和{name2}，吃晚饭？{name3}无法赴约")
    dinner[2] = 'd'
    name3 = dinner[2]
    print(f"{name3}，吃晚饭?")
    # print(f"{name1}和{name2}，吃晚饭？")
    dinner.insert(0, 'e')
    dinner.insert(2, 'f')
    dinner.append('g')
    popped = dinner.pop()
    print(f"{popped},抱歉不能来参加")
    del dinner[0]
    del dinner[0]
    del dinner[0]
    del dinner[0]
    del dinner[0]
    len(dinner)
    # del dinner[3]
    print(dinner)


# 排序 sort/临时排序 sorted/反向排序 reverse/长度len
def func1():
    trip = ['c新疆', 'a深圳', 'b香港', 'f台湾', 'd日本']
    print(trip)
    print(sorted(trip))
    print(trip)
    print(sorted(trip, reverse=True))
    print(trip)
    trip.reverse()
    print('-'.center(100, '-'))
    print(trip)
    trip.reverse()
    print(trip)
    trip.sort()
    trip.sort(reverse=True)
    print(trip)


def func2():
    # for i in range(1,21):
    # print (i)
    # for i in range(1, 1000000):
    # print(i)
    num_list = list(range(1, 1000001))
    print(min(num_list))
    print(max(num_list))
    print(sum(num_list))

    num_list = list(range(1, 20, 2))
    for num in num_list:
        print(num)

    num_list = [3 * i for i in range(1, 11)]
    print(num_list)

    num_list = [i ** 3 for i in range(1, 11)]
    print(num_list)

    print('the first three items in the list are:')
    print(num_list[:3])

    print('the middle  items in the list are:')
    print(num_list[4:7])

    print('the middle  items in the list are:')
    print(num_list[-3:])

    my = ['apple', 'banana', 'orange']
    friends = my[:]
    my.append('egg')
    friends.append('pen')
    print(my)
    print(friends)


# if 语句
def func3():
    alien_color = 'green'
    if alien_color == 'green':
        print("miaomiao get 5 score")

    alien_color = 'red'
    if alien_color != 'green':
        print("miaomiao get 10 score")
    elif alien_color == 'yellow':
        print("miaomiao get 10 score")
    if alien_color == 'red':
        print("miaomiao get 15 score")

    age = 25
    if age < 2:
        print("the person ia a baby")
    elif 2 <= age < 4:
        print("the person is a big baby")
    elif 4 <= age < 13:
        print("the person is a child")
    elif 13 <= age < 18:
        print("the person is a teenager")
    elif 18 <= age < 65:
        print("the person is a big teenager")
    elif 65 <= age:
        print("the person is a older")

    favorate_fruits = ['apple', 'orange', 'banana']
    if 'apple' in favorate_fruits:
        print("you really like apple")
    if 'orange' in favorate_fruits:
        print("you really like orange")
    if 'banana' in favorate_fruits:
        print("you really like banana")

    peoples = ['miaomiao', 'zhangfengming', 'admin', 'jaden', 'miao']
    for people in peoples:
        if people == 'admin':
            print("hello,would you like to see status report")
        elif people != 'admin':
            print(f"hello, {people} thank you for logging in again")
    if not peoples:
        print("we need some users!")

    for people in peoples:
        del peoples[0]
    print(peoples)

    for people in peoples:
        peoples.remove(people)
    del peoples[0]
    print(peoples)


# 字典
def func4():
    person = {'first_name': 'miao', 'last_name': 'qiu', 'age': 25, 'city': 'shanghai'}
    print(person)
    num = {'first_name': 1, 'last_name': 2, 'age': 3, 'city': 4, 'miao': 5}
    print(f" first_name like {num['first_name']}")
    print(f" first_name like {num.get('second_name')}")

    num = {'first_name': 'china', 'last_name': 'egypt', 'age': 'england', 'city': 'japan', 'miao': 'endian'}
    for k, v in num.items():
        print(f"the {k.title()} runs through {v.title()}  ")
    for v in num.values():
        print(v)
    for v in num.keys():
        print(v)

    person = {'first_name': 'miao', 'last_name': 'qiu', 'age': 25, 'city': 'shanghai'}
    person1 = {'first_name': 'miao1', 'last_name': 'qiu', 'age': 25, 'city': 'shanghai'}
    person2 = {'first_name': 'miao2', 'last_name': 'qiu', 'age': 25, 'city': 'shanghai'}
    peoples = [person, person1, person2]
    for people in peoples:
        print(people)


def func5():
    # message = input("tell me something:")
    # print(message)
    # int(message)>int(18)

    # message1 = input("what car you want to find:")
    # print(f"let me see if i can find you a {message1}")

    num = input("what number you want to find:")
    if int(num) % 10 == 0:
        print(f"{num} is yes")
    else:
        print(f"{num} is no")


###while 循环
def func6():
    num = 1
    while num <= 5:
        num += 1
        # print(num)
    pizza_list = []


def func6():
    pizza = "请输入披萨配料："
    message = ''
    while message != 'quit':
        message = input(pizza)
        print(message)


def func7():
    def func():
        if age == 'quit':
            return 0
        elif not age.isnumeric():
            print('年龄应为正整数，且小于200。')
            return 2
        elif int(age) > 200:
            print('年龄应为正整数，且小于200。')
            return 2
        else:
            return 1

    question = '你几岁:'
    active = True
    while active:
        age = input(question)
        if not func():
            active = False
        elif func() == 2:
            pass
        else:
            age = int(age)
            if age < 3:
                price = 0
            elif 3 <= age < 12:
                price = 10
            else:
                price = 15
            print(f"票价是：{price}")
            print(f"年龄是：{age}")


def func8():
    sandwich_orders = ['jirou', 'shuiguo', 'peigen']
    finish_sandwiches = []
    while sandwich_orders:
        finish_sandwich = sandwich_orders.pop()
        print(f"i made your tuna sandwich:{finish_sandwich}")
        finish_sandwiches.append(finish_sandwich)
    for i in finish_sandwiches:
        print(i)
    print(f'finish sandwiches :{", ".join(finish_sandwiches)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    func8()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
