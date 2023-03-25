/*
 Table:
 user{id,username,password}
 folder{id,author_id,foldername,created}
 document{id,author_id,folder_id,content,created}
 corpus{id,question,answer} answer待补充
 summary(id,doc_id,content)
 */

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
    foldername TEXT NOT NULL,
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

/*
  插入测试数据
  username:root, password:12345,user_id:1, folder_id:1, doc_id:1
 */
INSERT INTO user (username, password) VALUES ('root', '12345');

INSERT INTO folder(author_id, foldername) VALUES ('1' , 'default');

INSERT INTO document (author_id, folder_id, content)
VALUES (1, 1, 'This was the meeting of the CVPR 2022 conference. The meeting began with the introduction and introduction of the participants. Then, the participants gave a brief introduction to the conference and the agenda for the next meeting. After that, the meeting moved on to the discussion about the future of the conference. Then the participants talked about the current state of the project and the future plans of the event.

The meeting began with a brief introduction to the current situation of the project. The team was working on a new model for the recognition of human faces, and they were trying to find out how they could improve it. The meeting then moved onto a discussion about the current state of the team and the current challenges they were facing. After that, the team talked about the progress of the current project and the future directions they were going to take it.

 The meeting began with the introduction of the program chair, who gave a brief overview of the current situation of the conference. Then, the meeting moved on to the discussion of the review process, which included a list of outstanding reviewers, who would be honored with a gift certificate for their commitment to CVPR. The meeting ended with the presentation of the results of the first phase of the project, which was the evaluation of the participants'' work.  The meeting began with a brief introduction to the new policies that were introduced this year with the review process. After that, the meeting moved onto a discussion about the process of collecting data for the project. The meeting ended with a discussion on how the project could be improved and how the team could improve the quality of the data.

 The meeting began with a brief introduction to the current situation of the conference. The team was working on the diversity, equity, and inclusion efforts. Then, the team talked about the new policies for the conference, including the new social media policy and the new data contribution policy. The meeting ended with a discussion about the future of the event and how it could be expanded in the future.  The meeting began with a brief introduction to the program and a brief discussion of some of the elements of the program. The meeting was followed by a discussion about the format of the event, which was going to be a speed dating format with mentors moving from table to table to talk to different groups of students through the event. After that, the meeting moved on to a discussion of the remote program chair, Richard Singh, who would be giving a presentation on the remote control of the meeting.

 The first part of the meeting was the introduction of the conference program. The second part was the presentation of the participants'' proposals for the conference. The third part was a presentation on the current state of the project. Finally, the fourth portion was the discussion on the future direction of the program.

 The meeting was about the recent death of Jen Sun, one of the leading researchers in the field of computer vision. The meeting began with a brief introduction of the team and the current situation of the project. Then, the team discussed how they were going to carry out the next phase of research. The team then moved onto a discussion about the future of CVPR in the future. Finally, the meeting ended with a discussion on the current challenges facing the team.

 The PAMI TC presented three awards at CVPR each year: the Longa Higgins Prize, the Young Researcher Award, and the Thomas Wong Memorial Prize. This year''s prize was given to the paper, Are We Ready for Autonomous Driving? by Andreas Geiger, Philip Lentz, and Raquel Erteson. The committee also announced the award for the best student honorable mention, which went to Peter Hedman for his work in the field of neural networks.

 The meeting began with a brief introduction to the team and the current status of the project. The team was working on a project to train a neural network that could model a scene and then render it as a 3D model. They were working with Google to train the model on a variety of different materials and scenes. The meeting ended with the presentation of the results of the model and the discussion of the future directions the project could take.  The team was working on a project to train a neural network that could recognize objects based on their appearance. They were trying to solve the problem of how to train the model and then train it on the real world. To start with, the team discussed how they could improve the performance of the model. Then, they talked about how the model could be improved by adding more information to the data. Finally, they discussed how the team could train their model on the current state of the market and then improve it.  This was the second meeting of the CDPR 2022 meeting. The team was discussing the progress of the project and the future directions it could take. The meeting began with a brief introduction to the team''s current work. Then, the team talked about how they could further improve their model. They discussed how they can add more features to the current model to make it more flexible. Finally, they talked about the future direction of their project and how they would like to further develop it.  The meeting began with a brief introduction to the meeting, followed by a brief discussion on the current state of the project. The meeting ended with a discussion on how the project was progressing and the role of the team in the future.

 The meeting began with a brief introduction to the team and their current project. The team was working on a project to train a deep-learning model that could predict the pose of 3D objects from a single RGB image. After that, the team discussed how they could improve the performance of the model. The meeting ended with a presentation on the current status of the project and the progress of the team.  The meeting began with a brief introduction to the current state of the project. The team was working on training the model on a large data set of images. They were looking at how to improve the performance of the model. Then, the team discussed how they could improve the model by adding more features to it. Finally, they discussed how the model could be improved with the help of other techniques.  The meeting began with a brief introduction to the team and a brief discussion about the current state of the project. The team was working on a project to train a deep-learning neural network that would be able to recognize faces. After that, the team talked about how they could improve the performance of the model. The meeting ended with a discussion on how the team could further improve the model and the progress of the research.

 The meeting began with a brief introduction to the team and their current research project. The team was working on a new way to see sound using a dual-shutter imaging system for sensing low-amplitude, high-frequency vibrations using only regular, low-speed cameras. The group then discussed how they could make their camera see the tiny vibrations of each guitar separately, while being insensitive to the other guitar and the ambient noises. After that, the team presented some experimental results on how they were able to make the system work.  The meeting began with a brief introduction to the team and the team''s current project. The team was working on a new type of microphone that would be able to capture the sound of different frequencies at the same time. They were also working on an advanced version of the chip-based chip recognition system, which would allow them to detect different types of chips at different frequencies. Then, the team talked about how they could use this technology to create a new kind of chip that could be used in a variety of industries. The meeting ended with a presentation on the progress of the project and the next step.  The meeting began with a brief introduction to the project and the team''s work on the project. The team was working on a prototype of a microphone that could pick up the sound of a guitar and send a signal to a microphone. After that, the team talked about how they could improve the quality of the data they were collecting. The meeting ended with a short discussion about the progress of the project, and the next step was to find out what the team could do to improve the results.

 This meeting was about the progress of the team''s work on learning to solve hard minimal problems in computer vision. The team was working with Tim Duff, Anton Lakin, and Thomas Piedler on the project. They were trying to solve the problem of how to reconstruct 3D world from many images. The main problem is that all 272 solutions have to be processed, and only one solution is really meaningful. After that, the team was able to build an intermediate system which is close to the starting system.  The meeting began with a brief introduction to the team''s current project. The team was trying to train a neural network classifier for a new type of image recognition task. They used a combination of machine learning with optimized homotopic continuation to get a fast solver for relative pose between three calibrated cameras from four points in three views. After that, the team discussed how they could improve the performance of their model. The meeting ended with a discussion about the future of the project and future directions for the team.  The meeting began with a presentation on the current status of the project. The team was working on a new method to solve the problems they were facing. The meeting ended with the presentation of the results of the current project and the discussion of future directions.'
 );


--
-- -- 存放用于展示的summary
-- CREATE TABLE summary (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   doc_id INTEGER NOT NULL,
--   content TEXT NOT NULL,
--   FOREIGN KEY (doc_id) REFERENCES document (id)
-- );


-- chat对话语料 answer待补充
-- CREATE TABLE corpus (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   question TEXT NOT NULL,
--   answer TEXT NOT NULL
-- );


-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'论文试图解决什么问题','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'这是否是一个新的问题','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'这篇文章要验证一个什么科学假设','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'有哪些相关研究？如何归类？谁是这一类课题在领域内值得关注的研究员？','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'论文中提到的解决方案之关键是什么？','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'论文中的实验是如何设计的？','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'用于定量评估的数据集是什么？代码有没有开源？','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'论文中的实验及结果有没有很好地支持需要验证地科学假设？','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'这篇论文到底有什么贡献','padding');
--
-- INSERT INTO corpus (ID,question,answer)
-- VALUES (null,'下一步呢？有什么工作可以继续深入？','padding');


