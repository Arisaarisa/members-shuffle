import random


def main():
    f = open("members02.txt", mode="r")
    members_txt = f.read()
    members_list = members_txt.split("\n")

    shuffle_members = random.sample(members_list, k=6)

    table_list = ["Table1", "Table2:", "Table3:"]

    for table in table_list:
        for shuffle_member in shuffle_members:
            print(f"{table}{shuffle_member}")

    f.close()


if __name__ == "__main__":
    main()
