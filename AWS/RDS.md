# RDS

## Create Definition

- launch an existing ec2 instance
- install mysql-client
- DB definiton
  - standard create
  - mysql
  - free tier
  - set master password
  - connect to an ec2 instance
  - choose the instance
  - create a new secgroup
  - create database

## Download db

```bash
curl -LO https://gitlab.com/Reece-Elder/devops-m5-rds/-/raw/main/sample_data_movies_mysql.sql
```

import db

```bash
mysql -h <connection_url>  -u admin -p < sample_data_movies_mysql.sql
mysql -h <connection_url>  -u admin -p 
```


