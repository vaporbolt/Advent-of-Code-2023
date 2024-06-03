import sys
import functools

def main():
    input_file = sys.argv[1]
    input_text = open(input_file, "r").read()
    input_list = input_text.split("\n")
    total_value = get_winning_combinations(input_list)

    print(total_value)



def get_winning_combinations(input_list):
    winning_combinations_count = []
    time = 0
    record_distance = 0
    times = list(map(lambda x: int(x), input_list[0].split("Time:      ")[1].split()))
    record_distances = list(map(lambda x: int(x), input_list[1].split("Distance:  ")[1].split()))
    str_time = ""
    d_time = ""
    for t in times:
        str_time += str(t)
    for d in record_distances:
        d_time += str(d)
    time = int(str_time) 
    record_distance = int(d_time)   
    speed = 0
    winning_combination_count = 0
    for i in range(time):
        if i * (time - i) > record_distance:
            winning_combination_count += 1


    return winning_combination_count
main()

