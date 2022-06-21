#!/usr/bin/env ruby
#obtener de los registros de inicio de sesion solo:
#[el que envía(num)] [el que recibe(num)] [flags usadas]
#

puts ARGV[0].scan(/(?<=from:|to:|flags:).join(',')
