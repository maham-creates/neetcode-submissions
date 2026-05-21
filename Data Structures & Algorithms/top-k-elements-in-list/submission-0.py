class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_hashmap ={}
        freq_array = [[] for i in range(len(nums)+1)]

        for number in nums:
           count_hashmap[number]= 1 + count_hashmap.get(number,0)
        
        for num,freq in count_hashmap.items():
            freq_array[freq].append(num)
        
        result = []
        for x in range(len(freq_array)-1, 0,-1):
            for num in freq_array[x]:
                result.append(num)
                if len(result) == k:
                   return result
    