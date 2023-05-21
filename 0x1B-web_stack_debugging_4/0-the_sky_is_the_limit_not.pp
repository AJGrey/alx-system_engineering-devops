#increase the limit of nginx traffic
#edit the ulimit

exec { 'edit-file':
  command     => 'sed -i "s/15/4096/" /etc/default/nginx',
  path        => ['/usr/local/bin', '/bin/'],
  refreshonly => true,
  notify      => Exec['restart-nginx'],
} ->

exec { 'restart-nginx':
  command     => 'service nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
}
