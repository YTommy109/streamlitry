from fabric import task


@task
def list(c):
    c.run('fab --list')

@task
def run(c):
    c.run('streamlit run src/app.py')

@task
def test_watch(c):
    c.run('pytest-watcher .')

@task
def coverage(c):
    c.run('pytest --cov --cov-branch')

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
def mg_auto(c, msg):
    cmd = 'alembic revision --autogenerate'
    if msg:
        cmd += f' -m "{msg}"'
    c.run(cmd)

@task
def mg_head(c):
    c.run('alembic upgrade head')

@task
def mg_down(c):
    c.run('alembic downgrade -1')

@task
def mg_reset(c):
    c.run('alembic downgrade base')
