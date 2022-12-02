# frozen_string_literal: true

require 'set'

input = File.readlines('/Users/seema/p/advent-of-code/2022/inputs/2.txt').map { |line| line.split(' ') }

scores = { 'X' => 1, 'Y' => 2, 'Z' => 3 }
wins = { 'C' => 'X', 'B' => 'Z', 'A' => 'Y' }
loses = { 'C' => 'Y', 'B' => 'X', 'A' => 'Z' }
matches = { 'A' => 'X', 'B' => 'Y', 'C' => 'Z' }

part1 = input.sum do |player1, player2|
  points = scores[player2]
  if wins[player1] == player2
    points += 6
  elsif matches[player1] == player2
    points += 3
  end
  points
end

part2 = input.sum do |player1, instruction|
  case instruction
  when 'X'
    player2 = loses[player1]
    points = 0
  when 'Y'
    player2 = matches[player1]
    points = 3
  when 'Z'
    player2 = wins[player1]
    points = 6
  end
  points + scores[player2]
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
