def numRollsToTarget(n, k,target):
        if n == 1:
            return 1
        count = 0
        for i in range(n):
            for j in range(k):
                if i+j == target:
                    count+=1
        return count


print(numRollsToTarget(2,6,7))