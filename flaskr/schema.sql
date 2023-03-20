DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS folder;
Drop TABLE IF EXISTS document;
Drop TABLE IF EXISTS corpus;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE folder (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    name TEXT UNIQUE NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE document (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  folder_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (author_id) REFERENCES user (id),
  FOREIGN KEY (folder_id) REFERENCES folder (id)
);

CREATE TABLE corpus (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
);

INSERT INTO corpus (ID,question,answer)
VALUES (null,'论文试图解决什么问题','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'这是否是一个新的问题','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'这篇文章要验证一个什么科学假设','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'有哪些相关研究？如何归类？谁是这一类课题在领域内值得关注的研究员？','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'论文中提到的解决方案之关键是什么？','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'论文中的实验是如何设计的？','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'用于定量评估的数据集是什么？代码有没有开源？','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'论文中的实验及结果有没有很好地支持需要验证地科学假设？','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'这篇论文到底有什么贡献','padding');

INSERT INTO corpus (ID,question,answer)
VALUES (null,'下一步呢？有什么工作可以继续深入？','padding');