def merge_sort(draw_info, draw_list, ascending=True):
    lst = draw_info.list
    
    yield from _merge_sort(lst, 0, len(lst) - 1, draw_info, draw_list, ascending)
    
def _merge_sort(lst, left, right, draw_info, draw_list, ascending):
    if left >= right:
        return
    
    mid = (left+right)//2
    
    yield from _merge_sort(lst, left, mid, draw_info, draw_list, ascending)
    yield from _merge_sort(lst, mid+1, right, draw_info, draw_list, ascending)
    
    yield from _merge(lst, left, mid, right, draw_info, draw_list, ascending)
    
def _merge(lst, left, mid, right, draw_info, draw_list, ascending):
    left_half = lst[left:mid+1]
    right_half = lst[mid+1:right+1]
    
    i = j = 0
    k = left
    
    while i < len(left_half) and j < len(right_half):
        
        if (left_half[i] <= right_half[j] and ascending) or (left_half[i] >= right_half[j] and not ascending):
            lst[k] = left_half[i]
            i += 1
        else:
            lst[k] = right_half[j]
            j += 1
            
        draw_list(draw_info, {k: draw_info.GREEN}, True)
        yield True
        
        k += 1
        
    while i < len(left_half):
        lst[k] = left_half[i]
        i += 1
        
        draw_list(draw_info, {k: draw_info.GREEN}, True)
        yield True
        
        k += 1
        
    while j < len(right_half):
        lst[k] = right_half[j]
        j += 1
        
        draw_list(draw_info, {k: draw_info.GREEN}, True)
        yield True
        
        k += 1
        
    return i+1