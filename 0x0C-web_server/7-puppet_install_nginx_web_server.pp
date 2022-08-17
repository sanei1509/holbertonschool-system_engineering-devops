#automatizar tareas de nginx realizadas anteriormente

#instalar nginx
package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

#archivo con hello World en la vista statica
file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World',
}

#redireccion 301 al video de youtube
file_line { 'title':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

