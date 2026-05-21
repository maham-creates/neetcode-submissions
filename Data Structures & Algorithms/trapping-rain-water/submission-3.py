class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
          return 0
     
        total = 0
        l,r = 0, len(height)-1
        maxleft, maxright = height[l], height[r]
    
        while l < r:
            if maxleft <= maxright:
               l += 1
               maxleft = max(maxleft,height[l])
               total += maxleft - height[l]
            else:
                r -= 1
                maxright = max(maxright,height[r])
                total += maxright - height[r]
        return total

        