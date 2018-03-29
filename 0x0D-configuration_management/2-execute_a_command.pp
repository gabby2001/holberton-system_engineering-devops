exec { 'kill a process':
  command   => 'pkill -f killmenow'
}
