class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, maxVol = 0, len(height)-1, 0

        while l<r:
            # which ever is smaller height consider that fot volume calculation 
            # and traverse that pointer
            if height[l] < height[r]:
                vol = (r-l) * height[l]
                l += 1
            else:
                vol = (r-l) * height[r]
                r -= 1  

            # keep track of maximum vol   
            maxVol = max(maxVol, vol)

        return maxVol        
