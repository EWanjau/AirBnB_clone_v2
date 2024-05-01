#!/usr/bin/python3
"""Create and distribute an archive to the servers,
    using function deploy
"""
from fabric.api import put, run, env
from os import path

env.user = 'ubuntu'
env.hosts = ['100.25.157.156', '100.25.215.129']


def do_deploy(versions/web_static_20240501125237.tgz):
    """function to deploy an archive to the servers"""
    if path.exists(versions/web_static_20240501125237.tgz) is False:
        return False

    archive = versions/web_static_20240501125237.tgz.split('/')[1]
    folder = archive[:-4]

    try:
        put(versions/web_static_20240501125237.tgz, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(folder))
        run("tar -xzf /tmp/{} -C \
            /data/web_static/releases/{}".format(archive, folder))
        run("rm /tmp/{}".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}".format(folder, folder))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
            /data/web_static/current".format(folder))
        print('New release deployed!')
        return True
    except:
        return False
