# pygpg

encrypt files use gpg tools via python.



Usage:

```
python pygpg <path>
```

Only test in linux with a non-root user.


edit davfs config file(/etc/davfs2/secrets), 
the file content is as blow:
```
http://<ip or domain>:<port>/<path>        <username>   <password>
```

mount netdisk via webdav(alist service:
```
sudo mount.davfs "http://alist.lifang.fun:5244/dav" /mnt/aliyunpan -o uid=1000,gid=1000 
```

or, you can mount a sharefolder in lan. and then, sync files to sharefolder, and then, copy sharefolder to netdisk manually.
for example:
```
sudo mount -t cifs -o username=myuser,password=123456 //alist.lifang.fun/阿李照相馆 /mnt/pc16
```

use rsync to sync files from nas to netdisk.
```
sudo rsync -avrP --include="*/" --include="*.gpg" --exclude="*" "<source>" "<dest>"
```
for example:
```
sudo rsync -avrP --include="*/" --include="*.gpg" --exclude="*" "/data2/samba/safe_share/阿李照相馆" "/mnt/aliyunpan/数据备份/阿李照相馆"
```