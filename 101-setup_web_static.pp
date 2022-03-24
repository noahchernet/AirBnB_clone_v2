# Sets up your web servers for the deployment of web_static

exec {'setup_web_static':
  command  => '
  ./0-setup_web_static.sh
  ',
  provider => 'shell'

}
