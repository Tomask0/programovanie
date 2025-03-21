file = open(r"words.txt", 'r').readlines()
line_count = len(file)
print("line count = ", line_count)

new_file = ''.join(file)

print("word count = ", len(new_file.split()))
print("letter count = ", len(new_file))