#!/usr/bin/env bash
#string que empieza con h y termina con n
#^ -> indicamos comienzo
#? -> indica el final del string 

puts ARGV[0].scan(/^h.n$)
