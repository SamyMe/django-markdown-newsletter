###Mind refreshing: 

Help for upload : http://peterdowns.com/posts/first-time-with-pypi.html

1. Register package name : python setup.py register
2. To update package: 
	- make details and push them to github
	- *git tag x.y -m "message"*
	- *git push --tags origin master*
	- update version in *setup.py* to *x.y* (version & download_url)
	- *python setup.py sdist upload*


----------------------
Delete remote Git tag:
----------------------
git tag -d 12345
git push origin :refs/tags/12345
