# Для сортировки массива была выбрана сортировка слиянием. Временная сложность (даже в худшем случае)
# составляет О(n logn), в отличие от некоторых сортировок, которые в худжем случае дауют временную 
# сложность хуже. Помимо этого данная сортировка отлично подходит для сортировки массива из внешнего
# источника. Допустим есть файл, который весит несколько Гб и не помещается в память, тогда с помощью сортировки
# слиянием можно получать последовательный доступ к данным, сортировать их и записывать в другой файл.
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        i = j = 0
        newArray = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                newArray.append(left[i])
                i += 1
            else:
                newArray.append(right[j])
                j += 1
        while i < len(left):
            newArray.append(left[i])
            i += 1
        while j < len(right):
            newArray.append(right[j])
            j += 1
        return newArray

    else:
        return nums
    

def TestMergeSort():
    print(mergeSort([1, 4, 3, 2, 3, 2]))
    print(mergeSort([4]))
    print(mergeSort([]))
    print(mergeSort([5, 5, 5, 5, 5]))
    print(mergeSort([1, 2, 3, 4, 5]))
    print(mergeSort([5, 4, 3, 2, 1]))
    print(mergeSort([-4, 9, 2, -3, -6, 0, 10, -2]))
    print(mergeSort([49324, 124421, 86553, 25214343, 111111]))


if __name__ == "__main__":
    TestMergeSort()