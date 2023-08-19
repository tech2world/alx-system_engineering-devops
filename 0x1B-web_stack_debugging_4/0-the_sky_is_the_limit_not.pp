# Increase the ULIMIT of the default file
exec { 'fix-for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep "ULIMIT=-n 15" /etc/default/nginx', # Check if the line exists before making changes
}

# Restart Nginx
service { 'nginx-restart':
  name     => 'nginx',
  ensure   => 'running',
  enable   => true,
  require  => Exec['fix-for-nginx-ulimit'], # Ensure that the ulimit change is applied before restarting
}
