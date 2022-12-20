# frozen_string_literal: true

require 'set'

path = File.expand_path('../inputs/18.txt', __dir__)
cubes = Set.new(File.readlines(path, chomp: true).map { _1.split(',').map(&:to_i) })

part1 = cubes.reduce(0) do |current_sum, (x, y, z)|
  current_sum += 1 unless cubes.include?([x + 1, y, z])
  current_sum += 1 unless cubes.include?([x - 1, y, z])
  current_sum += 1 unless cubes.include?([x, y + 1, z])
  current_sum += 1 unless cubes.include?([x, y - 1, z])
  current_sum += 1 unless cubes.include?([x, y, z + 1])
  current_sum += 1 unless cubes.include?([x, y, z - 1])
  current_sum
end

puts "part 1:  #{part1} "
