#!/usr/bin/env ruby
#only 10 digitos, marcamos principio y final
puts ARGV[0].scan(/^\d{1,10}$/).join
