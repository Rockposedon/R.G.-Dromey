# a1 = n // 8
# a2 = n % 8
# print("Q = ", a1)
# print("R = ", a2)
# # for i in range(a1):
# #     if (a1 >= 0):
# #         a1 = a1 // 8
# #         a2 = a2 % 8
# #         print("Q = ", a1)
# #         print("R = ",a2)
# # for i in range(a1):
#
# def octal(n):
#     a1 = n // 8
#     a2 = n % 8
#     print("Q = ", a1)
#     print("R = ", a2)
#     if (a1 >= 0):
#         # for i in range(a1 != 0):
#         a1 = a1 // 8
#         a2 = a2 % 8
#
#         print("Q = ", a1)
#         print("R = ", a2)
#         print("r = ", a1)
# octal(n)
n = int(input("enter an integer : "))


def octal(n):
    if n > 0:
        octal(int(n / 8))
        print(n % 8, end="")


octal(n)
