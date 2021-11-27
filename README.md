<h1 align="center">Welcome to Auth microservice flask 👋</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: GNU GENERAL PUBLIC LICENSE 3" src="https://img.shields.io/badge/License-GNU GENERAL PUBLIC LICENSE 3-yellow.svg" />
  </a>
</p>

> this is a authentication service with Python and Flask

## Install
Python >= 3 and docker must be installed on your system then:
```sh
export AUTHMAN_DATABASE_URI = mysql+pymysql://root:test@localhost:3306/auth_microsevice_flask

docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=test mysql

```
or

RUN any sql database with docker. 
for see all configuration local variable see auth_microservice_flask/config/conig.py to export


```sh
pip install -r requirements.txt

flask db init

flask db migrate

flask run
```
or you can run it by docker

finally open localhost:5000/api/v1 on your browser

## Author

👤 **khalil farashiani**

* Website: Jezza.ir
* Github: [@khalil-farashiani](https://github.com/khalil-farashiani)

## Show your support

Give a ⭐️ if this project helped you!

***
