#!/usr/bin/env ruby
#accepts one arg and pass it to a regexp matching method

puts ARGV[0].scan(/hbt{2,5}n/).join
