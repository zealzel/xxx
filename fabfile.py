from fabric import task


host = 'zealzel@172.104.163.189'


@task
def whoareu(c):
    c.run('ls -al')
