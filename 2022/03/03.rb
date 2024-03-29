# frozen_string_literal: true

path = File.expand_path('../inputs/3.txt', __dir__)

input = File.readlines(path, chomp: true)

LOWER_CASE_SCORES = ('a'..'z').each_with_object({}).with_index { |(char, result), index| result[char] = index + 1 }
SCORES = ('A'..'Z').each_with_object(LOWER_CASE_SCORES).with_index { |(char, result), index| result[char] = index + 27 }

part1 = input.map { |items| items.chars.each_slice(items.length / 2).to_a }.sum do |compartment1, compartment2|
  SCORES[(compartment1 & compartment2)[0]]
end

part2 = input.each_slice(3).map { _1.map(&:chars) }.sum do |first, second, third|
  SCORES[(first & second & third)[0]]
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
