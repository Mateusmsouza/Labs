# Reproducing

- To create the environment run `docker-compose up`. Grafana will be exposed at http://127.0.0.1:3000.
- Before connecting Grafana to MySQL, create an user acessible by any host. By default, root user is only acessible from MySQL container.
`bash
$ mysql -u root -p mysql
mysql> CREATE USER 'chuchu'@'%' IDENTIFIED BY 'chuchu';
mysql> grant all on *.* to 'chuchu'@'%';
`
- Connect Grafana to MySQL using recently created user. Check the container IP inspecting the MySQL container.
