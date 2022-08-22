# automatizar la tareas realizada en la task 0

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install_Nginx'],
}

# instalar nginx:
exec {'install_Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['custom_header'],
}

exec { 'custom_header':
  provider => shell,
  command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
  before   => Exec['reiniciar_nginx'],
}

# reiniciar servidor nginx
exec { 'reiniciar-nginx': # se puede poner cualquier nombre aca
  command  => 'sudo service nginx restart', # Aca se le pasa el comando a ejecutar
  provider => 'shell' # Se le indica donde se va a correr
  }