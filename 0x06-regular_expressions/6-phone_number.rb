#!/usr/bin/env ruby
#accepts an arg, pass it to a regexp matching method

puts ARGV[0].scan(/^\d{10}$/).join
