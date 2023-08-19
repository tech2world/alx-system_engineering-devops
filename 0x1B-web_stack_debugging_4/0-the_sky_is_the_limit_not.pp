# Increase the ULIMIT of the default file
exec { 'fix-for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "ULIMIT=-n 15" /etc/default/nginx', # Corrected grep syntax
}

# Restart Nginx
service { 'nginx':
  ensure   => 'running',
  enable   => true,
  require  => Exec['fix-for-nginx-ulimit'],
  subscribe => Exec['fix-for-nginx-ulimit'], # Make sure the service restarts after the exec changes the ulimit
}
