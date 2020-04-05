ranges = [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12), (20, 30)]

def merge_ranges(meeting_time_ranges):
    """ merges times if they immediately follow each other  and returns the merged range """
    meeting_times = sorted(meeting_time_ranges)
    merged_range = [meeting_times[0]]

    for start, end in meeting_times[1:]:
        last_start, last_end = merged_range[-1]

        if last_end >= start:
            merged_range[-1] = (last_start, max(last_end, end))
        else:
            merged_range.append((start, end))
    
    return merged_range


merge_ranges(ranges)
