nums = [2, 11, 4, 15,7]
num_2 = [3,3]
target = 15

def calculate_two_sum(nums, target):
   seen = {}
   index = 0

   for i in nums:
       complement = target - i

       if complement in seen:
           return [seen[complement], index]   # <-- only mistake

       else:
           seen[i] = index
           index += 1


obj = calculate_two_sum(nums, target)
print(obj)
