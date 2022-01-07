# problem 3
def mul_list(list):
    # Multiply elements one by one
    product = 1
    for i in list:
        product = product * i
    return product


list1 = [8, 2, 3, -1, 7]
print(list1)
print("product: ")
print(mul_list(list1))

print("==============================================================")

#problem 9
def is_even_num(l):
    evenNum = []
    for n in l:
        if n % 2 == 0:
            evenNum.append(n)
    return evenNum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("==============================================================")

def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [8, 2, 3, 0, 7]
print ("The sum of my_list is", sum_of_list(my_list))

print("================================================================")

#problem 10
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('peter piper picked a peck of pickled peppers'))
