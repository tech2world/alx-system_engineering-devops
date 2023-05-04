#!/usr/bin/env ruby
#accept one arg then pass it to the regexp matching method

puts ARGV[0].scan(/[A-Z]/).join
