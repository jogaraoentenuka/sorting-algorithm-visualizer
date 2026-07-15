def insertion_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.list
    
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i-1
        
        while j >= 0 and ((lst[j] > curr and ascending) or lst[j] < curr and not ascending):
            
            lst[j + 1] = lst[j]
            draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
            yield True
            
            j-=1
            
        lst[j+1] = curr
        
        draw_list(draw_info, {j+1: draw_info.GREEN}, True)
        yield True
    
    return lst