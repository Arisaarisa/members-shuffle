import random


def main():
    f = open("members.txt", mode='r')

    text = f.read()

    members = text

    f.close()

    tables = ["Table1", "Table2", "Table3"]
    for table_name in tables:
        if members == 6:
            print(f"{tables[table_name]}{members}")
            members - 6

        if members == 0:
            print("席が確定しました")
            break


#
#     if member == 6:
#         return table[0]
#
#     print(member)
#
#
# #print(f"Table1:{member1}("\n")Table2:{member2}("\n")Table3:{member3}("\n")")


if __name__ == "__main__":
    main()
