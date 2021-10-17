package{ 'git':
  ensure => installed
}

package{ 'python3':
  ensure => installed
}

package{ 'python-pip':
  ensure  => installed,
  require => [ Package['python3'], ]
}

package{ 'flask':
  ensure   => installed,
  provider => 'pip'
}

package{ 'jinga-partials':
  ensure   => installed,
  provider => 'pip'
}

exec{ 'Clone application repository':
  command  => 'git clone https://github.com/adrienmillot/holberton_portfolio.git',
  provider => 'shell'
}

file{ 'Web application service creation':
  ensure  => present,
  path    => '/etc/systemd/system/ss_web_app.service',
  content => '[Unit]\nDescription=Survey storm API\nAfter=networ.target\n\n[Service]\nUser=ubuntu\nGroup=ubuntu\nExecStart=/home/ubuntu/.local/gunicorn --worker 3 --access-logfile /tmp/ss-access.log --error-logfile /tmp/ss-error.log --bind 0.0.0.0:5003 web_flask.app:app\n\[Install]\nWantedBy=multi-user.target',
}
