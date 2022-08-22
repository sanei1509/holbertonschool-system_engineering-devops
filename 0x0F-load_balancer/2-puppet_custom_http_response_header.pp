# automatizar la tareas realizada en la task 0

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

#instalar nginx
package {'nginx':
  ensure => present,
}

#intentar crear el header
exec { 'add_header':
  provider => shell,
  command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
  before   => Exec['restart_nginx'],
}

exec {'reiniciar nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}