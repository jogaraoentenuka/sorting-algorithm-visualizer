def selection_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.list
    
    for i in range(len(lst)):
        selected_idx = i
        
        for j in range(i+1, len(lst)):
            if(lst[j] < lst[selected_idx] and ascending) or (lst[j] > lst[selected_idx] and not ascending):              
                selected_idx = j
                
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED, selected_idx: draw_info.GREEN}, True)
            yield True
        
        if selected_idx != i:
            lst[i], lst[selected_idx] = lst[selected_idx], lst[i]
            
            draw_list(draw_info, {i: draw_info.GREEN, selected_idx: draw_info.RED}, True)
            yield True
            
    return lst