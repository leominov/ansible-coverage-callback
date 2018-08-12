import os
import re

from os.path import expanduser
from setuptools import setup, find_packages
from setuptools.command.install import install


READMEFILE = "README.md"
VERSIONFILE = os.path.join("callback_plugins", "coverage.py")
VSRE = r"CALLBACK\_VERSION\s\=\s['\"]([^'\"]*)['\"]"


def get_version():
    verstrline = open(VERSIONFILE, "rt").read()
    re_result = re.search(VSRE, verstrline, re.M)
    if re_result:
        return re_result.group(1)
    else:
        raise RuntimeError(
            "Unable to find version string in %s." % VERSIONFILE)

class Installer(install):
    def run(self):
        # Regular install
        install.run(self)

        print 'Creating Ansible Callback symlink'

        home = expanduser('~')
        callback_plugins_dir = os.path.join(home, '.ansible/plugins/callback_plugins')
        callback_plugins_dist_file = os.path.join(self.install_lib, 'callback_plugins', 'coverage.py')
        callback_plugins_user_file = os.path.join(callback_plugins_dir, 'coverage.py')

        if not os.path.exists(callback_plugins_dir):
            os.makedirs(callback_plugins_dir)

        if os.path.exists(callback_plugins_user_file):
            os.remove(callback_plugins_user_file)

        os.symlink(callback_plugins_dist_file, callback_plugins_user_file)

        print 'Done'

setup(
    name='ansible-coverage-callback',
    version=get_version(),
    description='Simple Ansible Coverage callback',
    long_description=open(READMEFILE).read(),
    url='https://github.com/leominov/ansible-coverage-callback',
    author='Lev Aminov',
    author_email='l.aminov@tinkoff.ru',
    license='MIT',
    packages=find_packages(),
    cmdclass={'install': Installer},
    install_requires=[
        'ansible>=2.4'
    ],
    include_package_data=True,
    zip_safe=False
)
