class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array = list()
        for i in range(len(arr)):
            if i+1 < len(arr):
                max_arr = arr[i+1:]
                max_num = max(max_arr)
                new_array.append(max_num)
            if i+1 == len(arr):
                new_array.append(-1)
        return new_array