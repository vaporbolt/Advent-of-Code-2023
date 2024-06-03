import sys
import functools

def main():
    input_file = sys.argv[1]
    input_text = open(input_file, "r").read()
    input_list = input_text.split("\n")
    seeds = list(map(lambda x: int(x),input_list[0].split("seeds: ")[1].split(" ")))
    seed_map = get_seed_map(seeds)
    seed_to_soil_map = get_map(input_list.index("seed-to-soil map:"),input_list)
    soil_to_fertilizer_map = get_map(input_list.index("soil-to-fertilizer map:"),input_list)
    fertilizer_to_water_map = get_map(input_list.index("fertilizer-to-water map:"),input_list)
    water_to_light_map = get_map(input_list.index("water-to-light map:"),input_list)
    light_to_temperature_map = get_map(input_list.index("light-to-temperature map:"),input_list)
    temperature_to_humidity_map = get_map(input_list.index("temperature-to-humidity map:"),input_list)
    humidity_to_location_map = get_map(input_list.index("humidity-to-location map:"),input_list)
    list_of_maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]
    seed_locations = []
    smallest_seed_location = float("inf")
    for seed in seed_map:
        for i in range(seed[1]):
            location = get_value_in_pipeline(seed[0] + i, list_of_maps)
            if location < smallest_seed_location:
                smallest_seed_location = location

    print (smallest_seed_location)

    #answer = sum(viable_parts)
    #print(answer)

def get_map(index_of_map_text, input_list):
    resources_map = [] # list of tuples containg desination, source, and the range
    index = index_of_map_text + 1
    while index < len(input_list) and input_list[index] != "":
        values = input_list[index].split(" ")
        destination_start = int(values[0])
        source_start = int(values[1])
        range_length = int(values[2])
        resources_map.append((destination_start, source_start, range_length))
        index +=1
    return resources_map




def get_value_in_pipeline(value, list_of_maps):
    current_value = value
    for resource_map in list_of_maps:
        for singular_map in resource_map:
            # if current value is between the start and the end
            if current_value >= singular_map[1] and current_value < singular_map[1] + singular_map[2]:
                # then the current value should be destination start + the range minus  
                current_value = singular_map[0] + current_value - singular_map[1]
                break
    return current_value

def get_seed_map(seeds):
    seed_map = [] # list of tuples with the starting seed and the
    index = 0
    for i in range(len(seeds)):
        if index >= len(seeds):
            break
        start_value = seeds[index]
        length = seeds[index + 1]
        index += 2
        seed_map.append((start_value, length))
    return seed_map    

main()