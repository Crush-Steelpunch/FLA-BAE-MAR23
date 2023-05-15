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

## ansible-doc

``bash
ansible-doc <module>
ansible-doc -l
```