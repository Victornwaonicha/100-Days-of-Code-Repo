def merge(list1, list2):
    merge_result = []
    
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_result.append(list1[i])
            i += 1
        else:
            merge_result.append(list2[j])
            j += 1
            
    while i < len(list1):
        merge_result.append(list1[i])
        i += 1

    # If there are remaining elements in list2
    while j < len(list2):
        merge_result.append(list2[j])
        j += 1
        
    return merge_result

# Test with two lists
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge(list1, list2)
print(merged_list)