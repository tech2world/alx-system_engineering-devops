#!/usr/bin/env ruby
#regexp that matches a specified pattern

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',)
