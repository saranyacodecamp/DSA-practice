def maxones(k:int,arr:list) -> int:
    l=r=0
    zeroes = 0
    len_ans = 0
    curr_ans = 0
    while r < len(arr):
        if arr[r] == 0:
            zeroes += 1
        while zeroes > k: 
            if arr[l] == 0:
                zeroes -= 1
            l += 1
        curr_ans = r-l+1
        len_ans = max(len_ans,curr_ans)        
        r+=1
    return len_ans
a = [1,1,1,1,0,0,0,1,1,1,0]
print(maxones(2,a))
print(maxones(0,a))
        

