# automatizar la tareas realizada en la task 0

#update
exec {'update':
    command  => 'sudo apt-get -y update',
    provider => shell,
    before   => Exec['nginx'],
}

#Instalamos nginx
exec {'nginx':
    command  => 'sudo apt-get -y install nginx',
    provider => shell,
    before  => Exec['custom-header'],
}

#Trying to modify the header
exec {'custom-header':
    provider => shell,
    command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
    before   => Exec['restart'],
}

#Reiniciar nginx
exec {'reiniciar-nginx':
    command  => 'sudo service nginx restart',
    provider => shell
}