# frozen_string_literal: true

path = File.expand_path('../inputs/3.txt', __dir__)

input = File.readlines(path, chomp: true)

LOWER_CASE_SCORES = ('a'..'z').map.with_index { |char, index| [char, index + 1] }.to_h
UPPER_CASE_SCORES = ('A'..'Z').map.with_index { |char, index| [char, index + 27] }.to_h
SCORES = LOWER_CASE_SCORES.merge(UPPER_CASE_SCORES)

part1 = input.sum do |items|
  compartment1, compartment2 = items.chars.each_slice(items.length / 2).to_a
  SCORES[(compartment1 & compartment2)[0]]
end

part2 = input.each_slice(3).sum do |first, second, third|
  in_common = (first.chars & second.chars & third.chars)[0]
  SCORES[in_common]
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
