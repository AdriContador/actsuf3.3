import literals as msg
import functions

def main():
    x = functions.validate(msg.MENU + "\n", 1, 4)
    match(x):
        case 1:
            f_name = functions.direccio()
            functions.only_create(f_name)
        case 2:
            f_name = input(msg.MSG2)
            functions.read_file(msg.ROUTE + f_name)
        case 3:
            f_name = input(msg.MSG2)
            functions.mod_file(msg.ROUTE + f_name)
        case _:
            print(msg.EXIT)





if __name__ == "__main__":
    main()