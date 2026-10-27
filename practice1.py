#https://github.com/MonaMohammadi-py/my-practice-sheet/blob/main/practice1.py

def sum_num(numbers_list):
    total = 0
    for number in numbers_list:
        total += number

    return total


def avg(total_sum , how_many):
    return total_sum / how_many


def valid_input():
    while True:
        try:
            numbers_list = list(map(float, input().split()))

        except ValueError:
            print("Invalid Input! Enter a valid input.")

        else:
            return numbers_list


def main():
    numbers_list = valid_input()
    how_many = len(numbers_list)
    total_sum = sum_num(numbers_list)
    print(f"{avg(total_sum , how_many):.2f}")


main()
