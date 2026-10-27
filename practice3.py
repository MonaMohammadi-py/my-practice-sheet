#https://github.com/MonaMohammadi-py/my-practice-sheet/blob/main/practice3.py

def calculate_price(price , tax_rate=0.1):
    final_price = price * (1 + tax_rate)
    return final_price




def main():
    price = int(input())
    tax_rate = input()

    print(round(calculate_price(price , float(tax_rate=0.1))))


main()