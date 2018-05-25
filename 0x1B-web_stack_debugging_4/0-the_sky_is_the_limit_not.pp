exec { 'increase file limit':
  command  => 'sed -i "\$aULIMIT=\"-n 3000\"" /etc/default/nginx; service nginx restart',
  provider => 'shell'
}
