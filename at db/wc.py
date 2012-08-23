def word_count(file_path, word):
    count = 0
    for line in open(file_path):
        if word in line.strip():
            count += 1
    print word, 'count:', count
