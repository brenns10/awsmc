AWS-MC Architecture
===================

Packages
--------
- For controlling AWS: boto3
- For controlling EC2 instances: paramiko

Components
----------
- Everything is combined in single script, `awsmc`
- Client commands will use boto to create / modify AWS resources
- Server commands will be called from the client over SSH

Commands
--------
Commands prefixed by `server_` are run only on the server.
- `awsmc init <name>` - create AWS instance and shut it down
- `awsmc start <name>` - start server
- `awsmc stop <name>` - stop server
- `awsmc restart <name>` - restart server
- `awsmc shell <name>` - go into the server shell
- `awsmc backup <name> <s3://bucket/destination` - backup world
- `awsmc server_init`
- `awsmc server_start`
- `awsmc server_stop`

Initialization Commands
-----------------------
Can build the server on the client and send it across, saves time.
```bash
sudo apt install git default-jre
mkdir build; cd build
git config --global --unset core.autocrlf
sed -i'' 's/false/true/' eula.txt
```
