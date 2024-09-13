/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - councillorsapp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`councillorsapp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `councillorsapp`;

/*Table structure for table `applcncatagory` */

DROP TABLE IF EXISTS `applcncatagory`;

CREATE TABLE `applcncatagory` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(25) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `mid` int(50) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `applcncatagory` */

insert  into `applcncatagory`(`cat_id`,`category`,`dept_id`,`description`,`mid`) values (1,'admin',0,'n',7),(2,'anvi',0,'xx',7),(3,'anvi',52,'xxx',7),(4,'sss',1,'sss',1);

/*Table structure for table `applcnrequest` */

DROP TABLE IF EXISTS `applcnrequest`;

CREATE TABLE `applcnrequest` (
  `request_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `submit_date` date DEFAULT NULL,
  `appdescription` varchar(40) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  `doc_file` varchar(25) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `applcnrequest` */

insert  into `applcnrequest`(`request_id`,`user_id`,`category_id`,`submit_date`,`appdescription`,`status`,`doc_file`,`type`) values (1,1,2,'2019-09-09','wwwwwww','verified','/static/application/1.jpg','housemaking');

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `acc_no` int(11) NOT NULL AUTO_INCREMENT,
  `balance` int(10) DEFAULT NULL,
  `security_pin` int(11) DEFAULT NULL,
  PRIMARY KEY (`acc_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

/*Table structure for table `certficatecategory` */

DROP TABLE IF EXISTS `certficatecategory`;

CREATE TABLE `certficatecategory` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(25) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `certficatecategory` */

insert  into `certficatecategory`(`category_id`,`category`,`description`,`dept_id`,`mid`) values (2,'eeee','eeee',53,1),(3,'anvi','  bbb',53,28);

/*Table structure for table `certificaterequest` */

DROP TABLE IF EXISTS `certificaterequest`;

CREATE TABLE `certificaterequest` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `submit_date` date DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  `doc_file` varchar(25) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `certificaterequest` */

/*Table structure for table `clerk` */

DROP TABLE IF EXISTS `clerk`;

CREATE TABLE `clerk` (
  `clerk_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `qualification` varchar(25) DEFAULT NULL,
  `house_name` varchar(30) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `image` varchar(300) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `joindate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`clerk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `clerk` */

insert  into `clerk`(`clerk_id`,`name`,`dept_id`,`dob`,`phone`,`email`,`gender`,`qualification`,`house_name`,`place`,`district`,`pin`,`image`,`login_id`,`joindate`,`enddate`) values (1,'sni',54,'2019-03-25','7897654321','sni123@gmail.com','female','MCA,','sni','thly','knr',567891,'/static/clerk/20190925-121800.jpg',18,NULL,NULL),(2,'anvi',54,'2019-10-22','1234567890','cc@gmail.com','female','MCA,','uthan','aroli','eeee',333333,'/static/clerk/20191102-155943.jpg',32,NULL,NULL);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(25) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  `from_id` int(11) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `reply_date` date DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaint`,`complaint_date`,`from_id`,`reply`,`reply_date`,`dept_id`) values (1,'not','2019-09-09',9,'nnn','2019-10-31',33),(2,'nnnn','2019-09-09',9,'xxx','2019-11-04',33),(3,'b\n','0000-00-00',9,'pending','0000-00-00',0),(4,'v','0000-00-00',9,'pending','0000-00-00',0),(5,'v','2019-11-05',9,'pending','0000-00-00',0),(6,'n ','2019-11-05',9,'pending','0000-00-00',0),(7,'f','2019-11-05',9,'pending','0000-00-00',0),(8,'e','2019-11-05',9,'pending','0000-00-00',0),(9,'v','2019-11-05',9,'pending','0000-00-00',0),(10,'v','2019-11-05',9,'pending','0000-00-00',0),(11,'m','2019-11-05',9,'pending','0000-00-00',0),(12,'n','2019-11-05',9,'pending','0000-00-00',0),(13,'n','2019-11-05',9,'pending','0000-00-00',0),(14,'n','2019-11-05',9,'pending','0000-00-00',0),(15,'n','2019-11-05',9,'pending','0000-00-00',0),(16,'n','2019-11-05',9,'pending','0000-00-00',0),(17,'b','2019-11-11',9,'pending','0000-00-00',0),(18,'vhjk','2019-11-12',9,'pending','0000-00-00',0);

/*Table structure for table `coordinator` */

DROP TABLE IF EXISTS `coordinator`;

CREATE TABLE `coordinator` (
  `coordinator_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `image` varchar(300) DEFAULT NULL,
  `email` varchar(26) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `councillor_id` int(11) DEFAULT NULL,
  `joindate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`coordinator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `coordinator` */

insert  into `coordinator`(`coordinator_id`,`name`,`gender`,`place`,`post`,`pin`,`image`,`email`,`phone`,`login_id`,`councillor_id`,`joindate`,`enddate`) values (5,'sudhi','female','uthan','aa',123,'/static/coordinator/20191110-233626.jpg','sudhi1234@gmail.com','2345678901',35,33,NULL,NULL),(6,'navya','female','uthan','aa',9,'/static/coordinator/20191110-233512.jpg','navya123@gmail.com','9867452389',36,33,NULL,NULL);

/*Table structure for table `corporationprofile` */

DROP TABLE IF EXISTS `corporationprofile`;

CREATE TABLE `corporationprofile` (
  `profile_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `image` varchar(250) DEFAULT NULL,
  `login_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`profile_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `corporationprofile` */

insert  into `corporationprofile`(`profile_id`,`name`,`email`,`phone`,`place`,`pin`,`image`,`login_id`) values (2,'kannur','knr@gmail.com','6789054321','knr',670561,'/static/coorperation/20191102-160001.jpg',25);

/*Table structure for table `councillor` */

DROP TABLE IF EXISTS `councillor`;

CREATE TABLE `councillor` (
  `councillor_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `house_name` varchar(25) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `pincode` int(6) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `ward` varchar(25) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `image` varchar(260) DEFAULT NULL,
  `joindate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`councillor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `councillor` */

insert  into `councillor`(`councillor_id`,`name`,`gender`,`dob`,`house_name`,`place`,`pincode`,`phone`,`email`,`district`,`ward`,`login_id`,`image`,`joindate`,`enddate`) values (5,'anvi','female','2019-10-23','uthan','aroli',123456,'1234567890','cc@gmail.com','knr','3',33,'/static/councillor/20191102-155915.jpg',NULL,NULL),(6,'anshika','female','2019-10-23','uthan','sss',123456,'9447087079','anshika123@gmail.com','knrs','5',34,'/static/councillor/20191102-155924.jpg',NULL,NULL);

/*Table structure for table `councillorconcillorchat` */

DROP TABLE IF EXISTS `councillorconcillorchat`;

CREATE TABLE `councillorconcillorchat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `messege` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `councillorconcillorchat` */

insert  into `councillorconcillorchat`(`chat_id`,`from_id`,`to_id`,`messege`,`date`) values (1,16,3,'  nnnn','2019-10-23'),(2,16,3,'hiiiiii','2019-10-23'),(3,3,16,'hlooo','2019-10-09'),(4,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(5,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(6,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(7,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(8,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(9,5,2,'http://127.0.0.1:5000/chat_councillors#','2019-10-23'),(10,16,3,'ttt','2019-10-23'),(11,16,3,'mm','2019-10-23'),(12,33,6,'hii','2019-10-23'),(13,34,5,'1','2019-10-23'),(14,34,33,'bb','2019-10-23'),(15,33,34,'xxx','2019-10-23'),(16,33,0,'xx','2019-10-23'),(17,33,0,'xx','2019-10-23'),(18,33,28,'n','2019-10-23'),(19,33,28,'eee','2019-10-23'),(20,33,34,'b','2019-10-23'),(21,34,33,'cc','2019-10-23');

/*Table structure for table `councillorcoodchat` */

DROP TABLE IF EXISTS `councillorcoodchat`;

CREATE TABLE `councillorcoodchat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `messege` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `councillorcoodchat` */

insert  into `councillorcoodchat`(`chat_id`,`from_id`,`to_id`,`messege`,`date`) values (1,36,33,'mm','2019-11-12'),(2,36,33,'mm','2019-11-12'),(3,36,33,'mm','2019-11-12'),(4,36,33,'mm','2019-11-12'),(9,33,36,'gfcb','2019-11-12'),(10,36,33,'kkkk','2019-11-12'),(11,33,36,'fgcg','2019-11-12'),(12,36,33,'bbbb','2019-11-12'),(13,36,33,'mmmm','2019-11-12'),(14,33,36,'dfgh',NULL),(15,36,33,'mmm','2019-11-12'),(16,36,33,'kkkk','2019-11-12'),(17,36,33,'kkkk','2019-11-12'),(18,36,33,'kkkkk','2019-11-12');

/*Table structure for table `councillormayorchat` */

DROP TABLE IF EXISTS `councillormayorchat`;

CREATE TABLE `councillormayorchat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `messege` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `councillormayorchat` */

insert  into `councillormayorchat`(`chat_id`,`from_id`,`to_id`,`messege`,`date`) values (1,28,33,'hii','2019-10-23'),(2,33,28,'nnn','2019-10-23'),(3,34,28,'dd','2019-10-23'),(4,33,28,'nnn','2019-10-30'),(5,28,34,'mm','2019-11-12');

/*Table structure for table `councillorrating` */

DROP TABLE IF EXISTS `councillorrating`;

CREATE TABLE `councillorrating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `councillorrating` */

insert  into `councillorrating`(`rating_id`,`councillor_id`,`user_id`,`rating`,`date`) values (1,33,9,'gooood','2019-09-08'),(2,5,9,'2.0','2019-11-06'),(3,6,9,'3.0','2019-11-06'),(4,5,9,'2.0','2019-11-11'),(5,5,9,'2.0','2019-11-11'),(6,5,9,'0.0','2019-11-11'),(7,33,9,'1.0','2019-11-11'),(8,33,9,'4.5','2019-11-12');

/*Table structure for table `departmentrating` */

DROP TABLE IF EXISTS `departmentrating`;

CREATE TABLE `departmentrating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rating` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `departmentrating` */

insert  into `departmentrating`(`rating_id`,`dept_id`,`user_id`,`rating`,`date`) values (1,1,1,'good','2000-09-09'),(2,53,9,'1.0','2019-11-06'),(3,53,9,'2.0','2019-11-12');

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `dept` */

insert  into `dept`(`dept_id`,`name`) values (1,'cs'),(52,'anu'),(53,'anvi'),(54,'xxx');

/*Table structure for table `depthead` */

DROP TABLE IF EXISTS `depthead`;

CREATE TABLE `depthead` (
  `head_id` int(11) NOT NULL AUTO_INCREMENT,
  `clerk_id` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`head_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `depthead` */

insert  into `depthead`(`head_id`,`clerk_id`,`dept_id`) values (5,18,53),(6,18,54),(8,1,1);

/*Table structure for table `discussion_comment` */

DROP TABLE IF EXISTS `discussion_comment`;

CREATE TABLE `discussion_comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `cdate` datetime NOT NULL,
  `dtype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `discussion_comment` */

insert  into `discussion_comment`(`comment_id`,`topic_id`,`user_id`,`comment`,`cdate`,`dtype`) values (1,1,9,'sss','2019-09-09 00:00:00','user'),(2,1,33,'nnn','2019-10-23 00:00:00','councillor'),(3,1,9,'nn','2019-09-09 00:00:00','user'),(24,1,33,'nn','2019-10-24 00:00:00','councillor'),(25,1,33,'ggg','2019-10-24 00:00:00','councillor'),(26,1,33,'mmm','2019-10-24 14:24:24','councillor'),(27,1,33,'mmmmmmm','2019-10-24 14:25:33','councillor'),(28,1,33,'mmmm','2019-10-24 14:25:44','councillor'),(29,1,33,'hhh','2019-10-24 14:32:33','councillor'),(30,2,9,'hhh','2019-10-24 14:33:55','user'),(32,2,33,'ccccc','2019-10-24 14:38:36','councillor'),(33,2,33,'ccccc','2019-10-24 14:38:48','councillor'),(34,2,33,'ccccc','2019-10-24 14:39:40','councillor'),(35,2,33,'ttt','2019-10-24 14:39:48','councillor'),(36,2,33,'ccccc','2019-10-25 16:10:20','councillor'),(40,9,3,'b','2019-11-10 00:00:00','user'),(41,9,3,'b','2019-11-10 22:47:01','user'),(42,9,3,'b','2019-11-10 22:47:33','user'),(43,9,1,'mmmm','2019-11-10 22:47:59','user'),(44,9,1,'hloooooo','2019-11-10 22:48:13','user'),(45,9,1,'mmm','2019-11-10 22:49:24','user'),(46,3,9,'nnn','2019-11-10 22:51:28','user'),(47,2,9,'bb','2019-11-10 22:51:42','user'),(48,2,9,'oooooooooooo','2019-11-10 22:52:01','user'),(49,2,9,'nnnnbvcfrugh','2019-11-10 22:53:08','user'),(50,2,9,'bbbbbvgc.f. h','2019-11-10 22:53:36','user'),(51,2,9,'suuuuuuu','2019-11-10 22:54:15','user'),(52,3,33,'nnnnnnmmmm','2019-11-10 23:31:22','councillor'),(53,1,9,'vvv','2019-11-11 12:15:15','user'),(54,1,9,'mmmmm','2019-11-12 12:54:43','user');

/*Table structure for table `discussion_forum` */

DROP TABLE IF EXISTS `discussion_forum`;

CREATE TABLE `discussion_forum` (
  `discussion_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `discussion_topic` varchar(25) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`discussion_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `discussion_forum` */

insert  into `discussion_forum`(`discussion_id`,`from_id`,`discussion_topic`,`date`) values (1,33,'flood','2019-09-26'),(2,33,'dddd','2019-09-09'),(3,33,'rain','2019-10-31');

/*Table structure for table `fundalloctocoodinator` */

DROP TABLE IF EXISTS `fundalloctocoodinator`;

CREATE TABLE `fundalloctocoodinator` (
  `fund_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `cood_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `fund` int(10) DEFAULT NULL,
  `fundids` int(11) DEFAULT NULL,
  PRIMARY KEY (`fund_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `fundalloctocoodinator` */

insert  into `fundalloctocoodinator`(`fund_id`,`councillor_id`,`cood_id`,`date`,`fund`,`fundids`) values (1,33,35,'2019-10-31',1,2),(2,33,36,'2019-10-31',1,2),(3,33,36,'2019-10-31',1,2);

/*Table structure for table `fundalloctocouncillor` */

DROP TABLE IF EXISTS `fundalloctocouncillor`;

CREATE TABLE `fundalloctocouncillor` (
  `fund_id` int(11) NOT NULL AUTO_INCREMENT,
  `fund` varchar(10) DEFAULT NULL,
  `councillor_id` int(11) DEFAULT NULL,
  `mayor_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fund_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fundalloctocouncillor` */

insert  into `fundalloctocouncillor`(`fund_id`,`fund`,`councillor_id`,`mayor_id`,`date`) values (1,'22',33,28,'2019-10-20'),(2,'3',33,28,'2019-10-22');

/*Table structure for table `logintable` */

DROP TABLE IF EXISTS `logintable`;

CREATE TABLE `logintable` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) DEFAULT NULL,
  `password` varchar(25) DEFAULT NULL,
  `usertype` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

/*Data for the table `logintable` */

insert  into `logintable`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(9,'anvi','1','user'),(18,'sni123@gmail.com','clerk','dept'),(28,'anju12@gmail.com','1','mayor'),(32,'anvi@gamil.com','clerk','clerks'),(33,'cc@gmail.com','1','councillors'),(34,'anshika123@gmail.com','1','councillors'),(35,'sudhi1234','1','coordinator'),(36,'navya123','1','coordinator'),(37,'abc','1','user'),(39,'bb','ee','user');

/*Table structure for table `mayor` */

DROP TABLE IF EXISTS `mayor`;

CREATE TABLE `mayor` (
  `mayor_id` int(11) NOT NULL AUTO_INCREMENT,
  `mayor_name` varchar(20) DEFAULT NULL,
  `picture` varchar(250) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `house_name` varchar(30) DEFAULT NULL,
  `place` varchar(41) DEFAULT NULL,
  `pincode` int(6) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `joindate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`mayor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `mayor` */

insert  into `mayor`(`mayor_id`,`mayor_name`,`picture`,`email`,`gender`,`dob`,`house_name`,`place`,`pincode`,`login_id`,`phone`,`district`,`joindate`,`enddate`) values (8,'anju','/static/mayor/20191102-155853.jpg','anju12@gmail.com','female','2019-09-26','ttt','ttt',111111,28,'8765342190','hhhh','2019-11-02','2024-10-31'),(10,'shikha','/static/mayor/20191102-155822.jpg','efrer@G.COM','female','2019-11-02','nnnnn','nnnnn',123455,40,'1233456666','hhh','2019-11-02','2024-10-31');

/*Table structure for table `meeting` */

DROP TABLE IF EXISTS `meeting`;

CREATE TABLE `meeting` (
  `meetingid` int(11) NOT NULL AUTO_INCREMENT,
  `mayorid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `venue` varchar(25) DEFAULT NULL,
  `topic` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`meetingid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `meeting` */

insert  into `meeting`(`meetingid`,`mayorid`,`date`,`time`,`venue`,`topic`) values (4,28,'2019-10-24','10:49:00','bbb','sss'),(5,28,'2019-10-24','10:49:00','bbb','sss'),(6,28,'2019-10-24','11:00:00','bbb','aroli');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(25) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `mayor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`subject`,`description`,`date`,`mayor_id`) values (1,'ffff','fffff','2019-09-09',1),(3,'aaa','aa','2019-10-23',28),(4,'anvi','nnn','2019-10-31',28);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `amount` int(15) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `policy` */

DROP TABLE IF EXISTS `policy`;

CREATE TABLE `policy` (
  `policy_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `councillor_id` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `policy` */

insert  into `policy`(`policy_id`,`name`,`councillor_id`,`description`,`date`,`status`) values (1,'meet',33,'cs','2019-10-21','accept'),(2,'flood',33,'ds','2019-09-09','pending');

/*Table structure for table `project` */

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `project` */

insert  into `project`(`project_id`,`name`,`details`,`status`,`date`,`uid`,`amount`,`enddate`) values (2,'flood','seminar\r\n','pending','2019-10-18',28,NULL,NULL),(3,'admin','wwww','pending','2019-10-17',28,NULL,NULL),(4,'dd','sss','pending','2019-10-22',28,NULL,NULL),(5,'anvi','sss','pending','2019-10-24',28,NULL,NULL),(6,'admin','ssss','pending','2019-10-24',28,NULL,NULL),(7,'nnn','vvvv','Complete','2019-11-04',28,2019,'2019-11-04'),(8,'admin','ffff','Complete','2019-11-04',28,2019,'2019-11-04'),(9,'admin','ffff','pending','2019-10-25',28,0,'2019-10-25'),(10,'admin','mmmm','pending','2019-10-25',28,9,'2019-10-26'),(11,'admin','mmmm','Complete','2019-11-04',28,9,'2019-10-25');

/*Table structure for table `publicneedfundalloc` */

DROP TABLE IF EXISTS `publicneedfundalloc`;

CREATE TABLE `publicneedfundalloc` (
  `fund_id` int(11) NOT NULL AUTO_INCREMENT,
  `fund` int(10) DEFAULT NULL,
  `report_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fund_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `publicneedfundalloc` */

insert  into `publicneedfundalloc`(`fund_id`,`fund`,`report_id`,`date`) values (1,111,1,'2019-09-11');

/*Table structure for table `publicneedreport` */

DROP TABLE IF EXISTS `publicneedreport`;

CREATE TABLE `publicneedreport` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `cood_id` int(11) DEFAULT NULL,
  `purpose` varchar(50) DEFAULT NULL,
  `pname` varchar(50) DEFAULT NULL,
  `adr1` varchar(50) DEFAULT NULL,
  `adrs2` varchar(50) DEFAULT NULL,
  `adrs3` varchar(50) DEFAULT NULL,
  `ph` varchar(50) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `publicneedreport` */

insert  into `publicneedreport`(`report_id`,`cood_id`,`purpose`,`pname`,`adr1`,`adrs2`,`adrs3`,`ph`,`issue_date`,`status`) values (1,35,'jjjj','vvv','bb','bbb','bb','11111111','2019-12-09','accept'),(2,35,'hhhh',' nnnn','nnfn','mmm','mm','111','2019-09-09','pending'),(3,35,'hhhh','nnnnn','nnnn','mmm','mmm','9999','2019-09-09','reject');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`service_id`,`name`,`description`,`m_id`) values (3,'food','food',28),(4,'flood','floodddd',28);

/*Table structure for table `suggestion` */

DROP TABLE IF EXISTS `suggestion`;

CREATE TABLE `suggestion` (
  `suggestion_id` int(11) NOT NULL AUTO_INCREMENT,
  `suggestion` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `suggestion` */

insert  into `suggestion`(`suggestion_id`,`suggestion`,`date`,`user_id`) values (1,'aaa','2019-10-21',9),(2,'www','2018-12-12',9),(3,'hloo\n','2019-11-06',9),(4,'hloo\n','2019-11-06',9),(5,'good','2019-11-10',9),(6,'','2019-11-11',9),(7,'r','2019-11-11',9),(8,'kkkk','2019-11-13',9),(9,'mm','2019-11-13',9),(10,'mmm','2019-11-13',9);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `ward` varchar(25) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`login_id`,`place`,`post`,`pin`,`phone`,`email`,`ward`,`image`) values (1,'anvikavinod',9,'aa','aa',111111,'2222222','anvivinod@gmail.com','3','/static/user/user_38.png'),(2,'abc',37,'arolu','asdd',123456,'1234567890','abc','5','/static/user/user_37.png'),(4,'nmm',39,'mmm','mmm',45566,'234567890','bb','5','/static/user/user_39.png'),(5,'u',55,'d','34',5,'123456','s','3','/static/user/user_55.png'),(6,'d',56,'aaa','aroli',23,'1234567890','sfcv@gmail.com','5','/static/user/user_56.png');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_head_id` int(11) DEFAULT NULL,
  `clerk_id` int(11) DEFAULT NULL,
  `work_details` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`work_id`,`dept_head_id`,`clerk_id`,`work_details`,`date`,`status`) values (7,18,32,'sssss','2019-10-22','complete'),(8,18,32,'admin','2019-10-25','complete'),(9,18,32,'admin','2019-10-25','complete'),(10,18,32,'na','2019-10-26','complete'),(11,18,32,'admin','2019-10-26','complete'),(12,18,32,'admin','2019-10-26','workingon'),(13,18,32,'admin','2019-11-12','pending'),(14,18,32,'www','2019-11-12','pending'),(15,18,32,'www','2019-11-12','pending');

/*Table structure for table `work_report` */

DROP TABLE IF EXISTS `work_report`;

CREATE TABLE `work_report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` int(11) DEFAULT NULL,
  `work_status` varchar(25) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `work_report` */

insert  into `work_report`(`report_id`,`work_id`,`work_status`,`description`,`date`,`cid`) values (2,7,'Complete','/static/clerkworrkreport/191026-092752.pdf','2019-10-26 09:52:27',32),(4,NULL,'pending','/static/clerkworrkreport/191023-095049.pdf','2019-10-23 00:00:00',NULL),(5,10,'Complete','/static/clerkworrkreport/191026-092755.pdf','2019-10-26 09:55:27',32),(6,11,'Complete','/static/clerkworrkreport/191030-093549.pdf','2019-10-30 09:49:35',32),(7,12,'working on','/static/clerkworrkreport/191030-094849.pdf','2019-10-30 09:49:48',32),(8,13,'pending','pending','0000-00-00 00:00:00',32),(9,14,'pending','pending','0000-00-00 00:00:00',32),(10,15,'pending','pending','0000-00-00 00:00:00',32);

/*Table structure for table `discussion` */

DROP TABLE IF EXISTS `discussion`;

/*!50001 DROP VIEW IF EXISTS `discussion` */;
/*!50001 DROP TABLE IF EXISTS `discussion` */;

/*!50001 CREATE TABLE `discussion` (
  `comment_id` int(11) NOT NULL DEFAULT '0',
  `comment` varchar(200) NOT NULL DEFAULT '',
  `name` varchar(25) DEFAULT NULL,
  `image` varchar(260) DEFAULT NULL,
  `topic_id` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 */;

/*View structure for view discussion */

/*!50001 DROP TABLE IF EXISTS `discussion` */;
/*!50001 DROP VIEW IF EXISTS `discussion` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `discussion` AS select `discussion_comment`.`comment_id` AS `comment_id`,`discussion_comment`.`comment` AS `comment`,`councillor`.`name` AS `name`,`councillor`.`image` AS `image`,`discussion_comment`.`topic_id` AS `topic_id` from (`councillor` join `discussion_comment` on((`discussion_comment`.`user_id` = `councillor`.`login_id`))) where (`discussion_comment`.`dtype` = 'councillor') union (select `discussion_comment`.`comment_id` AS `comment_id`,`discussion_comment`.`comment` AS `comment`,`user`.`name` AS `name`,`user`.`image` AS `image`,`discussion_comment`.`topic_id` AS `topic_id` from (`user` join `discussion_comment` on((`discussion_comment`.`user_id` = `user`.`login_id`))) where (`discussion_comment`.`dtype` = 'user')) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
