# frozen_string_literal: true

require 'httparty'
require 'fileutils'

cookie = ENV['AOC_SESSION']
options = { headers: { 'Cookie' => "session=#{cookie}" } }
day = ARGV[0]
year = ARGV[1] || 2022
response = HTTParty.get("http://adventofcode.com/#{year}/day/#{day}/input", options)
directory = File.expand_path("#{year}/inputs")

FileUtils.mkdir(directory) unless File.directory?(directory)

File.open("#{directory}/#{day}.txt", 'w') { |f| f.write(response.body) }
system('open', "https://adventofcode.com/#{year}/day/#{day}")
