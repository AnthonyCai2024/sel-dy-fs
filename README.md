# sel-dy-fs

## 先启动chrome实例, 再登录, 这时候打开抖音,是已经登录的状态

```bash
start chrome --remote-debugging-port=9222 --user-data-dir="D:\data\chrome\data\dy"
```

## 再执行程序

```bash
python auto-instancy.py
```