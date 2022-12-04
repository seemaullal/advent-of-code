# frozen_string_literal: true

class Entry
  attr_reader :password_frequency, :letter, :min_amount, :max_amount, :password

  def initialize(password_frequency:, letter:, min_amount:, max_amount:, password:)
    @password_frequency = password_frequency
    @letter = letter
    @min_amount = min_amount
    @max_amount = max_amount
    @password = password
  end
end

# shared setup
path = File.expand_path('../inputs/2.txt', __dir__)
entries = File.readlines(path)
entry_info = entries.map do |entry|
  requirements, password = entry.split(':').map(&:strip)
  amounts, letter = requirements.split
  min_amount, max_amount = amounts.split('-').map(&:to_i)
  password_frequency = Hash.new(0)
  password.each_char do |char|
    password_frequency[char] += 1
  end
  Entry.new(
    password_frequency:,
    letter:,
    min_amount:,
    max_amount:,
    password:
  )
end

part1 = entry_info.count do |info|
  info.password_frequency[info.letter] >= info.min_amount &&
    info.password_frequency[info.letter] <= info.max_amount
end

part2 = entry_info.count do |info|
  (info.password.chars[info.min_amount - 1] == info.letter) ^
    (info.password.chars[info.max_amount - 1] == info.letter)
end

puts "part 1:  #{part1} "
puts "part 2:  #{part2} "
