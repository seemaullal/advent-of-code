# frozen_string_literal: true

require 'ostruct'

# shared setup
entries = File.open('day2_input.txt').read.split("\n")
entry_info = entries.map do |entry|
  requirements, password = entry.split(':').map(&:strip)
  amounts, letter = requirements.split(' ')
  min_amount, max_amount = amounts.split('-').map(&:to_i)
  password_frequency = Hash.new(0)
  password.each_char do |char|
    password_frequency[char] += 1
  end
  OpenStruct.new({
                   password_frequency: password_frequency,
                   letter: letter,
                   min_amount: min_amount,
                   max_amount: max_amount,
                   password: password
                 })
end

# part 1
valid_entry_count = entry_info.count do |info|
  info.password_frequency[info.letter] >= info.min_amount &&
    info.password_frequency[info.letter] <= info.max_amount
end

puts "number of valid entries for part 1: #{valid_entry_count}"

# part 2
valid_entry_count = entry_info.count do |info|
  (info.password.chars[info.min_amount - 1] == info.letter) ^
    (info.password.chars[info.max_amount - 1] == info.letter)
end
puts "valid entries for part 2: #{valid_entry_count}"
