def bucket_sort(draw_info, draw_list, ascending=True):
    lst = draw_info.list
    n = len(lst)

    if n == 0:
        return

    min_val = draw_info.min_val
    max_val = draw_info.max_val

    # Create buckets
    bucket_count = n
    buckets = [[] for _ in range(bucket_count)]

    interval = (max_val - min_val + 1) / bucket_count

    # Place elements into buckets
    for i, value in enumerate(lst):
        idx = int((value - min_val) / interval)

        if idx >= bucket_count:
            idx = bucket_count - 1

        buckets[idx].append(value)

        # Highlight the element being distributed
        draw_list(
            draw_info,
            {i: draw_info.BLUE},
            True
        )
        yield True

    # Sort each bucket
    for bucket in buckets:
        bucket.sort(reverse=not ascending)

    # Merge buckets back into the array
    index = 0

    for bucket in buckets:
        for value in bucket:
            lst[index] = value

            draw_list(
                draw_info,
                {index: draw_info.GREEN},
                True
            )
            yield True

            index += 1