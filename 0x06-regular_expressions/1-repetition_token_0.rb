#!/usr/bin/env bash
#reg exp. to find h, b y t de 2 a 5 veces

puts ARGV[0].scan(/hbt{2,5}n/).join
