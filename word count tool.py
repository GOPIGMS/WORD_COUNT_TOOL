

def counting(value):
    print(value)
    value=value.split()
    print(len(value))
    con=input("If  you want to continue  press y:").upper()
    if con=="Y":
        choice()
    else:
        print("Thank you for using me !!!")




def choice_selection(choice):

    if choice== 1:
        filename=input("Enter the file name with the extension (example: text.txt)\n \t or \n Enter the path (example: D:\\python in pycharm\\python simple project\\text.txt):")
        try:
         with open(filename, "r" ) as f :
           value =f.read()
           counting(value)
        except Exception as e:
            print(e,"please check the input file or directory entered properly")


    elif choice==2:
        usertext=input("Enter the text:")
        counting(usertext)


    else :
        print("Invalid Input ")



def choice():

    choice=int(input("Enter the choice  \n 1 to input file \n \t or \n 2 to enter the text :"))
    choice_selection(choice)


if __name__=="__main__":
     choice()