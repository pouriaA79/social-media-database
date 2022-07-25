import mysql.connector


def main():
    conn = mysql.connector.connect(
        host="localhost", user="root",
        password="", database="qanari")
    cursor = conn.cursor()
    while True:
        # login_id = 1
        print("1. login")
        print("2. logincheck")
        print("3. daryaft avaye shakhsi")
        print("4. donbal kardan")
        print("5. tavaqof donbal kardan")
        print("6. block")
        print("7. unblock")
        print("8. daryaft faaliat donbal shavandegan")
        print("9. daryaft faaliat karbaran (motefavet ba sql)!!!!!!!!!!!")
        print("10. comment ")
        print("11. daryaft comment ")
        print("12. like ava ")
        print("13. number of like  ")
        print("14. avahaye portarafdar ")
        print("15. payamhaye daryafti karbar ")
        print("16. list ersal konandegan payam")
        print("17. send message ")
        print("18. list pasan konandegan ")
        print("19. avahaye hashtag ")
        print("20. add new user")
        print("21. add ava")
        print("22. add hashtag   (different)")



        decide = input("your choice : ")
        if decide == "1":
            login_info = input("enter your username  and password: ")
            inf = login_info.split(" ")
            info = []
            info.append(inf[0])
            info.append(inf[1])
            info.append("")
            arg = cursor.callproc("login", info)
            print("login successfully")
            login_id = arg[2]
            print(login_id)
            conn.commit()

        elif decide == "2":
            login_info = input("enter your username : ")
            info = ()
            info = info + (login_info,)
            cursor.callproc("logincheck", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            for j in range(len(data)):
                print(data[j][0], end=" ")
                print(data[j][1])
            conn.commit()
        elif decide == "3":
            print("avahaye shakhsi shoma:")
            info = []
            info.append(login_id)
            cursor.callproc("daryaft_avaye_shakhsi", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            print("====================")
            for j in range(len(data)):
                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tdate: ")
                print(data[j][2], end="\tuser_id: ")
                print(data[j][3], end="\tcomment on ava: ")
                print(data[j][4])
            conn.commit()
            print("====================")
        elif decide == "4":
            info = []
            info.append(login_id)
            info.append(int(input("which id yo want to follow: ")))
            cursor.callproc("donbal_kardan", info)
            print("follower_id  followed_id")
            for res in cursor.stored_results():
                data = res.fetchall()
                print(data)
            conn.commit()
            print("follow successfully!")
        elif decide == "5":
            info = []
            info.append(login_id)
            info.append(int(input("which id yo want to unfollow: ")))
            cursor.callproc("tavaqof_donbal_kardan", info)
            print("follower_id  followed_id")
            for res in cursor.stored_results():
                data = res.fetchall()
                print(data)
            conn.commit()
            print("unfollow successfully!")
        elif decide == "6":
            info = []
            info.append(login_id)
            info.append(int(input("which id yo want to block: ")))
            cursor.callproc("block", info)
            print("blocker_id  blocked_id")

            for res in cursor.stored_results():
                data = res.fetchall()
                print(data)
            conn.commit()
            print("block successfully!")
        elif decide == "7":
            info = []
            info.append(login_id)
            info.append(int(input("which id yo want to unblock: ")))
            cursor.callproc("unblock", info)
            print("blocker_id  blocked_id")
            for res in cursor.stored_results():
                data = res.fetchall()
                print(data)
            conn.commit()
            print("unblock successfully!")
        elif decide == "8":
            print("faaliat donbal shavandegan : ")
            info = []
            info.append(login_id)
            cursor.callproc("daryaft_faaliat_donbal_shavandegan", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            print("====================")
            for j in range(len(data)):
                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tdate: ")
                print(data[j][2], end="\tuser_id: ")
                print(data[j][3], end="\tcomment on ava: ")
                print(data[j][4])
            conn.commit()
            print("====================")
        elif decide == "9":
            print("faaliat karbaran : ")
            info = []
            info.append(login_id)
            info.append(int(input("id karbar mored nazar: ")))
            cursor.callproc("faaliat_karbaran", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            print("====================")
            for j in range(len(data)):
                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tdate: ")
                print(data[j][2], end="\tuser_id: ")
                print(data[j][3], end="\tcomment on ava: ")
                print(data[j][4])
            conn.commit()
            print("====================")
        elif decide == "10":

            info = []
            info.append(login_id)
            info.append(int(input("id avaye mored nazar: ")))
            info.append(input("your comment : "))
            cursor.callproc("nazar_dadan", info)
            # for res in cursor.stored_results():
            #     data = res.fetchall()
            #     print(data)
            conn.commit()
            print("done !")
        elif decide == "11":
            info = []
            info.append(login_id)
            info.append(int(input("id avaye mored nazar: ")))
            cursor.callproc("daryaft_comment", info)
            conn.commit()
            for res in cursor.stored_results():
                data = res.fetchall()
            print("====================")
            for j in range(len(data)):
                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tdate: ")
                print(data[j][2], end="\tuser_id: ")
                print(data[j][3], end="\tcomment on ava: ")
                print(data[j][4])

            print("done !")
        elif decide == "12":
            info = []
            info.append(login_id)
            info.append(int(input("id avaye mored nazar: ")))
            cursor.callproc("like_ava", info)
            conn.commit()
            print("done !")
        elif decide == "13":
            info = []
            info.append(login_id)
            info.append(int(input("id avaye mored nazar: ")))
            cursor.callproc("num_like", info)
            for res in cursor.stored_results():
                data = res.fetchall()
                print(data)
            conn.commit()
        elif decide=="14":
            info = []
            info.append(login_id)
            # info.append("12")
            cursor.callproc("avahaye_portarafdar", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            for j in range(len(data)):

                print("id ava: ", end="")
                print(data[j][0], end="\tnum_like: ")
                print(data[j][1])
            conn.commit()
        elif decide=="15":
            info = []
            info.append(login_id)
            # info.append("12")
            info.append(int(input("id sender: ")))
            cursor.callproc("payamhaye_daryafti_karbar", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            for j in range(len(data)):

                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tsender_id: ")
                print(data[j][2], end="\tdate: ")
                print(data[j][3])
            conn.commit()
        elif decide =="16":
            info = []
            info.append(login_id)
            # info.append("12")
            cursor.callproc("list_ersal_konandegan_payam", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            for j in range(len(data)):

                print("sender: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tid_ava: ")
                print(data[j][2], end="\tdate: ")
                print(data[j][3])
            conn.commit()
        elif decide == "17":
            info = []
            info.append(login_id)
            choice = input("enter 1 for ava and 2  for mahtavye matni:")
            date =input("enter date" )
            receive = int(input("id receiver: "))
            info.append(date)
            info.append(receive)
            if choice =="1":
                info.append(int(input("id ava: ")))
                info.append(1)
                info.append("")
                cursor.callproc("send_message", info)
                conn.commit()
            elif choice =="2":
                info.append("")
                info.append(2)
                info.append(input("matn payam :"))
                cursor.callproc("send_message", info)
                conn.commit()
        elif decide == "18":
            info = []
            info.append(login_id)
            info.append(int(input("id ava: ")))
            cursor.callproc("list_pasankonandegan", info)

            for res in cursor.stored_results():
                data = res.fetchall()
            print("usernames:")
            for j in range(len(data)):
                print(data[j])


            conn.commit()
        elif decide =="19":
            info = []
            info.append(login_id)
            info.append(int(input("id hashtag: ")))
            cursor.callproc("avahaye_hashtag", info)
            for res in cursor.stored_results():
                data = res.fetchall()
            for j in range(len(data)):

                print("id ava: ", end="")
                print(data[j][0], end="\tmohtava: ")
                print(data[j][1], end="\tpost date: ")
                print(data[j][2], end="\tuser_id: ")
                print(data[j][3], end="\tcomment on ava: ")
                print(data[j][4])

            conn.commit()
        elif decide == "20":
            info = []
            info.append((input("first name: ")))
            info.append((input("last name: ")))
            info.append((input("username: ")))
            info.append((input("password: ")))
            info.append((input("birthday: ")))
            info.append((input("biography: ")))
            cursor.callproc("add_user", info)
            conn.commit()
        elif decide ==  "21":
            info = []
            info.append(login_id)
            info.append(input("mohtava: "))
            cursor.callproc("add_ava", info)
            conn.commit()
        elif decide == "22":

            info = []
            info.append(login_id)
            info.append(input("mohtava: "))
            info.append("")
            info.append(input("hashtag : "))
            cursor.callproc("aadd_hashtag", info)
            conn.commit()








if __name__ == "__main__":
    main()
