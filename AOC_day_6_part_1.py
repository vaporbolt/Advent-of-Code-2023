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
    times = list(map(lambda x: int(x), input_list[0].split("Time:      ")[1].split()))
    record_distances = list(map(lambda x: int(x), input_list[1].split("Distance:  ")[1].split()))
    speed = 0
    winning_combination_count = 0
    for i in range(len(times)):
        for j in range(times[i]):
            if j * (times[i] - j) > record_distances[i]:
                winning_combination_count += 1

        winning_combinations_count.append(winning_combination_count)
        winning_combination_count = 0

    total_value = functools.reduce(lambda a, b: a * b, winning_combinations_count)
    return total_value
main()

