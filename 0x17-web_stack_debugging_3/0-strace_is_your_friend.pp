# Fix typo in file
exec { 'fix typo':
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  provider => 'shell'
}
