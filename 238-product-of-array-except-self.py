from typing import List

# This solution works, but it's brute force and doesn't meet the requirements because it's not O(n);
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[1 + i:]

            leftPro = 1
            rightPro = 1

            for j in range(len(left)):
                leftPro = leftPro * left[j]
            
            for k in range(len(right)):
                rightPro = rightPro * right[k]

            answerI = leftPro * rightPro

            answer.append(answerI)

        return answer
    
# Solution by NeedCode, introducing prefix and suffix.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer