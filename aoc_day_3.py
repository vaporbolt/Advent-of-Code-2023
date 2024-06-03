import sys
import functools

def main():
    input_file = sys.argv[1]
    input_text = open(input_file, "r").read()
    input_list = input_text.split("\n")
    viable_parts = get_viable_parts(input_list)
    answer = sum(viable_parts)
    print(answer)



def get_viable_parts(input_list):
    # width of the list
    grid_width = len(input_list[0])
    # however many entries is the height
    grid_height = len(input_list)
    # intialize grid
    grid = populate_grid(input_list, grid_width, grid_height)
    
    viable_parts = populate_viable_parts(grid)
    return viable_parts


def populate_grid(input_list, grid_width, grid_height):
    grid = [[None for i in range(grid_height)] for j in range(grid_width)]
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            grid[i][j] = input_list[i][j]

    return grid

def populate_viable_parts(grid):
    viable_parts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            symbol = grid[i][j]
            # if it's a symbol, we gotta get all adjacent numbers, and mark those numbers with None for "Taken"
            if not symbol.isdigit() and symbol != ".":
                adjacents = []
                adjacents.append(check_number(grid, i, j - 1)) # check left 
                adjacents.append(check_number(grid, i, j + 1)) # check right
                adjacents.append(check_number(grid, i - 1, j)) # check above
                adjacents.append(check_number(grid, i + 1, j)) # check below
                adjacents.append(check_number(grid, i + 1, j - 1)) # check bottom left
                adjacents.append(check_number(grid, i + 1, j + 1)) # check bottom right
                adjacents.append(check_number(grid, i -1 , j - 1)) # check top left
                adjacents.append(check_number(grid, i -1, j + 1)) # check bottom right
                # add all the none Nones into the parts list
                for part in adjacents:
                    if part is not None:
                        viable_parts.append(part)
    return viable_parts                    

# Returns the number at the location or None if there isn't a number / isn't valid location
def check_number(grid, i, j):
    if i < 0 or i >= len(grid):
        return None
    if j < 0 or j >= len(grid[0]):
        return None
    
    # if it's a number find the first digit of the number and put together the number
    if grid[i][j].isdigit():
        col = j
        while(col - 1 >= 0 and grid[i][col - 1].isdigit()):
            col = col - 1
        # col is now first digit
        str_num = ""
        while col >= 0 and col < len(grid[0]) and (grid[i][col].isdigit()):
            str_num += grid[i][col]
            grid[i][col] = "" # mark it as being included already
            col += 1
        return int(str_num)

main()