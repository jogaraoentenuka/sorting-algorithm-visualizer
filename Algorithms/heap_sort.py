def heap_sort(draw_info, draw_list, ascending=True):
    lst = draw_info.list
    n = len(lst)
    
    #Building Heap
    for i in range(n//2 - 1, -1, -1):
        yield from heapify(lst, n, i, draw_info, draw_list, ascending)
        
    # Extracting Elements
    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        
        draw_list(
            draw_info, 
            {0: draw_info.ORANGE, i: draw_info.DARK_GREEN},
            True
        )
        yield True
        yield from heapify(lst, i, 0, draw_info, draw_list, ascending)
        
def heapify(lst, heap_size, root, draw_info, draw_list, ascending):
    extreme = root
        
    left = 2*root + 1
    right = 2*root + 2
    
    # Show the current node and its children
    color_positions = {root: draw_info.RED}

    if left < heap_size:
        color_positions[left] = draw_info.GREEN
    if right < heap_size:
        color_positions[right] = draw_info.BLUE

    draw_list(draw_info, color_positions, True)
    yield True
    
    if ascending:
        if left < heap_size and lst[left] > lst[extreme]:
            extreme = left
        if right < heap_size and lst[right] > lst[extreme]:
            extreme = right
    else:
        if left < heap_size and lst[left] < lst[extreme]:
            extreme = left
        if right < heap_size and lst[right] < lst[extreme]:
            extreme = right
            
    if extreme != root:
        draw_list(
            draw_info,
            {
                root: draw_info.RED,
                extreme: draw_info.PURPLE,
            },
            True,
        )
        yield True
            
    if extreme != root:
        lst[root], lst[extreme] = lst[extreme], lst[root]
        
        draw_list(draw_info, {root: draw_info.ORANGE, extreme: draw_info.ORANGE}, True)
        yield True
        yield from heapify(lst, heap_size, extreme, draw_info, draw_list, ascending)