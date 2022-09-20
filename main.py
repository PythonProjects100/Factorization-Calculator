print("NOTE: Float isn't supported")
def main():
    a=int(input("Enter A Number: "))


    b=2
    print(" ","|",a)
    while a !=1:
        if b>a:
            print("1","|",a)
        elif a%b !=0:
            b=b+1
        elif a%b==0:
            a=a/b
            print(b,"|",a)
        if a==1:
        
            main()
main()

        