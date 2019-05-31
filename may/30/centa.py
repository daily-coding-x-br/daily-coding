# Two-pass algorithm

def justify_text(k, words):
    lines = []
    line_info = []

    #assert(k <= max(list(map(len, words))))

    # First pass to determine the number of words on each line
    curr = { "words": 0, "chars": 0 }
    for word in words:
        print(word)
        if len(word) + curr["chars"] <= k:
            if curr["words"] > 0:
                curr["chars"] += 1
            
            curr["words"] += 1
            curr["chars"] += len(word)

        else:
            line_info.append(curr)
            curr = { "words": 1, "chars": len(word) }

    
    if curr["words"] != 0:
        line_info.append(curr)


    # Second pass to actually construct the lines
    line_start = 0
    for info in line_info:
        line = []
        padding, extra = 0, 0

        if info["words"] > 1:
            padding = int((k - info["chars"]) / (info["words"] - 1))
            extra = (k - info["chars"]) % (info["words"] - 1)

        for j in range(info["words"]):
            line.append(words[line_start+j])

            if j < info["words"] - 1:
                line.append(" " * (padding + 1))
                if j < extra:
                    line.append(" ")

        line_start += info["words"]
        lines.append("".join(line))

    return lines


if __name__ == "__main__":
    k = int(input())
    words = input().split()

    print(justify_text(k, words))
