#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import pygithub3
import sys
import os

gh = None

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

Banner = """\033[37m
╔═╗┌─┐┌┬┐    ╦═╗┌─┐┌─┐┌─┐┌─┐┬┌┬┐┌─┐┬─┐┬┌─┐┌─┐
║ ╦├┤  │0.0.2╠╦╝├┤ ├─┘│ │└─┐│ │ │ │├┬┘│├┤ └─┐
╚═╝└─┘ ┴     ╩╚═└─┘┴  └─┘└─┘┴ ┴ └─┘┴└─┴└─┘└─┘
\033[91m         https://github.com/byRo0t96\033[37m\n"""

cls()

print (Banner)


try:
    user = sys.argv[1]
    def gather_clone_urls(organization, no_forks=True):
        all_repos = gh.repos.list(user=organization).all()
        for repo in all_repos:
            if no_forks and repo.fork:
                continue
            yield repo.clone_url

    if __name__ == '__main__':
        gh = pygithub3.Github()

        clone_urls = gather_clone_urls(user)
        for url in clone_urls:
            final0 = str(url.replace("https://github.com/",""))
            final1 = str(final0.replace(".git",""))
            final = str(final1.replace("hub.io",".github.io"))
            txtfile=("{}.txt".format(user))
            fs=open(txtfile, "a+".format(user))
            fs.write("{}\n".format(final))
        print ("all repositories is listed in {}.txt file".format(user))


except:
    print('Usage: python start.py username\n')
    sys.exit()


