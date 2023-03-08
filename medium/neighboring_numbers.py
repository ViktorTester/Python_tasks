s = input().split()

if len(s) == 1:
    print(*s)
else:
    nums = list((map(int, s)))
    nums = nums + nums[:2]
    arr = [nums[i] + nums[i + 2] for i in range(len(nums) - 2)]
    arr = [arr[-1]] + arr[:-1]
    print(arr)

# The input to the program is a list of numbers in one line. The program for each
# element displays the sum of its two neighbors. For the last element of a list,
# one of the neighbors is the element on the opposite side of the list.
