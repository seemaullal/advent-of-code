# frozen_string_literal: true

require 'pry'

path = File.expand_path('../inputs/13.txt', __dir__)
pairs = File.read(path).split("\n\n").map { |pair| pair.split.map { eval(_1) } } # rubocop:disable Security/Eval

KEEP_GOING = 'equal, check next'

def part_1_compare(item1, item2)
  if item1.is_a?(Integer) && item2.is_a?(Integer)
    return KEEP_GOING if item1 == item2

    item1 < item2
  elsif item1.is_a?(Array) && item2.is_a?(Array)
    item1.each_with_index do |first_value, index|
      break unless item2[index]

      result = part_1_compare(first_value, item2[index])
      return result unless result == KEEP_GOING
    end
    return KEEP_GOING if item1.length == item2.length

    item1.length < item2.length
  else
    part_1_compare(Array(item1), Array(item2))
  end
end

part1 = pairs.each_with_index.filter_map { |(item1, item2), index| index + 1 if part_1_compare(item1, item2) }.sum

puts "part 1:  #{part1} "
# puts "part 2:  #{part2} "
