#Kadane’s Algorithm:

def maxSubArraySum(a, size):
    max = a[0]
    sum = 0

    for i in range(0, size):
        sum += a[i]
        if sum < 0:
            max = sum
            sum = 0


        # Do not compare for all elements. Compare only
        # when max_ending_here > 0
        elif (max < sum):
            max = sum

    return max


# Driver function to check the above function
a = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxSubArraySum(a, len(a))
print(ans)
