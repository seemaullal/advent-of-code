require 'httparty'
require 'fileutils'

cookie = ENV['AOC_SESSION']
base_url =  'adventofcode.com'
options = { headers: { 'Cookie' => "session=#{cookie}" } }
day = ARGV[0]
year = ARGV[1] || 2022
response = HTTParty.get("http://adventofcode.com/#{year}/day/#{day}/input", options)
directory = File.expand_path("../#{year}/inputs")
unless File.directory?(directory)
    FileUtils.mkdir(directory)
end
File.open("#{directory}/#{day}.txt", 'w') { |f| f.write(response.body) }