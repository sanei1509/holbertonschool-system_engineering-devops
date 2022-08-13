# automatizar lo que hicimos en la task 2
exec {'/etc/ssh/ssh_config':
  command  => 'echo "	IdentityFile ~/.ssh/school" > /etc/ssh/ssh_config || echo "	PasswordAuthentication no" > /etc/ssh/ssh_config',
  provider => 'shell'
}