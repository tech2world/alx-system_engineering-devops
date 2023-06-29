# puppet script to create config file
file_line {'password auth': 
  ensure   => 'present',
  path      => '/etc/ssh/ssh_config',
  line      => '    PasswordAuthentication no',
  #after    => undef,
  #match    => undef, # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}

file_line {'set identity file': 
  ensure   => 'present',
  path      => '/etc/ssh/ssh_config',
  line      => '    IdentityFile ~/.ssh/school',
  #after    => undef,
  #match    => undef, # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}
