def twosum(nums:list[int], target:int) -> list[int]:
    seen = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return []
print(twosum([5,7,9,11,5],10))
