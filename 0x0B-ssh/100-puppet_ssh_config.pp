file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "\
# This line manages the PasswordAuthentication setting
PasswordAuthentication no

# This line manages the IdentityFile setting
IdentityFile ~/.ssh/school
",
}
