def remove_dups(data : list) -> list:
    unique_set = set(data)
    return list(unique_set)

my_list = [1, 2, 3, 4, 127]
print(remove_dups(my_list))

set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 4, 5}
difference_set = set_1 - set_2
print(difference_set)

set_3 = {1, 2, 3}
element_to_find = 2
for element in set_3:
    if element == element_to_find:
        print(f"Element {element_to_find} is in the set")
        break
