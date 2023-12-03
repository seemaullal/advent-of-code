# frozen_string_literal: true

require 'pry'

path = File.expand_path('../inputs/1.txt', __dir__)

document_lines = File.readlines(path, chomp: true)

document_lines.sum do |line|
  line = line.chars.filter_map do |char|
    char.to_i.to_s == char ? char.to_i : nil
  end
  print(line)
  0
end

# binding.pry
# part1 = numeric_values.map { |values| "#{values.first}#{values.last}".to_i }.sum

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
