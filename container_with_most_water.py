class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max = 0
        while(start<end):
            breath = end-start
            length = min(height[start], height[end])
            print("l - " + str(length))
            index = height.index(length, start, end+1)
            print("b - " + str(breath))            
            if length*breath>max:
                print("a - " + str(length*breath))
                max = length*breath
            
            if(index==start):
                start+=1
            else:
                end-=1
            
        return max
