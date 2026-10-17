class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = [None] *len(arr)
        arr2[-1] = -1
        max = 0
        for index in range(len(arr)-1, 0, -1):
            if arr[index] > max:
                arr2[index-1] = arr[index]
                max = arr[index]
            else:
                arr2[index-1] = max
        return arr2