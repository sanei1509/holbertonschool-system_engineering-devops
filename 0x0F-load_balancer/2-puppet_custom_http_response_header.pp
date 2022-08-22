# automatizar la tareas realizada en la task 0

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

#instalar nginx
package {'nginx':
  ensure => installed,
  name   => 'nginx',
}

#intentar crear el header
file_line { 'custom-header':
  ensure => present,
    path => '/etc/nginx/sites-enabled/default',
  line   => "add_header X-Served-By ${hostname};",
  match  => 'listen 80 default_server;',
}

exec {'reiniciar nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}