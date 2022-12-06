# frozen_string_literal: true

require 'pry'
path = File.expand_path('../inputs/5.txt', __dir__)

start, instructions = File.read(path).split("\n\n")
start = start.split("\n").map(&:chars).reverse[1..]
instructions = instructions.split("\n").map do |instruction|
  instruction.split.filter_map { _1.to_i if _1.to_i.to_s == _1 }
end

stacks = []

start.each do |line|
  (1..35).step(4).each_with_index do |v, idx|
    stacks[idx] ||= []
    stacks[idx].push(line[v]) unless line[v] == ' '
  end
end

part1 = stacks.map(&:dup)
part2 = stacks.map(&:dup)

instructions.each do |num_to_move, move_from, move_to|
  num_to_move.times do
    part1[move_to - 1].push(part1[move_from - 1].pop)
  end
  part2[move_to - 1].concat(part2[move_from - 1].pop(num_to_move))
end

puts part1.map(&:last).join
puts part2.map(&:last).join
