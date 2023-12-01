# frozen_string_literal: true

path = File.expand_path('../inputs/1.txt', __dir__)

calories_per_elf = File.read(path).split("\n\n").map{ |calories| calories.split("\n").map(&:to_i).sum}

part1 = calories_per_elf.max

part2 = calories_per_elf.max(3).sum

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
