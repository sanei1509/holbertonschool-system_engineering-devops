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
#task-> 3
file_line { 'redireccion-301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

#comprobar que nginx este funcionando
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
