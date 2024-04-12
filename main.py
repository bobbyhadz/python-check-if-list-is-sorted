# Check if a List is Sorted (Ascending) in Python

def is_sorted_ascending(lst):
    return all(
        lst[index] <= lst[index+1]
        for index in range(len(lst) - 1)
    )


list_1 = [1, 2, 3, 4, 5]
print(is_sorted_ascending(list_1))  # 👉️ True

list_2 = [5, 4, 3, 2, 1]
print(is_sorted_ascending(list_2))  # 👉️ False

if is_sorted_ascending(list_1):
    print('The list is sorted in ascending order')
else:
    print('The list is not sorted in ascending order')
