# frozen_string_literal: true

require 'fileutils'
require 'uri'
require 'net/http'

cookie = ENV.fetch('AOC_SESSION', nil)
day = ARGV[0].to_i.to_s # remove leading zeroes
year = ARGV[1] || 2022
two_digit_day = format('%02d', day)
input_directory = File.expand_path("#{year}/inputs")
solution_directory = File.expand_path("#{year}/#{two_digit_day}")
template_path = File.expand_path('2022/04')

FileUtils.mkdir(input_directory) unless File.directory?(input_directory)
FileUtils.mkdir(solution_directory) unless File.directory?(solution_directory)
unless File.exist?(File.join(solution_directory, "#{two_digit_day}.rb"))
  FileUtils.cp("#{template_path}/04.rb", "#{solution_directory}/#{two_digit_day}.rb")
end
unless File.exist?(File.join(solution_directory, "#{two_digit_day}.py"))
  FileUtils.cp("#{template_path}/04.py", "#{solution_directory}/#{two_digit_day}.py")
end

uri = URI("https://adventofcode.com/#{year}/day/#{day}/input")
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

request = Net::HTTP::Get.new(uri)
request['Cookie'] = "session=#{cookie}"
# per https://www.reddit.com/r/adventofcode/comments/z9dhtd
request['User-Agent'] = 'github.com/seemaullal/advent-of-code/blob/main/gi.rb by seemaullal at gmail dot com'
response = http.request(request)

File.write("#{input_directory}/#{day}.txt", response.read_body)
system('open', "https://adventofcode.com/#{year}/day/#{day}")
