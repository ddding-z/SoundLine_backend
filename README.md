# soundline后端

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





## 数据库设计

学校云平台 数据库

User { username, password, token(?), file : [{id,name,content}, {}, {}, {}] }

Folder { id, user_id, name, create_time, files : [ {id,name}, {id}, {} ] }

## 后端功能