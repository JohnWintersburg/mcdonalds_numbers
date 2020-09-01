import sys
def enter(number):
    one = ["   *","  **"," * *","   *","****"]
    two = ["****","   *","  * "," *  ","****"]
    three = ["****","   *"," ***","   *","****"]
    four = ["*  *","*  *","*  *","****","   *"]
    five = ["****","*   ","*** ","   *","****"]
    six = ["   *"," *  ","****","*  *","****"]
    seven = ["****","   *"," ***","   *","   *"]
    eight = ["****","*  *","****","*  *","****"]
    nine = ["****","*  *","****","  * "," *  "]
    zero = ["****","*  *","*  *","*  *","****"]
    final = [" "," "," "," "," "]
    i = 0
    while i < len(number):
        current = number[i]
        if int(current) == 1:
            final[0] = final[0]+one[0]+" "
            final[1] = final[1]+one[1]+" "
            final[2] = final[2]+one[2]+" "
            final[3] = final[3]+one[3]+" "
            final[4] = final[4]+one[4]+" "
        if int(current) == 2:
            final[0] = final[0]+two[0]+" "
            final[1] = final[1]+two[1]+" "
            final[2] = final[2]+two[2]+" "
            final[3] = final[3]+two[3]+" "
            final[4] = final[4]+two[4]+" "
        if int(current) == 3:
            final[0] = final[0]+three[0]+" "
            final[1] = final[1]+three[1]+" "
            final[2] = final[2]+three[2]+" "
            final[3] = final[3]+three[3]+" "
            final[4] = final[4]+three[4]+" "
        if int(current) == 4:
            final[0] = final[0]+four[0]+" "
            final[1] = final[1]+four[1]+" "
            final[2] = final[2]+four[2]+" "
            final[3] = final[3]+four[3]+" "
            final[4] = final[4]+four[4]+" "
        if int(current) == 5:
            final[0] = final[0]+five[0]+" "
            final[1] = final[1]+five[1]+" "
            final[2] = final[2]+five[2]+" "
            final[3] = final[3]+five[3]+" "
            final[4] = final[4]+five[4]+" "
        if int(current) == 6:
            final[0] = final[0]+six[0]+" "
            final[1] = final[1]+six[1]+" "
            final[2] = final[2]+six[2]+" "
            final[3] = final[3]+six[3]+" "
            final[4] = final[4]+six[4]+" "
        if int(current) == 7:
            final[0] = final[0]+seven[0]+" "
            final[1] = final[1]+seven[1]+" "
            final[2] = final[2]+seven[2]+" "
            final[3] = final[3]+seven[3]+" "
            final[4] = final[4]+seven[4]+" "
        if int(current) == 8:
            final[0] = final[0]+eight[0]+" "
            final[1] = final[1]+eight[1]+" "
            final[2] = final[2]+eight[2]+" "
            final[3] = final[3]+eight[3]+" "
            final[4] = final[4]+eight[4]+" "
        if int(current) == 9:
            final[0] = final[0]+nine[0]+" "
            final[1] = final[1]+nine[1]+" "
            final[2] = final[2]+nine[2]+" "
            final[3] = final[3]+nine[3]+" "
            final[4] = final[4]+nine[4]+" "
        if int(current) == 0:
            final[0] = final[0]+zero[0]+" "
            final[1] = final[1]+zero[1]+" "
            final[2] = final[2]+zero[2]+" "
            final[3] = final[3]+zero[3]+" "
            final[4] = final[4]+zero[4]+" "
        i += 1
    print(final[0])
    print(final[1])
    print(final[2])
    print(final[3])
    print(final[4])
    cons()
def cons():
    consequence = input("If you want to close app write n.\nOtherwise, enter your number\n")
    if consequence == "n":
        sys.exit()
    else:
        enter(consequence)
number = input("Enter your number:\n")
enter(number)
