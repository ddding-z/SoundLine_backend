# Soundline后端

## 需求

登录 传入（账号密码） 返回（状态 账号名）**POST**

注册 传入（账号密码） 返回（状态）**POST**

Start 传入 （账号 页码 每一页文件数） 返回 （账号所拥有的笔记）**GET**

Start 传入 （账号） 返回 （状态） 后端（随机给文件夹生成名字）**GET**

Start 新建笔记 跳转至文件详情页面  

Start 上传音频并新建笔记 传入 （账号） 返回 （笔记内容（大纲））**GET**

Recents 传入（账号 页码 每一页文件数） 返回 （账号所拥有的笔记）--- 接口同Start **GET**

Folders 传入（账号 页码 每一页文件夹数） 返回 （账号所拥有的文件夹）--- 接口同Start **GET**

文件详情页面 传入 （账号 文件id） 返回 （文件具体内容和信息）**GET**

文件详情页面修改 传入 （账号 文件id 文件内容） 返回 （状态）**PUT**

文件详情页面新建 传入 （账号 文件内容） 返回 （状态）**POST**

文件详情页面chat 传入 （账号 问题内容） 返回 （问题对应答案）**POST**

文件夹详情页面 传入 （账号 文件夹id） 返回 （文件夹所有包含的笔记 以及 信息）**GET**

```json
response:{msg: 1,  username:'',....} // 1--成功 0--失败
```

## 后端如何读取请求传入参数

### PUT和POST

```python
@app.route('/login', methods=["POST", "PUT"])
def login():
	username = request.json.get("username")
```

### GET

```python
@app.route('/login', methods=["GET"])
def login():
	username = request.args.get("username")
```
## 项目布局
```
SoundLine_backend:.
│  .gitignore
│  README.md
│  requirements.txt
├─.idea
├─flaskr
│  │  auth.py # 登录
│  │  db.py # 数据库初始化
│  │  document.py # 文档详情
│  │  folder.py # 文件夹详情
│  │  recent.py # recent界面
│  │  schema.sql # 数据库定义
│  │  start.py # start界面
│  │  __init__.py # 应用初始化
│  │  
│  └─__pycache__
│
└─instance # sqlite数据库
        flaskr.sqlite
```      

## 数据库

设计 见schema.sql

初始化

```shell
$ flask init-db
```

## 运行

```cmd
# cmd
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run

#powershell
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run

# 可以将看到类似的输出：
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```

