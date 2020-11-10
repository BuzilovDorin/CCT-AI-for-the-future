start_num, last_num = int(input('Enter Starting number: ')), int(input("Enter Last number: "))


for x in range(start_num, last_num+1):
    if (x % 2) == 0:
        print(x)