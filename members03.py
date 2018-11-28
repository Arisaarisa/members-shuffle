import random

def main():
    f = open("members02.txt", mode='r')

    members = f.read()
    #
    members_list = members.split("\n")
    #
    # def shafull_tabele(members,)


#
    tables = ["Table1", "Table2", "Table3"]
#
    for table_name in tables:
        shuffle_member = random.shuffle(members_list,3)
        # print(f"{table_name}:{shuffle_member}")
        if shuffle_member == 6:
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


    f.close()
if __name__ == "__main__":
    main()
