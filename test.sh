lftp -u test,test ftp://10.156.114.17 -e 'mirror -R --exclude-glob "*.mp4" --exclude-glob ".*" /storage/emulated/0/dcim' > /dev/null 2>&1
