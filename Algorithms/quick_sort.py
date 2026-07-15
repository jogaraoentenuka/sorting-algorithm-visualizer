def quick_sort(draw_info, draw_list, ascending=True):
    lst = draw_info.list

    yield from _quick_sort(
        lst,
        0,
        len(lst) - 1,
        draw_info,
        draw_list,
        ascending,
    )


def _quick_sort(lst, low, high, draw_info, draw_list, ascending):
    if low < high:

        pivot = yield from _partition(
            lst,
            low,
            high,
            draw_info,
            draw_list,
            ascending,
        )

        yield from _quick_sort(
            lst,
            low,
            pivot - 1,
            draw_info,
            draw_list,
            ascending,
        )

        yield from _quick_sort(
            lst,
            pivot + 1,
            high,
            draw_info,
            draw_list,
            ascending,
        )


def _partition(lst, low, high, draw_info, draw_list, ascending):
    pivot = lst[high]

    i = low - 1

    for j in range(low, high):

        if (lst[j] <= pivot and ascending) or \
           (lst[j] >= pivot and not ascending):

            i += 1
            lst[i], lst[j] = lst[j], lst[i]

            draw_list(
                draw_info,
                {
                    i: draw_info.GREEN,
                    j: draw_info.RED,
                    high: draw_info.GREY,
                },
                True,
            )

            yield True

    lst[i + 1], lst[high] = lst[high], lst[i + 1]

    draw_list(
        draw_info,
        {
            i + 1: draw_info.GREEN,
            high: draw_info.RED,
        },
        True,
    )

    yield True

    return i + 1