# create a custom header using puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure  => 'present',
}
-> file_line {'http_header':
  path  => '/etc/nginx/nignix.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => 'usr/sbin/service nginx restart',
}
