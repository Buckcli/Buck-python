# Introducing, the next big thing , BUCK .

Buck is a free, lightweight (I'm speaking 4.8kb), open source cli tool designed to help improve your productivity in the terminal.

Now let's see how we can organise multiple commands, in this case, pushing a new version of our app to git with buck all in one single command. .

DISCLAIMER : YOU ARE BROKE.

## Installation

You have to have python and pip installed or node and npm/yarn installed, then you have to SUPPORT ME ON PATREON , even if it's one dollar, it would help a little, sad and virgin ass nerd.


Once you have that all ready,

```sh
pip install buck
```
or
```sh
npm install buck

yarn install buck
```

That should be installed in seconds if you are leaving somewhere definitely not in Nigeria.

## Setup

We are going to be organizing all of these commands into one :

- git add .
- git commit -am "commit message"
- git status
- git push master


Now , run **buck -c or --create command :**

### Name
This is the name of this bucket of commands, you can call it anything, I'd call it git push .

### Commands
These are all the commands you want to run all at once, which in this case are:
git add. , git commit -am $, git status , git push master.

*PLEASE SEPRATE MULTIPLE COMMANDS WITH A ","*

You are probably wondering why we have a $ as the commit message , this is so that we don't have to repeat the same commit message for every push to git. So we add the $, to accept future values(you'd see this in execution)

### Executor

This is the keyword you'd use to run all of these commands, you can go crazy with this and name it anything, I'd just call it push.

### Description (optional)

This is a short message on what the bucket does, you don't really need it .

If you followed all the steps you should have something like this :




Once you have all that setup, **SUPPORT ME ON PATREON.**

It's time to see what we've created in action,clear your terminal for this life changing moment, and run this:

```sh
buck push "your commit message"
```

It is done , folks !. You must became a way more better developer now you can go and work on your billion dollar idea, you can create other buckets to organize multiple commands of your choice whether to deploy to a cloud service provider, setup your projects, update your projects, install a long list of commands in your project and so much more.

Go ahead now! Pip install buck


Please support me by donating to this project . Become a patron sponsor today !.

Check it out the open source code :
https://github.com/Pleasant-tech/Buck

Installation link :
https://pypi.org/project/buck/

Reach out to me :
https://YouTube.com/c/Pleasanttech/
https://Twitter.com/Pleasantech_

