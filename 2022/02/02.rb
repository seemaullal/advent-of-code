# frozen_string_literal: true

require 'set'

input = File.readlines('/Users/seema/p/advent-of-code/2022/inputs/2.txt').map { |line| line.split(' ') }

scores = { 'X' => 1, 'Y' => 2, 'Z' => 3 }
wins = Set.new(%w[XC ZB YA])
matches = { 'A' => 'X', 'B' => 'Y', 'C' => 'Z' }

part1 = input.sum do |player1, player2|
  points = 0
  points += scores[player2]
  if wins.include?("#{player2}#{player1}")
    points += 6
  elsif matches[player1] == player2
    points += 3
  end
  points
end

# # part2 = input.map(&:sum).max(3).sum

puts "part 1:  #{part1} "
# # puts "part 2:  #{part2} "
