# Permitir una mayor cantidad de solicitudes

exec {'remplazar en la config':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
  provider => 'shell'
}

exec { 'reseteo del server nginx':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}}
