import random


def main():
    f = open("members02.txt", mode="r")
    members_txt = f.read()

    members_list = members_txt.split("\n")


    table = ["Table1","Table2","Table3"]
    print(random.sample(members_list, 6))
        # if members_list.remove(shuffle_member):
        #     print(members_list)
        # elif members_list.remove():
        #
    members_list.remove(members_list)
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
