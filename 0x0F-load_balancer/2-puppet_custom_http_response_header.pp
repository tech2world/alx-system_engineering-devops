# create a custom header using puppet

exec {'update':
  command => 'apt-get update -y',
}
-> package {'nginx':
  ensure  => 'present',
}
-> file_line {'http_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "	location / {
  add_header X-Served-By ${hostname};",
  match   => '^\tlocation / {',
}
-> exec {'run':
  command => 'usr/sbin/service nginx restart',
}
