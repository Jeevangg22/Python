# Print largest number in a given list
#
# def print_largest(number):
#     highest = number[0]
#     for i in number:
#         if i > highest:
#             highest = i
#     print(highest)
#
#
# num = [90, 29, 98, 34, 21, 99, 45]
# print_largest(num)

# Print even number in a given range
# def range_even(begin, last):
#     for i in range(begin, last):
#         if i % 2 == 0:
#             print(i, end=' ')
#
#
# start, end = map(int, input("enter start and end range: ").split())
# range_even(start, end)


# Triangle pattern

# def pattern(begin, last):
#     for i in range(begin, last + 1):
#         for j in range(i):
#             print('#', end=" ")
#         print('\n')
#
#
# start, end = map(int, input("enter start and end range: ").split())
# pattern(start, end)

# square pattern
# def pattern(begin, last):
#     for i in range(begin, last):
#         print('\n')
#         for j in range(begin, last):
#             print('#', end=" ")
#
#
# start, end = map(int, input("enter start and end range: ").split())
# pattern(start, end)
