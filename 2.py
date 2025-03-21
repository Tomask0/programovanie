import linecache as lc 

file_array = []
sorted_file_array_smallfirst = []
sorted_file_array_bigfirst = []

line_count = len(open(r"sensor_reading.txt", 'r').readlines())

for i in range(line_count):
    line = int(lc.getline('sensor_reading.txt', i+1))
    file_array.append(line)

sorted_file_array_smallfirst = sorted(file_array)
sorted_file_array_bigfirst = sorted(file_array, reverse=True)

# for n in sorted_file_array_bigfirst:
#     print(n)

print("max = ", max(file_array),"   min = ", min(file_array))
print(sum(file_array)/len(file_array)) 



class read_file:

    file_line = []

    def __init__(self) -> None:
        pass