# ssh-helper
A python script that reads your ~/.ssh/config file and maintains a json file, to allow easy lookup/connections. There are more features being added, see the Planned Features section below.

**Requires Python3**

# Installation / Use

1. `git clone https://github.com/d4rkd0s/ssh-helper`

2. `cd ssh-helper`

3. Run it, first time, it will generate `~/.ssh/connections.json` used by the script as an intermediate layer (only file read permissions are needed for `~/.ssh/config` as it builds the `connections.json` for read/write.

4. A list of servers will display

```
[lschmidt@it586g .ssh]$ ssh_helper.py 
1 - util
2 - mca
3 - mcdb
4 - mcadev
5 - mcdbdev
6 - ashstgapp
7 - ashstgweb
8 - ashprdapp
9 - ashprdweb
10 - core
11 - theia
Enter server #: 
```

5. Pick one and connect, Whoosh!

```
Enter server #: 1
Last login: Wed Sep  5 16:28:27 2018 from 10.xx.xx.xx
[lschmidt@util ~]$ 
[lschmidt@util ~]$ 
[lschmidt@util ~]$ 
[lschmidt@util ~]$ exit
logout
Connection to 10.xx.xx.xx closed.
```

# Planned features

- [X] Ability to list servers
- [X] Ability to choose and connect to a server
- [ ] Ability to test connections all at once
- [ ] Ability to update passwords on all servers (using Ansible underneath)
- [ ] Ability to manage servers in your `~/.ssh/config` file using `ssh_helper.py`
