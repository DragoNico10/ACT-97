def func(input):
    num=int(input)
    if(num%4==0):
        if(num%100==0):
            if(num%400==0):
                print(f'The year {input} is a leap year')
            else:
                print(f'The year {input} is NOT a leap year')
        else:
            print(f'The year {input} is a leap year')
    else:
        print(f'The year {input} is NOT a leap year')
inp=input('Enter year')
func(inp)