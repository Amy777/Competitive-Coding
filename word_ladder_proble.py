k=open('text_file.txt','r')
d = {}
#g = Graph()
    # create buckets of words that differ by one letter


for line in k:
    print(line)
    words = line[:-1]

    for i in range(len(words)):
        bucket = words[:i] + '_' + words[i+1:]
        print(bucket)
        if bucket in d:
            d[bucket].append(words)
        else:
            d[bucket] = [words]


print(d.items())

