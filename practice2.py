def take_fruits():
    fruits = {}
    while True:
        item_taker = input()
        
        if item_taker == "finish":
            return fruits


        fruit , price = item_taker.split()
        price = int(price)
        fruits[fruit] = price


def how_many_item(**fruits):
    print(f"You have {len(fruits)} fruits in your shopping list")


def total_price(**fruits):
    total = sum(fruits.values())
    print(f"The total cost of the shopping list is {total}")


def min_price(**fruits):
    cheapest_fruit = min(fruits , key=fruits.get)
    cheapest_fruit_price = fruits[cheapest_fruit]
    print(f"The cheapest fruit is {cheapest_fruit} with the price of {cheapest_fruit_price}")


def max_price(**fruits):
    most_expensive_fruit = max(fruits , key=fruits.get)
    most_expensive_fruit_price = fruits[most_expensive_fruit]
    print(f"The most expensive fruit is {most_expensive_fruit} with the price of {most_expensive_fruit_price}")



def main():
    fruits = take_fruits()
    how_many_item(**fruits)
    total_price(**fruits)
    max_price(**fruits)
    min_price(**fruits)


main()















