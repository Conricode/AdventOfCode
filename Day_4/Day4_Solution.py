#Part One
def part_one():
    def count_xmas_in_grid(grid, word="XMAS"):
        # Define the eight possible directions as (row_delta, col_delta)
        directions = [
            (0, 1),  # Horizontal right
            (1, 0),  # Vertical down
            (1, 1),  # Diagonal down-right
            (-1, 1), # Diagonal up-right
            (0, -1), # Horizontal left
            (-1, 0), # Vertical up
            (-1, -1),# Diagonal up-left
            (1, -1)  # Diagonal down-left
        ]
        
        rows = len(grid)
        cols = len(grid[0])
        word_length = len(word)
        count = 0
        
        # Check each cell as the starting point
        for row in range(rows):
            for col in range(cols):
                for dr, dc in directions:
                    # Check if the word fits in the current direction
                    if 0 <= row + dr * (word_length - 1) < rows and \
                    0 <= col + dc * (word_length - 1) < cols:
                        # Extract the word in this direction
                        match = True
                        for k in range(word_length):
                            if grid[row + k * dr][col + k * dc] != word[k]:
                                match = False
                                break
                        if match:
                            count += 1
        return count

    def read_grid_from_file(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    
    if __name__ == "__main__":
        filename = "Day_4\\Day4_Input.txt"
        grid = read_grid_from_file(filename)
        result = count_xmas_in_grid(grid)
        print(f"The word 'XMAS' appears {result} times in the grid.")

#Part Two
def part_two():
    def count_mas_in_grid(grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # Iterate through all possible 3x3 subgrids
        for row in range(rows - 2):
            for col in range(cols - 2):
                # Centre point must be 'A' for an X-MAS pattern
                if grid[row + 1][col + 1] == 'A':
                    # Check for all valid diagonal combinations forming an X
                    if (
                        # Top-left to bottom-right and Bottom-left to top-right
                        (grid[row][col] == 'M' and grid[row + 2][col + 2] == 'S' and
                        grid[row + 2][col] == 'M' and grid[row][col + 2] == 'S') or
                        # Top-right to bottom-left and Bottom-left to top-right
                        (grid[row][col + 2] == 'M' and grid[row + 2][col] == 'S' and
                        grid[row + 2][col + 2] == 'M' and grid[row][col] == 'S') or
                        # Top-left to bottom-right and Top-right to bottom-left
                        (grid[row][col] == 'M' and grid[row + 2][col + 2] == 'S' and
                        grid[row][col + 2] == 'M' and grid[row + 2][col] == 'S') or
                        # Bottom-left to top-right and Bottom-right to top-left
                        (grid[row + 2][col] == 'M' and grid[row][col + 2] == 'S' and
                        grid[row + 2][col + 2] == 'M' and grid[row][col] == 'S')
                    ):
                        count += 1

        return count

    def read_grid_from_file(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f]

    if __name__ == "__main__":
        filename = "Day_4\\Day4_Input.txt"
        grid = read_grid_from_file(filename)
        result = count_mas_in_grid(grid)
        print(f"The X-MAS pattern appears {result} times in the grid.")

part_one()
part_two()