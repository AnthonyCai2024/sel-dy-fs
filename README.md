# sel-dy-fs

## 先启动chrome实例, 再登录, 这时候打开抖音,是已经登录的状态

```bash
start chrome --remote-debugging-port=9222 --user-data-dir="D:\data\chrome\data\dy"
```

## 再执行程序

```bash
python auto-instancy.py
```

## todo

### 1. 优化代码

### 2. 增加参数设置,需要独立出来,容易给用户使用

### 3. 增加日志输出,目前日志太乱

### 4. 修改逻辑

#### 4.1 每天先获取2000个最新的关注粉丝账号,然后再随机从中选择200个账号关注

#### 4.2 每次运行前,先获取自己已关注的账号,避免重复关注

#### 4.3 增加关注计数器,达到一定的数量程序将自动停止


