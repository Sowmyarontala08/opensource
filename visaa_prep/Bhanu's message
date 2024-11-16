import re
phone_number = input().strip()
pattern_with_code = r"^\+\d{2} \d{10}$"
if re.match(pattern_with_code, phone_number):
    digits = phone_number.split()[1]
    if sum(int(digit) for digit in digits) > 0:
        print("Correct")
    else:
        print("Incorrect")
elif len(phone_number) == 10 and phone_number.isdigit():
    print("Correct")
else:
    print("Incorrect")
