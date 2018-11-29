import random


def main():
    f = open("members02.txt", mode="r")
    list = f.read().splitlines()

    member_1 = random.sample(list, 6)
    print(member_1)

    new_l_1 = [str(member_1) for member_1 in list if not len(member_1) % 6 == 0]
    # print(new_l_1)

    member_2 = random.sample(new_l_1, 5)
    print(member_2)

    new_l_2 = [str(member_2) for member_2 in new_l_1 if not len(member_2) % 5 == 0]

    # print(new_l_2)

    member_3 = random.sample(new_l_2, 4)
    print(member_3)

    table = ["Table1", "Table2", "Table3"]
    # print(random.sample(members_list, 6))
    # if members_list.remove(shuffle_member):
    #     print(members_list)
    # elif members_list.remove():
    #
    # members_list.remove(members_list)
    #
    # print(random.sample(members_list,4))
    # shuffle_members2=random.randrange(members_list,6)
    # shuffle_members3=random.sample(members_list,6)

    # print(f"Table1:{shuffle_members2}")
    # print(f"Table1:{shuffle_members3}")

    # shuffle_members2 = set(shuffle_members1)
    # print(shuffle_members2)

    #
    f.close()


if __name__ == "__main__":
    main()
