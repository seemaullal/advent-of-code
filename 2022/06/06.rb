# frozen_string_literal: true

path = File.expand_path('../inputs/6.txt', __dir__)

input = File.read(path, chomp: true)

part1 = input.chars.each_cons(4).to_a.index { |chars| chars.uniq.length == 4 } + 4
part2 = input.chars.each_cons(14).to_a.index { |chars| chars.uniq.length == 14 } + 14

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
