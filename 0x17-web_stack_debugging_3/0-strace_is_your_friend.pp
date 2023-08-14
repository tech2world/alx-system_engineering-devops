# puppet file to replace a line on the server
# change phpp to php

exec { 'replace_line':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
