import DataStructure.Sort

mSort_test = DataStructure.Sort.Sort()
list_test = [1,9,5,6,3,7,0,2,5,9,8]
print(list_test)
print(sorted(list_test))
mSort_test.SelectionSort(list_test)
print(list_test)
