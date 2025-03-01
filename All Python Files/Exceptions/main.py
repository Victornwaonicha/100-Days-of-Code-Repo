# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(f"You entered {x}")
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again and make sure it's a number...")

# while True print('Hello world')


# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


# def bool_return():
#     try:
#         return True
#     finally:
#         return False


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise