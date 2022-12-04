# frozen_string_literal: true

path = File.expand_path('../inputs/3.txt', __dir__)

GRID = File.readlines(path, chomp: true)

COL_NUMBER = GRID[0].length
ROW_NUMBER = GRID.length

def calculate_slope_trees(right_amount, down_amount)
  row_position = col_position = tree_count = 0
  while row_position < ROW_NUMBER
    actual_col = col_position % COL_NUMBER
    tree_count += 1 if GRID[row_position][actual_col] == '#'
    row_position += down_amount
    col_position += right_amount
  end
  tree_count
end

part1 = calculate_slope_trees(3, 1)

part2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]].reduce(1) do |current_product, (right, down)|
  current_product * calculate_slope_trees(right, down)
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
