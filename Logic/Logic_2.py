# x = input("xの値を入力してください")
# y = input("xの値を入力してください")

# if x == y :
#     print("x=",x,"y=",y,"xとyの値が同じ場合")
# elif x> y:
#     print("x=",x,"y=",y,"xはyよりも大きい") 
# elif x < y:
#     print("x=",x,"y=",y,"xがyよりも小さい") 
        

# 問2：正負の奇数か偶数を判定するプログラム

# while True:
#     number = input("値を入力してください")

#     try :
#         number= int(number)
#         if number >= 0 :
#             if number%2 == 0 :
#                 print("正の数の偶数") 
#             else :
#                 print("正の数の奇数") 
#             break        
#         else :
#             if number%2 == 1 :
#                 print("負の数の奇数") 
#             else:
#                 print("負の数の偶数")   
#         break
#     except:   
#         print("다시 입력해주세용") 
#         number

# 問2：正負の奇数か偶数を判定するプログラム       

value = True 

while value :
    month = input("月の値（１～１２）を入力してください")

    try:
        month= int(month)
        if month>0 and month<13 :
            if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
                print(month,"は31日まであり") 
            elif month ==  4 or month ==6 or month ==9 or month ==11 :
                print(month,"は30日まであり") 
            elif month ==  2 :
                print(month,"は29日まであり")
        else:
            print("入力が間違っています") 
            value = False                    
    except:
        print("入力が間違っています") 
        value = False 