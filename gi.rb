# frozen_string_literal: true

require 'fileutils'
require 'uri'
require 'net/http'

cookie = ENV['AOC_SESSION']
day = ARGV[0]
year = ARGV[1] || 2022
directory = File.expand_path("#{year}/inputs")

FileUtils.mkdir(directory) unless File.directory?(directory)

uri = URI("http://adventofcode.com/#{year}/day/#{day}/input")
response = Net::HTTP.get_response(uri)
https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(uri)
request['Cookie'] = "session=#{cookie}"
# per https://www.reddit.com/r/adventofcode/comments/z9dhtd
request['User-Agent'] = 'github.com/seemaullal/advent-of-code/blob/main/gi.rb by seemaullal at gmail dot com'
response = https.request(request)

File.open("#{directory}/#{day}.txt", 'w') { |f| f.write(response.read_body) }
system('open', "https://adventofcode.com/#{year}/day/#{day}")
