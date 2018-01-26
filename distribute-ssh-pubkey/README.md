### distribute-pubkey

一键分发ssh公钥
安装依赖
```
pip3 install -r requirements.txt
```
还需openssh,与sshpass
安装
```
sudo -H python3 setup.py install
```
使用
```
distribute_pubkey -f <filepath>
```
测试
启动测试环境
```
cd test
docker-compose up -d
distribute_pubkey -f hosts
```
登录,无需密码
```
ssh root@127.0.0.1 -p45521
```
