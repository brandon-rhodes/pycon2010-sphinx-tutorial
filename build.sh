#!/bin/bash

set -e  # exit on errors
cd $(dirname "$0")
mkdir thumb
cd thumb

mkdir python-windows
cd python-windows
wget http://www.python.org/ftp/python/2.7.1/python-2.7.1.msi
wget http://www.python.org/ftp/python/2.7.1/python-2.7.1.amd64.msi
cd ..

mkdir python-mac
cd python-mac
wget http://www.python.org/ftp/python/2.7.1/python-2.7.1-macosx10.3.dmg
wget http://www.python.org/ftp/python/2.7.1/python-2.7.1-macosx10.6.dmg
cd ..

mkdir python-source
cd python-source
wget http://www.python.org/ftp/python/2.7.1/Python-2.7.1.tgz
cd ..

mkdir virtualenv
cd virtualenv
wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.5.1.tar.gz#md5=3daa1f449d5d2ee03099484cecb1c2b7
tar xvzf virtualenv-1.5.1.tar.gz virtualenv-1.5.1/virtualenv.py
mv virtualenv-1.5.1/virtualenv.py virtualenv.py
rmdir virtualenv-1.5.1
cd ..

mkdir sphinx
cd sphinx

wget http://pypi.python.org/packages/2.4/P/Pygments/Pygments-1.4-py2.4.egg#md5=619325b28c60a1ac96ba1c9b301149c6
wget http://pypi.python.org/packages/2.5/P/Pygments/Pygments-1.4-py2.5.egg#md5=c8979b9844ad9e39aeaf9469185a70a4
wget http://pypi.python.org/packages/2.6/P/Pygments/Pygments-1.4-py2.6.egg#md5=306241dd68799753cdb4a2c9ce8e883a
wget http://pypi.python.org/packages/2.7/P/Pygments/Pygments-1.4-py2.7.egg#md5=acbdde4dae30efaba8cfa86dcb6070f2
wget http://pypi.python.org/packages/source/P/Pygments/Pygments-1.4.tar.gz#md5=d77ac8c93a7fb27545f2522abe9cc462

wget http://pypi.python.org/packages/2.4/S/Sphinx/Sphinx-1.0.7-py2.4.egg#md5=f77624e49a3a2bf45d7262722cf51bbb
wget http://pypi.python.org/packages/2.5/S/Sphinx/Sphinx-1.0.7-py2.5.egg#md5=f1607f94e0431bad74fabd18366fdbbf
wget http://pypi.python.org/packages/2.6/S/Sphinx/Sphinx-1.0.7-py2.6.egg#md5=a547658740040dd87ef71fbf723e7962
wget http://pypi.python.org/packages/2.7/S/Sphinx/Sphinx-1.0.7-py2.7.egg#md5=1321a3888d4fad656a5ede5838686e12
wget http://pypi.python.org/packages/source/S/Sphinx/Sphinx-1.0.7.tar.gz#md5=42c722d48e52d4888193965dd473adb5

cd ..

hg clone ssh://hg@bitbucket.org/brandon/pycon2010-sphinx-tutorial tutorial
rm -rf tutorial/.hg
