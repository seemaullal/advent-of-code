# frozen_string_literal: true

path = File.expand_path('../inputs/3.txt', __dir__)

input = File.readlines(path, chomp: true)

def get_priority(char)
  if char.match(/[[:lower:]]/)
    char.ord - 96
  else
    char.ord - 38
  end
end

part1 = input.sum do |items|
  compartment1, compartment2 = items.chars.each_slice(items.length / 2).to_a
  get_priority((compartment1 & compartment2)[0])
end

part2 = input.each_slice(3).sum do |group|
  in_common = (group[0].chars & group[1].chars & group[2].chars)[0]
  get_priority(in_common)
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
