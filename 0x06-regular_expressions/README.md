# Regular expression

## Language
Bash | Ruby

### also can work in ``python`` or ``javascript``

name of the project → ****0x06. Regular expression****
<br>
#
## About Bash projects
Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

````
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
````
## Authors

[Santiago Neira](https://github.com/sanei1509)
