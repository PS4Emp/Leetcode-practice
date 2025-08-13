#solution 1(Basic python) 
return nums + nums 

#solution 2(Loop)
result = [] 
for i in range(len(nums)):
    result.append(nums[i])
for i in range(len(nums)):
    result.append(nums[i])
return result 

#solution 3(Index Mapping)
n = lens(nums)
ans = [0] * (2 * n) 
for i in range(n):
    ans[i] = nums[i]
    ans[i + n] = nums[i]
return ans