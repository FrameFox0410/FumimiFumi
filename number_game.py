import random
def guess_number() :
    number = random. randint(1,10)
    attempts = 0 
    print("ทายสินี่เลขอะไร")

    while True :
        try :
            guess = int(input("0-10"))

            attempts += 1
            if guess < number : 
                print("เพิ่มอีกกก")
            elif guess > number : 
                print("มากไปปป")
            else :
                print (f"ถูกต้อง! ลองไป{attempts}ครั้ง")
                break
        except ValueError : 
                print("ใช่เลขแน่นะวิ")

guess_number()