# SSH Helper
A python script that reads your ~/.ssh/config file and maintains a json file, to allow easy lookup/connections

# Requirements

- Linux or Mac OS (tested on linux)
- Python3
- A prepared `~/.ssh/config` file https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/

# Installation / Use

1. `git clone https://github.com/d4rkd0s/ssh-helper`

2. `cd ssh-helper`

3. Edit the script and add your username

```
# Your username
username = ""
```
Change to whatever your `/home/yourname` is (Linux/Mac OS)
```
# Your username
username = "yourname"
```

4. Run it, first time, it will generate `~/.ssh/connections.json` used by the script as an intermediate layer (only file read permissions are needed for `~/.ssh/config` as it builds the `connections.json` for read/write.

5. A list of servers will display

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

6. Pick one and connect, Whoosh!

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
- [ ] Ability to manage (add/modify/remove) servers to your `~/.ssh/config` file using `ssh_helper.py`
