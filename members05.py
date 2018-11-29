import random


# class shuffle_m   embers
def main():
    with open("members02.txt", mode="r") as f:
        lists = f.read().splitlines()

        # members = lists.split("\n")
        member_1 = random.sample(lists,6)
        print(f"Table1:{member_1}")
        for l in range(0,len(member_1)):
            lists.remove(member_1[l])

        member_2 = random.sample(lists,5)
        print(f"Table2:{member_2}")
        for l in range(0,len(member_2)):
            lists.remove(member_2[l])

        member_3 = lists
        print(f"Table3:{member_3}")






    f.close()


if __name__ == "__main__":
    main()
