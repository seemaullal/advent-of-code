# frozen_string_literal: true

path = File.expand_path('../inputs/4.txt', __dir__)

input_ranges = File.readlines(path, chomp: true).map do |elf_assignments|
  elf1, elf2 = elf_assignments.split(',')
  elf1_start, elf1_end = elf1.split('-').map(&:to_i)
  elf2_start, elf2_end = elf2.split('-').map(&:to_i)
  [Range.new(elf1_start, elf1_end), Range.new(elf2_start, elf2_end)]
end

part1 = input_ranges.count do |elf1_range, elf2_range|
  elf1_range.cover?(elf2_range) || elf2_range.cover?(elf1_range)
end

part2 = input_ranges.count do |elf1_range, elf2_range|
  !(elf1_range.last < elf2_range.first || elf2_range.last < elf1_range.first)
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
