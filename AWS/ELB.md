## install steps

```bash
sudo apt update; sudo apt install nginx -y
echo $(hostname) | sudo tee /var/www/html/index.nginx-debian.html
```