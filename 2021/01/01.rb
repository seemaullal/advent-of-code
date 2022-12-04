# frozen_string_literal: true

input = File.readlines("#{__dir__}/inputs/1.txt").map(&:to_i)
part1 = input
        .each_cons(2)
        .count { |first, second| first < second }

part2 = input.each_cons(3).map(&:sum).each_cons(2).count { |first, second| first < second }

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
