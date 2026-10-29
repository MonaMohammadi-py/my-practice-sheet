#https://github.com/MonaMohammadi-py/my-practice-sheet/blob/main/practice3.py

def calculate_price(price , tax_rate=0.1):
    final_price = price * (1 + tax_rate)
    return round(final_price , 2)




def main():
    price = float(input())
    
    try:
        tax_rate = float(input())
    except EOFError:
        print(calculate_price(price))

    else:
        print(calculate_price(price , tax_rate))



main()
