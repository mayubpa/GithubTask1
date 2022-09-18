from math_function import add, multiple, minus, divide

def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    
    elif operator == "-":
        result = minus(data_1, data_2)
    
    elif operator == "*":
        result = multiple(data_1, data_2)
    
    elif operator == "/":
        result = divide(data_1, data_2)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()