from fabric import task

@task
def list(c):
    c.run('fab --list')

@task
def freeze(c):
    c.run('uv pip freeze > requirements.txt')

@task
def sync(c):
    c.run('uv pip sync requirements.txt')

@task
def mysqlStart(c):
    c.run('docker compose up -d')

@task
def mysqlEnd(c):
    c.run('docker compose down')

@task
def mg_auto(c):
    c.run('alembic revision --autogenerate')

@task
def mg_head(c):
    c.run('alembic upgrade head')
