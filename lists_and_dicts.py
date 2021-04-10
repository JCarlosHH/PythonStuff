def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname":"Carlos", "lastname":"Hernandez"}

    super_list = [
        {"firstname":"Richard", "lastname":"Hendricks"},
        {"firstname":"Erlich", "lastname":"Bachman"},
        {"firstname":"Nelson", "lastname":"Bighetti"},
        {"firstname":"Bertram", "lastname":"Gilfoyle"},
        {"firstname":"Jared", "lastname":"Dunn"}
    ]

    supe_dict = {
        "natural_nums" : [1,2,4,5],
        "intenger_nums" : [-1,-2,0,1,2],
        "floating_num" : [1.1,1.4,1.5]
    }

    for row in super_list:
        for key, value in row.items():
            print(key, "-", value)


def challenge_1():
    natural_list= []
    for row in range(100):
        row += 1
        natural_list.append(row**2)
    print(natural_list)


def challenge_1_1():
    natural_list= []
    for row in range(100):
        row += 1
        if row%3  != 0:
            natural_list.append(row**2)
    print(natural_list)

    # List comprehensions
    # We use compressions list to create new lists
    # [element for element in iterable if condition]

    list_comprehension = [row**2 for row in range(1,101) if row%3  != 0]
    print(list_comprehension)

    # Challenge 
    list_comp_challenge = [row for row in range(1,100000) if (row%4  == 0 and row%6  == 0 and row%9  == 0)]
    print(list_comp_challenge)


if __name__ == '__main__':
    challenge_1_1()