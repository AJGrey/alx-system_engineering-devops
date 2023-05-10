# A puppet code to edit a file  error on a server

$file_path = '/var/www/html/wp-settings.php'
$search_string = 'phpp'
$replacement_string = 'php'

exec { 'replace_line':
  command => "sed -i 's/${search_string}/${replacement_string}/g' ${file_path}",
  path    => ['/bin', '/usr/bin']
}
