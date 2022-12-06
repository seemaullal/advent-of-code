# frozen_string_literal: true

path = File.expand_path('../inputs/6.txt', __dir__)

input = File.read(path, chomp: true)

first_four_char_unique_sequence = input.chars.each_cons(4).find do |current_characters|
  current_characters.uniq.length == 4
end

part1 = input.index(first_four_char_unique_sequence.join) + 4

first_fourteen_char_unique_sequence = input.chars.each_cons(14).find do |current_characters|
  current_characters.uniq.length == 14
end

part2 = input.index(first_fourteen_char_unique_sequence.join) + 14

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
