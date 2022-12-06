# frozen_string_literal: true

path = File.expand_path('../inputs/5.txt', __dir__)

start, instructions = File.read(path).split("\n\n")

stack_number = start[-1].to_i

start = start.split("\n").map(&:chars).reverse[1..]

instructions = instructions.split("\n").map do |instruction|
  instruction.split.filter_map do |character|
    # only keep numbers
    character.to_i if character.to_i.to_s == character
  end
end

part1 = Array.new(stack_number) { [] }
part2 = Array.new(stack_number) { [] }

[part1, part2].each do |part|
  start.each do |line|
    (1..line.length).step(4).each_with_index do |v, idx|
      part[idx].push(line[v]) if line[v] != ' '
    end
  end
end

instructions.each do |num_to_move, move_from, move_to|
  part1[move_to - 1].concat(part1[move_from - 1].pop(num_to_move).reverse)
  part2[move_to - 1].concat(part2[move_from - 1].pop(num_to_move))
end

puts "Part 1: #{part1.map(&:last).join}"
puts "Part 2: #{part2.map(&:last).join}"
