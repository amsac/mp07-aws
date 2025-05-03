# mp07-aws

prometheus command

docker run -it -d -p 9090:9090 -u root -v "$PWD/prometheus.yml:/etc/prometheus/prometheus.yml" -v "$PWD/prometheus-data:/prometheus" --name=prom_cont prom/prometheus