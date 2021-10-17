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

package{ 'flask-cors':
  ensure   => installed,
  provider => 'pip'
}

package{ 'setuptools':
  ensure   => installed,
  provider => 'pip'
}

package{ 'flasgger':
  ensure   => installed,
  provider => 'pip'
}

package{ 'mysqlclient':
  ensure   => installed,
  provider => 'pip'
}

package{ 'bcrypt':
  ensure   => installed,
  provider => 'pip'
}

package{ 'SQLAlchemy==1.2.5':
  ensure   => installed,
  provider => 'pip'
}

package{ 'pyjwt==1.4.2':
  ensure   => installed,
  provider => 'pip'
}

exec{ 'Clone application repository':
  command  => 'git clone https://github.com/adrienmillot/holberton_portfolio.git',
  provider => 'shell'
}

file{ 'API service creation':
  ensure  => present,
  path    => '/etc/systemd/system/ss_api.service',
  content => '[Unit]\nDescription=Survey storm API\nAfter=networ.target\n\n[Service]\nUser=ubuntu\nGroup=ubuntu\nExecStart=/home/ubuntu/.local/gunicorn --worker 3 --access-logfile /tmp/ss-access.log --error-logfile /tmp/ss-error.log --bind 0.0.0.0:5003 api.v1.app:app\n\[Install]\nWantedBy=multi-user.target',
}
