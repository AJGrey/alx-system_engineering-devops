# A puppet code to edit a file  error on a server

$filePath = '/var/www/html/wp-settings.php'
$searchString = 'phpp'
$replacementString = 'php'

exec { 'replace_line':
  command => "sed -i 's/${searchString}/${replacementString}/g' ${filePath}",
  path    => ['/bin', '/usr/bin'],
}
