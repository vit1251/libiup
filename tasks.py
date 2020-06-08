
from invoke import task

@task
def prepare(c):
    """ Prepare builddir
    """
    c.run('rm -rf builddir', echo=True, pty=True)
    c.run('meson builddir', echo=True, pty=True)

@task(default=True, pre=[prepare])
def build(c):
    """ Build
    """
    c.run('ninja -C builddir', echo=True, pty=True)
