class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = [None] * len(arr)
        arr2[-1] = -1
        maximum = 0
        for i in range(len(arr)-2, -1, -1):
            if arr[i+1] > maximum:
                maximum = arr[i+1]
            arr2[i] = maximum
        return arr2
        