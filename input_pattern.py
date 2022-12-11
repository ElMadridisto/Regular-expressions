import re

def input_pattern(rows, pattern):
    list_new = []
    for items in rows:
        list_new.append(re.sub(pattern, r"\1,\3,\6,\10,\12,+7(\16)\17-\18-\19\21\22\23", ','.join(items)))

    return list_new