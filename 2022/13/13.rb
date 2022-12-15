# frozen_string_literal: true

require 'pry'

path = File.expand_path('../inputs/13.txt', __dir__)
pairs = File.read(path).split("\n\n").map { |pair| pair.split.map { eval(_1) } } # rubocop:disable Security/Eval

def compare(item1, item2)
  if item1.is_a?(Integer) && item2.is_a?(Integer)
    return 0 if item1 == item2
    return -1 if item1 < item2
    1
  elsif item1.is_a?(Array) && item2.is_a?(Array)
    item1.each_with_index do |first_value, index|
      break unless item2[index]

      result = compare(first_value, item2[index])
      return result unless result == 0
    end
    return 0 if item1.length == item2.length
    return -1 if item1.length < item2.length
    1
  else
    compare(Array(item1), Array(item2))
  end
end

part1 = pairs.each_with_index.filter_map { |(item1, item2), index| index + 1 if compare(item1, item2) == -1 }.sum

puts "part 1:  #{part1} "
# puts "part 2:  #{part2} "
