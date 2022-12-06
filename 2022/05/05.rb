# frozen_string_literal: true

require 'pry'
path = File.expand_path('../inputs/5.txt', __dir__)

start, instructions = File.read(path).split("\n\n")
start = start.split("\n").map(&:chars).reverse[1..]
instructions = instructions.split("\n").map do |instruction|
  instruction.split.filter_map { _1.to_i if _1.to_i.to_s == _1 }
end

part1 = Array.new(9) { [] }
part2 = Array.new(9) { [] }

[part1, part2].each do |part|
  start.each do |line|
    (1..35).step(4).each_with_index do |v, idx|
      part[idx].push(line[v]) unless line[v] == ' '
    end
  end
end

instructions.each do |num_to_move, move_from, move_to|
  part1[move_to - 1].concat(part1[move_from - 1].pop(num_to_move).reverse)
  part2[move_to - 1].concat(part2[move_from - 1].pop(num_to_move))
end

puts "Part 1: #{part1.map(&:last).join}"
puts "Part 2: #{part2.map(&:last).join}"
