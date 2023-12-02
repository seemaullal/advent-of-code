# frozen_string_literal: true

require 'pry'

path = File.expand_path('../inputs/1.txt', __dir__)

document_lines = File.readlines(path, chomp: true)
part2 = 0

numeric_values = document_lines.map(&:chars).map do |chars|
  puts chars
  chars.filter_map { |char| char.to_i.to_s == char ? char : nil }
end
binding.pry
part1 = numeric_values.map { |values| "#{values.first}#{values.last}".to_i }.sum

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
