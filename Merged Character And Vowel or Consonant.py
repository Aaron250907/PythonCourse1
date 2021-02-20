Character1 = input("Enter A Character : ");

if ((Character1 >= 'a' and Character1 <= 'z') or (Character1 >= 'A' and Character1 <= 'Z')):
    print(Character1, "Is a Character")
    if (Character1 == 'A') or (Character1 == 'a') or (Character1 == 'E') or (Character1 == 'e') or (
            Character1 == 'I') or (Character1 == 'i') or (Character1 == 'O') or (Character1 == 'o') or (
            Character1 == 'U') or (Character1 == 'u'):
        print(Character1, "is a vowel")

    else:
        print(Character1, "Is not A Vowel. It is a Consonent")


else:
    print(Character1, "Is Not A Character")
