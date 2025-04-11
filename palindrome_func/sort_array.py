def remove_duplicates(nums):
    s= set()
    k = 0

    for num in nums:
        if num not in s:
            s.add(num)
            nums[k] = num
            k += 1

    return k


input1 =input("enter the num:")
nums=input1.split(",")
k = remove_duplicates(nums)
print(nums[0])
print("k =", k)
print("Modified nums =", nums[:k])



