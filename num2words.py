import inflect
def num2words(num):
    p = inflect.engine()
    return print(p.number_to_words(num))
while True:
    num = int(input("Enter number to convert \n"))
    num2words(num)