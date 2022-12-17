# frozen_string_literal: true

require 'pry'
file_path = File.expand_path('../inputs/14.txt', __dir__)

rock_paths = File.readlines(file_path, chomp: true).map do |line|
  line.split(' -> ').map { _1.split(',').map(&:to_i) }
end

wall = []
y_max = -Float::INFINITY

rock_paths.each do |path|
  path.each_cons(2).each do |(x1, y1), (x2, y2)|
    # loop from smaller x to bigger x and smaller y to bigger y
    ([x1, x2].min..[x1, x2].max).each do |x|
      ([y1, y2].min..[y1, y2].max).each do |y|
        wall << [x, y]
        y_max = [y, y_max].max
      end
    end
  end
end

points = {}
wall.each { points[_1] = '#' }
sand_position = [500, 0]
keep_going = true

while keep_going
  x, y = sand_position
  loop do
    if points[[x, y + 1]].nil?
      y += 1
      if y > y_max
        keep_going = false
        break
      end
    elsif !points[[x - 1, y + 1]]
      x -= 1
      y += 1
    elsif !points[[x + 1, y + 1]]
      x += 1
      y += 1
    else
      points[[x, y]] = 'S'
      break
    end
  end
end

puts "part 1:  #{points.filter { |_k, v| v == 'S' }.length} "
# puts "part 2:  #{part2} "
