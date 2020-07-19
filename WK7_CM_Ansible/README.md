# Description

This is to demo the generic usage of Ansible.

# Tasks

## Task #1: Install Ansible
Install Ansible, boto3 and botocore via pip3. We install boto3 because it's required by Ansible Inventory EC2 plugin. 
```
pip3 install ansible boto3 botocore
```
Validate by executing `ansible --version` and check it's using python3.

Alternatively, you can follow https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

You can play around by checking localhost, so you can control your machine :)

```bash
ansible localhost -v -a 'ls'
```

Note -v means verbose mode. You can add more verbose like `-vvvv`

## Task #2: Create a EC2 machine in AWS to ssh

- Get a ssh public key in your local machine. 
```
cat ~/.ssh/id_rsa.pub
```
- Import your ssh public key into AWS as a key pair.
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName

![Alt text](images/ansible-keyimport.png?raw=true)

- Create a EC2 machine with default VPC and subnet

  Select a Ubuntu image as free-tier.

![Alt text](images/ansible-ubuntu.png?raw=true)

  create a Security Group with ssh and http
![Alt text](images/ansible-ec2-sg.png?raw=true)

  select the existing key pair as imported above
![Alt text](images/ansible-keypair.png?raw=true)

- SSH the EC2 machine in AWS EC2 service

Get the ip address

![Alt text](images/ansible-ec2-ip.png?raw=true)

SSH the instance in your local machine
```
ssh ubuntu@<ip address from aws ec2>
```

## Task #3: Install Nginx on Ubuntu

- Go to `ansible-nginx` folder and run the command as below

```
ansible-playbook -i <ec2 ip address>, nginx_install.yaml
```

Explanation:
- i inventory: it tells Ansible which hosts to apply. The default location for inventory is a file called /etc/ansible/hosts. You can specify a different inventory file at the command line using the -i <path> option. 
  
  see detail https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
  
- *.yml playbook

- Inspect the terminal 

![Alt text](images/ansible-terminal.png?raw=true)

- check if Nginx is installed correctly

visit the IP address
![Alt text](images/ansible-nginx.png?raw=true)

Some explanation on Playbook:

Playbooks are the files where Ansible code is written. Playbooks are written in YAML format. YAML stands for Yet Another Markup Language. 

Playbooks are one of the core features of Ansible and tell Ansible what to execute. They are like a to-do list for Ansible that contains a list of tasks.

Playbook Structure:
- It is a YAML file. Be careful with indention.

- Start with --- (3 hyphens)

- name: This tag specifies the name of the Ansible playbook. As in what this playbook will be doing. Any logical name can be given to the playbook.

- hosts: This tag specifies the lists of hosts or host group against which we want to run the task. The hosts field/tag is mandatory. It tells Ansible on which hosts to run the listed tasks. The tasks can be run on the same machine or on a remote machine. One can run the tasks on multiple machines and hence hosts tag can have a group of hosts’ entry as well.

- tasks: All playbooks should contain tasks or a list of tasks to be executed. Tasks are a list of actions one needs to perform. A tasks field contains the name of the task. This works as the help text for the user. It is not mandatory but proves useful in debugging the playbook. Each task internally links to a piece of code called a module. A module that should be executed, and arguments that are required for the module you want to execute.

- become: Ansible allows you to ‘become’ another user, different from the user that logged into the machine (remote user).
  
  see [Some examples](https://www.middlewareinventory.com/blog/ansible-sudo-ansible-become-example/#:~:text=Ansible%20Sudo%20or%20become%20is,user%20or%20some%20other%20user.&text=become%20and%20become_user%20both%20have,someuser%20before%20running%20a%20task)

## Task #4: Uninstall and config Nginx

- Uninstall: In order to allow us to see the full cycle we would like to check how to uninstall Nginx. This is the playbook we are going to use.

```
ansible-playbook -i <ec2 ip address>, nginx_uninstall.yaml
```

- Config Nginx to display a static html file

```
ansible-playbook -i <ec2 ip address>, nginx_update.yaml
```

Tip: 
- find modules from https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
- `--check` The check mode allows you to run in dry-run mode, without making any change.

It is fine to install on a remote machine, what about more machines?

## Task #5: Create AWS EC2 instances in us-east-1 region using CloudFormation

- Use this [cloudformation template](CFN-EC2.yaml) to create EC2 instances for our handson: https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template

We are going to deploy the sample app -https://github.com/JiangRenDevOps/jrcms

We can use the default VPC and its corresponding subnet. Then go head creating the stack.

While it is being created, let us have a walkthrough at both the project and cloud formation before going next.

Inspect what have been created, e.g. checking ec2 service and instance tags.

After the creation is successful, you should be able to ssh the public IP of the instance.

## Task #6: Manually config client machines in Ansible hosts
- List the machines in the default inventory `etc/ansible/hosts`
```bash
sudo vi /etc/ansible/hosts
```
Note: It is the default inventory location. Create a directory if you don't have it

```bash
sudo mkdir -p /etc/ansible
```


- Write the IP address into the file, and then save it
```bash
[web]
<public ip from aws cloudformation output>
<public ip from aws cloudformation output>

[redis]
<public ip from aws cloudformation output>
```

- Checkout the inventory graph
```bash
ansible-inventory --graph
```

- Execute to ping all machines. You should be able to see the success results from it.
```bash
ansible all -m ping -u ubuntu
```
![Alt text](images/ansible-ping.png?raw=true)

We can also play around by adding a file like
```bash
ansible all -u ubuntu -a "touch michael"
```

```bash
ansible all -u ubuntu -a "ls -la"
```

## Task #7: Automatically detect client machines 

It is not efficient to manually config the list when managing more machines. So we can configure the following to automatically detect client machines from AWS. We need to create an IAM user and configuring three environment variables.

Get the value from your AWS console.
```
export AWS_ACCESS_KEY=YOUR_AWS_ACCESS_KEY
export AWS_SECRET_KEY=YOUR_AWS_SECRET_KEY
export ANSIBLE_HOST_KEY_CHECKING=False
```
Note: ANSIBLE_HOST_KEY_CHECKING=False is to skip checking host key. see https://docs.ansible.com/ansible/latest/reference_appendices/config.html

## Task #8: Validate the setup of the EC2 instances
```
cd DevOpsLectureNotes2/WK7_CM_Ansible/ansible-playbooks
ansible all -i inventory.aws_ec2.yaml -u ubuntu -m ping
```
You should be able to ping three machines from AWS

Also, you can view the inventory by executing the following:
```bash
ansible-inventory -i inventory.aws_ec2.yaml --graph
```
![Alt text](images/ansible-graph.png?raw=true)

Note: the display list is no longer IPs.

## Task #9: Install a docker role from galaxy to your local laptop

Use `ansible-galaxy install -r requirements.yaml`

Alternatively, you can install it directly
```
ansible-galaxy install -c geerlingguy.docker
```

## Task #10: Read playbook under ansible-playbook-plain and execute
Read `site.yaml` under `ansible-playbook-plain`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```

Note there is a check flag to inspect if there are any errors. If not, run without flag to execute for real.

If you don't see errors, you should be able to view the app from one of the web server.
![Alt text](images/ansible-result.png?raw=true)

![Alt text](images/app-ec2.png?raw=true)

## Task #11: Read playbook under ansible-playbook-roles and execute
Read `site.yaml` under `ansible-playbook-roles`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```

Some explanation on Roles

In Ansible, the role is the primary mechanism for breaking a playbook into multiple files. This simplifies writing complex playbooks, and it makes them easier to reuse. The breaking of playbook allows you to logically break the playbook into reusable components.

Each role is basically limited to a particular functionality or desired output, with all the necessary steps to provide that result either within that role itself or in other roles listed as dependencies.

Roles are not playbooks. Roles are small functionality which can be independently used but have to be used within playbooks. There is no way to directly execute a role. Roles have no explicit setting for which host the role will apply to.

Top-level playbooks are the bridge holding the hosts from your inventory file to roles that should be applied to those hosts.

Tip: Exam a role file structure - `ansible-galaxy init role1`

## Task #12: Install more software via Ansible and play around
Install sth like Jenkins, Kubernetes, Wordpress etc.
