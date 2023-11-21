import random
done = False
km_traveled = 0
thirst = 0
camel_tired = 0
oasis = 0
police_traveled = -30
drink = 5

while not done:
    print("A. Ус уух.")
    print("B. Дундаж хурдаар явах.")
    print("C. Бүх хурдаараа явах.")
    print("D. Зогсож амрах.")
    print("E. Нөхцөл байдлыг шалгах.")
    print("F. Элсэн шуурга болох")
    print("Q. Гарах.")
    print()

    choice = input("Таны сонголт? :")

    if choice.upper() == "Q":
        done = True

    elif choice.upper() == "E":
        print("Туулсан зам: ", km_traveled, "км")
        print("Савтай усны тоо: ", drink, "ш")
        print("Цагдаа таниас ", km_traveled -
              police_traveled, "км-ийн зайтай байна.")
        print("Тэмээний ядарсан хэмжээ: ", camel_tired, "%")
        print("Ам цангасан хэмжээ: ", thirst, "\n")
        print()
    elif choice.upper() == "D":
        camel_tired = 0
        police_up = random.randrange(6, 15)
        police_traveled = police_traveled + police_up
        print("Тэмээ амарч авлаа! гэвч цагдаа ",
              police_up, "км зам тууллаа.\n")
        print()

    elif choice.upper() == "F":
        thirst = thirst + 1
        drink -= 1

    elif choice.upper() == "C":
        full_speed = random.randrange(10, 20)
        km_traveled = km_traveled + full_speed
        police_up = random.randrange(6, 15)
        police_traveled = police_traveled + police_up
        thirst = thirst + 1
        camel_tired = camel_tired + random.randrange(2, 3)*10
        oasis = random.randrange(1, 20)
        if oasis == 10:
            thirst = 0
            camel_tired = 0
            drink = 5
            print("Та ", full_speed, " км зам тууллаа.")
            print("Баянбүрд тааралдлаа баяр хүргэе")
            print("Таны амны цангаа тайлагдаж савнуудаа усаар дүүргэж авлаа")
            print("Мөн таны тэмээ амарч авлаа")
            print("Гэвч,Цагдаа ", police_up, "км зам тууллаа")
            print()
        else:
            print("Та ", full_speed, "км зам тууллаа.")
            print("Тэмээний ядарсан хэмжээ: ", camel_tired, "%")
            print("Ам цангасан хэмжээ: ", thirst)
            print("Цагдаа ", police_up, "км зам тууллаа\n")
    elif choice.upper() == "B":
        mid_speed = random.randrange(5, 12)
        km_traveled = km_traveled + mid_speed
        police_up = random.randrange(6, 15)
        police_traveled = police_traveled + police_up
        thirst = thirst + 1
        camel_tired = camel_tired + random.randrange(1, 2)*10
        oasis = random.randrange(1, 20)
        if oasis == 10:
            thirst = 0
            camel_tired = 0
            drink = 5
            print("Та ", mid_speed, " км зам тууллаа.")
            print("Баянбүрд тааралдлаа баяр хүргэе")
            print("Таны амны цангаа тайлагдаж савнуудаа усаар дүүргэж авлаа")
            print("Мөн таны тэмээ амарч авлаа")
            print("Гэвч,Цагдаа ", police_up, "км зам тууллаа")
            print()
        else:
            print("Та ", mid_speed, "км зам тууллаа.")
            print("Тэмээний ядарсан хэмжээ: ", camel_tired, "%")
            print("Ам цангасан хэмжээ: ", thirst)
            print("Цагдаа ", police_up, "км зам тууллаа\n")
    elif choice.upper() == "A":
        if drink > 0:
            print("Та цангаагаа тайлж 1 савтай усаа уулаа.")
            drink = drink - 1
            print("Таньд ", drink, "ширхэг савтай ус үлдлээ.\n")
            thirst = 0
        else:
            print("Ус дууссан!!!")

    if thirst >= 5:
        print("Та цангаж үхэв!")
        print()
        done = True
        break
    elif thirst >= 4:
        print("Ам цангаж үхлээ шдээ!\n")
    elif thirst >= 3:
        print("Ам цангаж байна.!\n")
    if camel_tired >= 100:
        print("Таны тэмээ ядарч үхэв!")
        done = True
        break
    # Таны тэмээ ядарч байна!
    elif camel_tired >= 50:
        print("Таны тэмээ ядарч байна.!\n")
    # Та цагдаад баригдлаа!
    if km_traveled - police_traveled <= 0:
        print("Та цагдаад баригдлаа.")
        done = True
        break
    # Цагдаа ойртож байна.
    elif km_traveled - police_traveled <= 15:
        print("Цагдаа ойртож байна.\n")

    if km_traveled >= 200:
        print("Та чадлаа, их элсэн говийг амжилттай туулж цагдаагаас зугтаж чадлаа")
        done = True

    # Тэмээ удаашрина
    if camel_tired >= 50:
        full_speed = random.randrange(5, 10)
    else:
        full_speed = random.randrange(10, 20)
    # Тэмээ удаашрина
    if camel_tired >= 50:
        mid_speed = random.randrange(3, 10)
    else:
        mid_speed = random.randrange(5, 12)
    # Тоглоом дуусна
print("Тоглоом дууслаа.")
