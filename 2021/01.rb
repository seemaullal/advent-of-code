# frozen_string_literal: true

part1 = File.readlines("#{__dir__}/inputs/1.txt")
            .map(&:to_i)
            .each_cons(2)
            .count { |first, second| first < second }

puts "part 1:  #{part1} "
