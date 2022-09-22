# Error 500 (internal error)
# cambiamos todos los phpp que hayan en la config por php:
# dentro de la config php -> path "/var/www/html/wp-settings.php"

exec {'Solution to internal error 500':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell
}