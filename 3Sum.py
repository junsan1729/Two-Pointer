class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # based on two sum II approach 
        # sort nums to get lowest number in beginning 
        # helps in eliminating some cases when all numbers are positive
        nums.sort()


        for a in range(len(nums)):
            # repeating first operand
            if a>0 and nums[a-1] == nums[a]:
                continue

            # l = second operand pointer 
            # r = third operand pointer 
            l, r = a+1, len(nums)-1 

            # till l is strictly less than r
            # as they can't be the same element/operand 
            while l<r:
                sum = nums[a] + nums[l] + nums[r]

                # sum too high, take smaller third operand 
                if sum > 0:
                    r-=1 

                # sum too low, take larger second operand
                elif sum < 0:
                    l+=1

                # sum is zero, put into ans list, and 
                # traverse l till repeating elements are found 
                else:
                    ans.append([nums[a], nums[l], nums[r]])
                    # go to next position
                    l+=1
                    # now check for repeating element or not 
                    while l<r and nums[l-1] == nums[l]:
                        l+=1

        # return list of all combination which makes zero sum
        return ans                        
