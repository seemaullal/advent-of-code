# frozen_string_literal: true

path = File.expand_path('../inputs/10.txt', __dir__)
commands = File.read(path, chomp: true).split("\n").map(&:split)

def strength_increase
  $cycle_number % 40 == 20 ? $cycle_number * $x : 0
end

def update_pixels
  row_number = $cycle_number / 40
  col_number = $cycle_number % 40
  $pixels[row_number][col_number] = ($x - col_number).abs <= 1 ? '█' : ' '
  $cycle_number += 1
  $part1 += strength_increase
end

$part1 = 0
$cycle_number = 0
$x = 1
$pixels = Array.new(6) { Array.new(40) }
commands.each do |command, value|
  update_pixels
  if command == 'addx'
    update_pixels
    $x += value.to_i
  end
end

puts "part 1:  #{$part1} "
puts 'part 2:'
$pixels.map { puts(_1.join) }
