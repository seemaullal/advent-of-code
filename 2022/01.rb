# frozen_string_literal: true

input = File.read("#{__dir__}/inputs/1.txt").split("\n\n").map { |nums| nums.split("\n").map(&:to_i) }
part1 = input.map(&:sum).max

part2 = input.sort_by(&:sum).last(3).map(&:sum).sum

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
