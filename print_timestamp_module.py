from datetime import datetime
old_print = print


def timestamped_print(*args, **kwargs):
    old_print(datetime.now(), *args, **kwargs)


# Print with timestamp
print = timestamped_print