#https://github.com/MonaMohammadi-py/my-practice-sheet/blob/main/practice3.py

def calculate_price(price , tax_rate=0.1):
    final_price = price * (1 + tax_rate)
    return final_price




def main():
    price = int(input())
    
    try:
        tax_rate = float(input())
    except EOFError:
        print(round(calculate_price(price) , 2))

    else:        
        print(round(calculate_price(price , tax_rate) , 2))


main()
