class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]

        while l <= r:
            if maxleft <= maxright:
                total += max(min(maxleft,maxright) - height[l],0)
                maxleft = max(maxleft, height[l])
                l += 1
            else:
                total += max(min(maxleft,maxright) - height[r],0)
                maxright = max(maxright, height[r])
                r -= 1
        return total
                
        