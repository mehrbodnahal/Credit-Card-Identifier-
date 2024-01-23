def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


while True:
    card = get_positive_int("Card: ")
    if card > 0:
        break


def LAW_check_value(card):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    check_value = 0
    check_value += sum(odd_digits)
    for d in even_digits:
        check_value += sum(digits_of(d * 2))
    return check_value % 10


card_str = str(card)
length = len(card_str)

visa = card
amex = card
master = card

while visa >= 10:
    visa = int(visa / 10)

while master >= 10**14:
    master = int(master / 10**14)

while amex >= 10**13:
    amex = int(amex / 10**13)

if LAW_check_value(card) == 0:
    if card_str.startswith("4") and (length == 13 or length == 16):
        print("VISA")
    elif length == 15 and (amex == 34 or amex == 37):
        print("AMEX")
    elif length == 16 and (51 <= master <= 55):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
