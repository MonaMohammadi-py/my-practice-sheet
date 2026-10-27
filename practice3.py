##https://github.com/MonaMohammadi-py/my-practice-sheet/blob/main/practice3.py

def calculate_price(price , tax_rate=0.1):
    final_price = price * (1 + tax_rate)
    return final_price




def main():
    price = int(input())
    tax_rate = input()
    if tax_rate == "":
        print(round(calculate_price(price) , 2))

    else:
        tax_rate = float(tax_rate)
        print(round(calculate_price(price, tax_rate) , 2))