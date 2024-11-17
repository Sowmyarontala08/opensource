N = int(input().strip())
if 3 <= N <= 8:
    print("Spring")
elif 6 <= N <= 8:
    print("Summer")
elif 9 <= N <= 11:
    print("Autumn")
elif 1<= N <= 2 or N == 12:
    print("Winter")
else:
    print("Invalid")
