#!/usr/bin/env ruby
#"h" y "b" solo una vez, "t" y "n"
#? -> se repite solo una vez


puts ARGV[0].scan(/hb?tn/).join
