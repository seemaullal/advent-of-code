# frozen_string_literal: true

path = File.expand_path('../inputs/13.txt', __dir__)
# rubocop:disable Security/Eval
packets = File.read(path).split("\n").reject(&:empty?).map { eval(_1) }
# rubocop:enable Security/Eval

DIVISOR_PACKETS = [[[2]], [[6]]].freeze

def compare(item1, item2)
  if item1.is_a?(Integer) && item2.is_a?(Integer)
    return 0 if item1 == item2

    item1 < item2 ? -1 : 1
  elsif item1.is_a?(Array) && item2.is_a?(Array)
    item1.each_with_index do |first_value, index|
      break unless item2[index]

      result = compare(first_value, item2[index])
      return result unless result.zero?
    end
    return 0 if item1.length == item2.length

    item1.length < item2.length ? -1 : 1
  else
    compare(Array(item1), Array(item2))
  end
end

part1 = packets.each_slice(2).filter_map.with_index(1) do |(item1, item2), packet_number|
  packet_number if compare(item1, item2) == -1
end.sum

sorted_packets = [*packets, *DIVISOR_PACKETS].sort { |pair1, pair2| compare(pair1, pair2) }

part2 = sorted_packets.filter_map.with_index(1) do |packet, packet_number|
  packet_number if DIVISOR_PACKETS.include?(packet)
end.reduce(&:*)

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
