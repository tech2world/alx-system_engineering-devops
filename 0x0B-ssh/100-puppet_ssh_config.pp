# puppet script to create config file
file_line {'password auth': 
  line      => '    PasswordAuthentication no',
  path      => '/etc/ssh/ssh_config',
  ensure   => 'present',
  #after    => undef,
  #match    => undef, # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}

file_line {'set identity file': 
  line      => '    IdentityFile ~/.ssh/school',
  path      => '/etc/ssh/ssh_config',
  ensure   => 'present',
  #after    => undef,
  #match    => undef, # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}
