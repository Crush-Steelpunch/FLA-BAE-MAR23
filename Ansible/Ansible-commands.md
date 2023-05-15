# Ansible command

```bash
ansible hosts -m <module> -a 'key=val'
ansible 127.0.0.1 -m file -a 'path=ansibleexamplefile state=touch'
ansible 127.0.0.1 -m user -a 'name=leon --become # add become if it needs sudo permissions'
```

## example modules

- command
- ping
- file
- copy
- systemd
- user

## ansible-doc

```bash
ansible-doc <module>
ansible-doc -l
```

## scp

```bash
scp <source> <target>
scp -i <keyfile>  <source> <user>@<targethost>:<path>
#example usage
scp -i ~/Downloads/fla-may15.pem ~/Downloads/fla-may15.pem ubuntu@3.8.182.85:~/
```

## copy

```bash
ansible -i inventory.yaml loadbalancers -m copy -a 'src=nginx-lb.conf  dest=/etc/nginx/nginx.conf' --become
ansible -i inventory.yaml appserver -m copy -a 'src=example-webpage.html  dest=/var/www/html/index.nginx-debian.html' --become
```

## user

```bash
ansible -i inventory.yaml userconfig -m user -a 'name=leon state=present' --become
```

## systemd

`1`bash
ansible -i inventory.yaml loadbalancers -m systemd -a 'name=nginx state=restarted' --become
```