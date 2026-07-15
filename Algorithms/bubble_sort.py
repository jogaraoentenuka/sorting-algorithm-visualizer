def bubble_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.list
    
    for i in range(len(lst) - 1):
        for j in range(len(lst)-1-i):
            num_1 = lst[j]
            num_2 = lst[j+1]
            
            if (num_1 > num_2 and ascending) or (num_1 < num_2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True
                
    return lst