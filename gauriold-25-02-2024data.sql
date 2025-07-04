-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: cap_project
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('admin','vck@123'),('capmember','cap@123');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cap_faculty`
--

DROP TABLE IF EXISTS `cap_faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cap_faculty` (
  `capfaculty_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `appoiment_date` date NOT NULL,
  `appoiment_letter` varchar(100) DEFAULT NULL,
  `examsession_id` int DEFAULT NULL,
  `contact_no` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `biometric` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`capfaculty_id`),
  KEY `fk_exam_id` (`examsession_id`),
  CONSTRAINT `fk_exam_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cap_faculty`
--

LOCK TABLES `cap_faculty` WRITE;
/*!40000 ALTER TABLE `cap_faculty` DISABLE KEYS */;
INSERT INTO `cap_faculty` VALUES (16,'Mujawar','Director','2024-01-08','E:\\project_cap\\static\\appoiment_letters\\report (1).pdf',11,89679834,'mujawar123@gmail.com','done'),(17,'Sagar','Clerk','2024-01-19','E:\\project_cap\\static\\appoiment_letters\\report (2).pdf',15,12564389,'sagar123@gmail.com','done'),(18,'aarya','Q.Director','2024-05-15','E:\\project_cap\\static\\appoiment_letters\\Activity Diagram.pdf',15,98763389,'aarya123@gmail.com','done'),(19,'Ajit Powar','Q.Director','2024-01-30','E:\\project_cap\\static\\appoiment_letters\\report (3).pdf',15,99012367,'ajit123@gmail.com','done'),(20,'gauri','Scrutiny Clerk','2024-02-05','E:\\project_cap\\static\\appoiment_letters\\statistics.docx',12,777777770,'gauri@gamil.com','done'),(21,'Mrunal Dinde','Scrutiny Clerk','2024-02-08','D:\\central system\\static\\appoiment_letters\\report (9).pdf',12,5647353,'dinde123@gmail.com','done'),(22,'Mrunal Dinde','Q.Director','2024-02-08','D:\\central system\\static\\appoiment_letters\\Capreview3.pptx',12,8967983465,'shruti123@gmail.com','done');
/*!40000 ALTER TABLE `cap_faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coursefield`
--

DROP TABLE IF EXISTS `coursefield`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursefield` (
  `coursefield_id` int NOT NULL AUTO_INCREMENT,
  `faculty_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `year` int NOT NULL,
  `sem` int NOT NULL,
  PRIMARY KEY (`coursefield_id`),
  KEY `fk_id` (`faculty_id`),
  KEY `fk_studentid` (`subject_id`),
  CONSTRAINT `fk_id` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `fk_studentid` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursefield`
--

LOCK TABLES `coursefield` WRITE;
/*!40000 ALTER TABLE `coursefield` DISABLE KEYS */;
INSERT INTO `coursefield` VALUES (36,11,22,1,1),(37,11,22,1,1),(38,11,22,2,3),(39,11,22,3,5),(40,11,22,3,6),(41,11,26,1,1),(42,11,26,1,1),(43,11,26,2,4),(44,11,26,3,6),(45,11,26,3,5),(46,11,27,1,1),(47,11,27,2,4),(48,11,27,3,5),(49,11,27,3,6),(50,11,24,2,4),(51,11,24,1,2),(52,11,24,3,6),(53,11,25,2,4),(54,11,25,2,4),(55,11,25,2,4),(56,11,28,3,6),(57,11,25,3,6);
/*!40000 ALTER TABLE `coursefield` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coursename`
--

DROP TABLE IF EXISTS `coursename`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursename` (
  `coursename_id` int NOT NULL AUTO_INCREMENT,
  `course_id` varchar(200) DEFAULT NULL,
  `coursename` varchar(200) DEFAULT NULL,
  `coursefield_id` int NOT NULL,
  PRIMARY KEY (`coursename_id`),
  UNIQUE KEY `course_id` (`course_id`),
  KEY `fk_coursename` (`coursefield_id`),
  CONSTRAINT `fk_coursename` FOREIGN KEY (`coursefield_id`) REFERENCES `coursefield` (`coursefield_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursename`
--

LOCK TABLES `coursename` WRITE;
/*!40000 ALTER TABLE `coursename` DISABLE KEYS */;
INSERT INTO `coursename` VALUES (50,'DSC-1001A','Physics-I ',36),(52,'DSC-1001B','Physics-II ',37),(53,'DSC-1001C','Physics-I ',38),(54,'DSE-1001E1','Physics-I ',39),(55,'DSE-1001F1','Physics -I',40),(56,'DSC-1003A','Mathematics-I',41),(59,'DSC -1003D','Mathematics-I',43),(60,'DSC-1003F1','Mathematics -',44),(61,'DSC-1003E1','Mathematics -I ',45),(62,'DSC-1004A','Statistics-I',46),(63,'DSC-1004D','State-I  Proba Distri-II',47),(64,'DSE-1004E1','Sec-II Staistical Inference',48),(65,'DSE-1004E2','Sec-I Sampling theory',49),(66,'DSC-1005C','Electronic Communication',50),(67,'DSC-1005B','Analog Electronic(sec I)',51),(68,'DSE-1005E1','Linear Integrated circuits(sec I)',52),(71,'DSC-12ccc','aaa',55),(72,'DSC-1001ddd','ddd',56),(73,'DSC-1001eee','eee',56);
/*!40000 ALTER TABLE `coursename` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examsession`
--

DROP TABLE IF EXISTS `examsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examsession` (
  `examsession_id` int NOT NULL AUTO_INCREMENT,
  `month` varchar(250) NOT NULL,
  `exam_year` year NOT NULL,
  `pattern_id` int NOT NULL,
  `degree` varchar(250) NOT NULL,
  `year` int NOT NULL,
  `sem` int NOT NULL,
  `faculty_id` int NOT NULL,
  PRIMARY KEY (`examsession_id`),
  KEY `fk_examid` (`faculty_id`),
  KEY `fk_examsession_id` (`pattern_id`),
  CONSTRAINT `fk_examid` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `fk_examsession_id` FOREIGN KEY (`pattern_id`) REFERENCES `pattern` (`pattern_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examsession`
--

LOCK TABLES `examsession` WRITE;
/*!40000 ALTER TABLE `examsession` DISABLE KEYS */;
INSERT INTO `examsession` VALUES (11,'January-February',2023,23,'UG',1,2,11),(12,'February-March',2024,33,'UG',3,6,11),(13,'March-April',2023,34,'UG',3,6,11),(14,'April-May',2020,26,'UG',2,3,11),(15,'May-June',2024,32,'UG',3,6,11),(16,'August-September',2021,26,'UG',2,4,17),(17,'September-October',2021,32,'UG',2,4,11),(18,'October -November',2023,25,'UG',3,6,11),(19,'October -November',2023,25,'UG',3,6,13),(20,'October -November',2023,25,'UG',3,6,14),(21,'October -November',2023,25,'UG',3,6,16),(22,'January-February',2024,25,'UG',3,6,11),(23,'January-February',2024,25,'UG',3,6,13),(24,'January-February',2024,25,'UG',3,6,14);
/*!40000 ALTER TABLE `examsession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `faculty_id` int NOT NULL AUTO_INCREMENT,
  `faculty` varchar(200) NOT NULL,
  `duration` int NOT NULL,
  `sem_pattern` varchar(256) NOT NULL,
  PRIMARY KEY (`faculty_id`),
  UNIQUE KEY `faculty` (`faculty`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (11,'B.Sc.',3,'bimester'),(12,'M.Sc.',2,'bimester'),(13,'B.C.A.',3,'bimester'),(14,'B.Com.',3,'bimester'),(15,'M.Com.',2,'bimester'),(16,'B.B.A.',3,'bimester'),(17,'B.A.',3,'bimester'),(18,'B.Voc.',3,'bimester'),(19,'M.Voc.',3,'bimester'),(26,'Mca',2,'Bimester');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_check`
--

DROP TABLE IF EXISTS `issue_check`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_check` (
  `issue_check_id` int NOT NULL AUTO_INCREMENT,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `papercount_id` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `teacher_paper_count` int DEFAULT NULL,
  `timetable_id` int DEFAULT NULL,
  `from_count` int DEFAULT NULL,
  `to_count` int DEFAULT NULL,
  PRIMARY KEY (`issue_check_id`),
  KEY `fk_papercount` (`papercount_id`),
  KEY `fk_teacher` (`teacher_id`),
  KEY `fk_timetable` (`timetable_id`),
  CONSTRAINT `fk_papercount` FOREIGN KEY (`papercount_id`) REFERENCES `paper_count` (`papercount_id`),
  CONSTRAINT `fk_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`),
  CONSTRAINT `fk_timetable` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_check`
--

LOCK TABLES `issue_check` WRITE;
/*!40000 ALTER TABLE `issue_check` DISABLE KEYS */;
INSERT INTO `issue_check` VALUES (5,'2024-01-29','2024-01-31',26,17,50,24,NULL,NULL),(7,'2024-01-26','2024-01-28',22,14,20,9,NULL,NULL),(8,'2024-01-25','2024-01-25',22,11,20,9,NULL,NULL),(9,'2024-01-24','2024-01-31',22,14,5,9,NULL,NULL),(10,'2024-02-26','2024-02-14',23,11,50,9,NULL,NULL),(18,'2024-02-21','2024-02-17',26,17,3,24,12,14),(19,'2024-02-21',NULL,26,17,3,24,12,14),(20,'2024-02-14','2024-02-10',31,11,131,9,120,250),(21,'2024-01-31','2024-02-11',22,11,8,9,13,20),(22,'2024-01-29','2024-02-11',40,15,17,24,34,50),(23,'2024-02-09',NULL,42,16,20,8,1,20),(24,'2024-02-09','2024-02-11',44,16,19,8,11,29),(25,'2024-02-09',NULL,22,11,7,9,1,7),(26,'2024-02-08','2024-02-11',30,14,50,9,1,50),(27,'2024-02-11',NULL,44,19,5,8,1,5),(28,'2024-02-11','2024-02-11',43,19,3,8,2,4),(29,'2024-02-11','2024-02-11',48,11,2,9,1,2),(30,'2024-02-11','2024-02-11',48,11,98,9,3,100),(31,'2024-02-11',NULL,44,16,5,8,1,5);
/*!40000 ALTER TABLE `issue_check` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moderation`
--

DROP TABLE IF EXISTS `moderation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moderation` (
  `moderation_id` int NOT NULL AUTO_INCREMENT,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `cases` varchar(300) NOT NULL,
  `papercount_id` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `timetable_id` int DEFAULT NULL,
  `moderation_paper_count` int DEFAULT NULL,
  `from_count` int DEFAULT NULL,
  `to_count` int DEFAULT NULL,
  PRIMARY KEY (`moderation_id`),
  KEY `fk_id_papercount` (`papercount_id`),
  KEY `fk_id_teacher` (`teacher_id`),
  KEY `fk_time_table_id` (`timetable_id`),
  CONSTRAINT `fk_id_papercount` FOREIGN KEY (`papercount_id`) REFERENCES `paper_count` (`papercount_id`),
  CONSTRAINT `fk_id_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`),
  CONSTRAINT `fk_time_table_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moderation`
--

LOCK TABLES `moderation` WRITE;
/*!40000 ALTER TABLE `moderation` DISABLE KEYS */;
INSERT INTO `moderation` VALUES (14,'2024-02-16','2024-02-11','2',41,16,25,10,1,10),(15,'2024-02-09','2024-02-17','1',39,16,16,5,1,5),(16,'2024-02-11',NULL,'1',41,11,25,40,11,50),(17,'2024-02-13',NULL,'2',41,15,25,51,50,100);
/*!40000 ALTER TABLE `moderation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_count`
--

DROP TABLE IF EXISTS `paper_count`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paper_count` (
  `papercount_id` int NOT NULL AUTO_INCREMENT,
  `quespaper_code` varchar(200) DEFAULT NULL,
  `count` int DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `reason` varchar(250) DEFAULT NULL,
  `received_date` date DEFAULT NULL,
  `examsession_id` int DEFAULT NULL,
  `timetable_id` int DEFAULT NULL,
  `submited_name` varchar(200) DEFAULT NULL,
  `remaining_paper` int DEFAULT NULL,
  `sign` varchar(200) DEFAULT NULL,
  `capfaculty_id` int DEFAULT NULL,
  `moderation_remaining` int DEFAULT NULL,
  `scrutany_remaining` int DEFAULT NULL,
  PRIMARY KEY (`papercount_id`),
  KEY `fk_tt_id` (`timetable_id`),
  KEY `fk_es_id` (`examsession_id`),
  KEY `fk_paper_count_capfaculty` (`capfaculty_id`),
  CONSTRAINT `fk_es_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `fk_paper_count_capfaculty` FOREIGN KEY (`capfaculty_id`) REFERENCES `cap_faculty` (`capfaculty_id`),
  CONSTRAINT `fk_tt_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count`
--

LOCK TABLES `paper_count` WRITE;
/*!40000 ALTER TABLE `paper_count` DISABLE KEYS */;
INSERT INTO `paper_count` VALUES (22,'DSE-1012',100,'Pending','pending','2024-01-24',13,9,'varsha',0,NULL,16,NULL,NULL),(23,'CD78-9990',300,'OK','ok','2023-07-21',13,9,'shyam',250,NULL,18,NULL,NULL),(24,'CD12-7898',680,'Pending','pending','2024-01-30',15,10,'Mujawar',680,NULL,19,NULL,NULL),(25,'CD13-7890',700,'OK','ok','2024-01-30',15,11,'Mujawar',0,NULL,19,NULL,NULL),(26,'CD14-7892',400,'Pending','pending','2024-02-29',12,24,'shyam',397,NULL,17,NULL,NULL),(27,'CD77-7880',500,'Pending','pending','2024-02-29',12,25,'shyam',0,NULL,17,NULL,NULL),(28,'CD12-7892',1290,'OK','ok','2024-02-05',15,10,'shubham',1290,NULL,19,NULL,NULL),(29,'CD12-7888',1250,'OK','ok','2024-02-05',15,10,'shruti patil',1250,NULL,19,NULL,NULL),(30,'DSE-1011',1240,'OK','ok','2024-02-12',13,9,'sharvary',1190,NULL,19,NULL,1100),(31,'CD12-7895',1250,'OK','ok','2024-02-07',13,9,'Mujawar',1119,NULL,18,NULL,1245),(32,'QEr-9099',1200,'OK','ok','2024-02-08',13,9,'richarani',1200,NULL,20,NULL,1200),(33,'DSE-1013',230,'OK','ok','2024-02-08',13,15,'richarani',0,NULL,20,230,0),(34,'DSE-1012',600,'OK','ok','2024-02-29',13,9,'shubham',0,NULL,18,525,580),(35,'DSE-1013',700,'OK','ok','2024-02-29',13,15,'shubham',0,NULL,18,700,676),(36,'CD12-7890',1300,'OK','ok','2024-02-07',12,24,'shubham',0,NULL,16,1300,1155),(37,'ASD-9013',4300,'OK','ok','2024-02-07',12,25,'shubham',4300,NULL,16,4300,4300),(38,'DSE-1012',1001,'OK','ok','2024-02-07',13,15,'shubham',1001,NULL,18,1001,1001),(39,'DSE-1012',1500,'OK','ok','2024-02-08',12,16,'rajashree patil',0,NULL,19,0,0),(40,'DSE-1019',1350,'OK','ok','2024-02-09',12,24,'sagar',1333,NULL,19,1350,1350),(41,'DSE-1016',1450,'OK','ok','2024-02-09',12,25,'sagar',0,NULL,19,1349,1345),(42,'CD12-7890',1201,'OK','ok','2024-02-09',12,8,'varsha',1181,NULL,17,NULL,NULL),(43,'CD12-7898',1301,'OK','ok','2024-02-09',12,8,'varsha',1298,NULL,17,NULL,NULL),(44,'CD12-78922',1029,'OK','ok','2024-02-08',12,8,'dinde',1000,NULL,16,NULL,NULL),(45,'CD12-8888',1230,'OK','ok','2024-02-09',12,28,'Mujawar',1230,NULL,19,1230,1210),(46,'CD12-7890',1200,'Ok','ok','2024-02-07',15,10,'shyam',1200,NULL,18,1200,1200),(47,'CD12-7890',1150,'Ok','ok','2024-02-08',15,11,'varsha',1150,NULL,18,1150,1150),(48,'ASD-9013',1002,'Ok','ok','2024-02-07',13,9,'richarani',902,NULL,18,1002,1002),(49,'CD12-7898',111,'Ok','ok','2024-02-05',15,10,'shubham',111,NULL,18,111,111),(50,'QEr-9099',120,'Ok','ok','2024-02-08',15,10,'Mujawar',120,NULL,17,120,120),(51,'Ext-111',350,'OK','ok','2024-02-07',15,10,'shruti',350,NULL,16,350,350),(52,'Ext-5677',100,'OK','ok','2024-02-07',15,10,'shruti',100,NULL,16,100,100);
/*!40000 ALTER TABLE `paper_count` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper_count_pending`
--

DROP TABLE IF EXISTS `paper_count_pending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paper_count_pending` (
  `paperpending_id` int NOT NULL AUTO_INCREMENT,
  `quespaper_code` varchar(200) DEFAULT NULL,
  `count` int DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `reason` varchar(250) DEFAULT NULL,
  `received_date` date DEFAULT NULL,
  `examsession_id` int DEFAULT NULL,
  `timetable_id` int DEFAULT NULL,
  `submited_name` varchar(200) DEFAULT NULL,
  `capfaculty_id` int NOT NULL,
  `status` int DEFAULT '0',
  PRIMARY KEY (`paperpending_id`),
  KEY `fk_t_id` (`timetable_id`),
  KEY `fk_esid_id` (`examsession_id`),
  KEY `fk_faculty_paper` (`capfaculty_id`),
  CONSTRAINT `fk_esid_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `fk_faculty_paper` FOREIGN KEY (`capfaculty_id`) REFERENCES `cap_faculty` (`capfaculty_id`),
  CONSTRAINT `fk_t_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count_pending`
--

LOCK TABLES `paper_count_pending` WRITE;
/*!40000 ALTER TABLE `paper_count_pending` DISABLE KEYS */;
INSERT INTO `paper_count_pending` VALUES (1,'CD12-7891',1230,'Pending','pending','2024-02-05',15,11,'shubham',19,1),(3,'CD12-7899',1150,'Pending','pending','2024-02-05',15,11,'shruti patil',19,0),(4,'DSE-1014',1140,'Pending','pending','2024-02-12',13,15,'sharvary',19,0),(5,'CD12-7898',1350,'Pending','pending','2024-02-07',13,15,'Mujawar',18,1),(6,'ASD-9013',1002,'Pending','pending','2024-02-07',13,9,'shubham',18,1),(7,'QEr-9099',120,'Pending','pending','2024-02-05',15,10,'rani ',19,1),(8,'CD12-7898',111,'Pending','pending','2024-02-05',15,10,'rani ',19,1);
/*!40000 ALTER TABLE `paper_count_pending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pattern`
--

DROP TABLE IF EXISTS `pattern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pattern` (
  `pattern_id` int NOT NULL AUTO_INCREMENT,
  `pattern` varchar(100) NOT NULL,
  `theory_mark` int NOT NULL,
  `internal_mark` int NOT NULL,
  `year` int NOT NULL,
  `faculty_id` int NOT NULL,
  PRIMARY KEY (`pattern_id`),
  KEY `fk_pattern_id_fk` (`faculty_id`),
  CONSTRAINT `fk_pattern_id_fk` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pattern`
--

LOCK TABLES `pattern` WRITE;
/*!40000 ALTER TABLE `pattern` DISABLE KEYS */;
INSERT INTO `pattern` VALUES (23,'Old',10,40,1,11),(24,'Old',10,40,2,11),(25,'Old',10,40,3,11),(26,'NEP',10,40,1,11),(27,'NEP',10,40,2,11),(29,'NEP',10,40,3,11),(32,'New',15,35,2,11),(33,'New',15,35,3,11),(34,'New',15,35,1,11),(35,'Old',10,40,1,17),(36,'Old',10,40,2,17),(37,'Old',10,40,3,17),(38,'NEP',10,40,1,17),(39,'NEP',10,40,1,17),(40,'NEP',10,40,3,17),(41,'New',15,35,1,17),(42,'New',15,35,2,17),(43,'New',15,35,3,17),(44,'Old',10,40,1,13),(45,'Old',10,40,2,13),(46,'Old',10,40,3,13),(50,'NEP',10,40,1,13),(51,'NEP',10,40,2,13),(52,'NEP',10,40,3,13),(53,'New',15,35,1,13),(54,'New',15,35,2,13),(55,'New',15,35,3,13),(56,'Old',16,41,3,11),(57,'Old',15,40,3,11);
/*!40000 ALTER TABLE `pattern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remu_perpaper`
--

DROP TABLE IF EXISTS `remu_perpaper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remu_perpaper` (
  `remuperpaper_id` int NOT NULL AUTO_INCREMENT,
  `examsession_id` int DEFAULT NULL,
  `remuneration_id` int DEFAULT NULL,
  `degree` varchar(200) NOT NULL,
  `perpaper_rs` float NOT NULL,
  PRIMARY KEY (`remuperpaper_id`),
  KEY `f_eid` (`examsession_id`),
  KEY `f_reid` (`remuneration_id`),
  CONSTRAINT `f_eid` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `f_reid` FOREIGN KEY (`remuneration_id`) REFERENCES `remuneration` (`remuneration_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remu_perpaper`
--

LOCK TABLES `remu_perpaper` WRITE;
/*!40000 ALTER TABLE `remu_perpaper` DISABLE KEYS */;
INSERT INTO `remu_perpaper` VALUES (1,14,NULL,'UG',7),(2,13,3,'UG',10),(3,13,4,'UG',6),(4,17,5,'PG',10),(5,17,6,'PG',10),(6,17,7,'PG',10),(7,14,8,'UG',22),(8,14,9,'UG',11),(9,14,10,'UG',11),(10,14,11,'UG',11),(11,16,12,'PG',12),(12,16,13,'PG',12),(13,12,14,'UG',10),(14,11,15,'UG',20),(15,11,16,'UG',20),(16,11,17,'UG',20),(17,14,18,'PG',23),(18,14,19,'PG',23),(19,14,20,'UG',7),(20,14,21,'UG',7),(21,12,22,'UG',8),(22,12,23,'UG',8),(23,12,24,'UG',6),(24,12,25,'UG',6);
/*!40000 ALTER TABLE `remu_perpaper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remuneration`
--

DROP TABLE IF EXISTS `remuneration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remuneration` (
  `remuneration_id` int NOT NULL AUTO_INCREMENT,
  `examsession_id` int DEFAULT NULL,
  `degree` varchar(200) NOT NULL,
  `slab` varchar(200) NOT NULL,
  `lowerlimit` int NOT NULL,
  `upperlimit` int NOT NULL,
  `rupees` float NOT NULL,
  PRIMARY KEY (`remuneration_id`),
  KEY `fk_eid` (`examsession_id`),
  CONSTRAINT `fk_eid` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remuneration`
--

LOCK TABLES `remuneration` WRITE;
/*!40000 ALTER TABLE `remuneration` DISABLE KEYS */;
INSERT INTO `remuneration` VALUES (1,12,'UG','slab1',1,5,50),(2,14,'UG','slab2',6,10,100),(3,13,'UG','slab1',21,30,200),(4,13,'UG','slab1',1,5,51),(5,17,'PG','s',1,2,2),(6,17,'PG','s',1,2,2),(7,17,'PG','s',1,2,2),(8,14,'UG','slab21',7,11,51),(9,14,'UG','slab101',100,150,1001),(10,14,'UG','slab102',151,200,2001),(11,14,'UG','slab103',201,250,3001),(12,16,'PG','slab11',11,21,150),(13,16,'PG','slab12',22,30,200),(14,12,'UG','slab10',10,20,200),(15,11,'UG','slab1',1,5,70),(16,11,'UG','slab2',6,10,20),(17,11,'UG','slab5',2,10,40),(18,14,'PG','slab1',10,20,21),(19,14,'PG','slab2',21,30,31),(20,14,'UG','slab1',1,10,100),(21,14,'UG','slab2',2,15,150),(22,12,'UG','slab1',1,5,100),(23,12,'UG','slab2',6,10,200),(24,12,'UG','slab1',1,5,50),(25,12,'UG','slab2',6,10,100);
/*!40000 ALTER TABLE `remuneration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scrutany`
--

DROP TABLE IF EXISTS `scrutany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scrutany` (
  `scrutany_id` int NOT NULL AUTO_INCREMENT,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `papercount_id` int DEFAULT NULL,
  `capfaculty_id` int DEFAULT NULL,
  `timetable_id` int DEFAULT NULL,
  `scrutany_paper_count` int DEFAULT NULL,
  `from_count` int DEFAULT NULL,
  `to_count` int DEFAULT NULL,
  PRIMARY KEY (`scrutany_id`),
  KEY `fkid_papercount` (`papercount_id`),
  KEY `fk_id_capfaculty` (`capfaculty_id`),
  KEY `fktime_table_id` (`timetable_id`),
  CONSTRAINT `fk_id_capfaculty` FOREIGN KEY (`capfaculty_id`) REFERENCES `cap_faculty` (`capfaculty_id`),
  CONSTRAINT `fkid_papercount` FOREIGN KEY (`papercount_id`) REFERENCES `paper_count` (`papercount_id`),
  CONSTRAINT `fktime_table_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrutany`
--

LOCK TABLES `scrutany` WRITE;
/*!40000 ALTER TABLE `scrutany` DISABLE KEYS */;
INSERT INTO `scrutany` VALUES (1,'2024-02-15','2024-02-28',NULL,NULL,NULL,NULL,NULL,NULL),(2,'2024-02-22','2024-02-29',NULL,NULL,NULL,NULL,NULL,NULL),(3,'2024-02-14','2024-02-25',NULL,NULL,NULL,NULL,NULL,NULL),(4,'2024-02-14','2024-02-23',23,20,9,NULL,NULL,NULL),(5,'2024-02-06','2024-02-07',30,20,9,40,NULL,NULL),(6,'2024-02-22','2024-02-29',30,20,9,100,NULL,NULL),(7,'2024-02-08','2024-02-09',36,20,24,100,1,100),(8,'2023-06-04','2024-02-11',41,20,25,10,1,10),(9,'2024-02-08','2024-02-11',41,21,25,20,1,20),(10,'2024-04-01','2024-03-01',41,21,25,40,1,40),(11,'2024-02-09','2024-02-10',45,21,28,20,1,20),(12,'2024-02-08','2024-02-11',31,21,9,5,1,5),(13,'2024-02-11','2024-02-11',33,21,15,30,1,30),(14,'2024-02-09','2024-02-11',39,21,16,6,1,6),(15,'2024-02-09','2024-02-11',33,21,15,200,1,200),(16,'2024-02-11','2024-02-11',41,20,25,3,1,3),(17,'2023-10-14','2024-02-11',34,21,9,5,1,5),(18,'2023-01-11','2024-02-11',35,21,15,10,1,10),(19,'2023-08-09','2024-02-11',36,20,24,20,1,20),(20,'2023-12-24','2024-02-11',41,20,25,7,1,7),(21,'2023-08-09','2024-02-11',34,21,9,5,1,5),(22,'2023-11-11','2024-02-11',36,21,24,10,1,10),(23,'2023-01-12','2024-02-11',41,21,25,8,1,8),(24,'2023-04-18','2024-02-11',36,21,24,6,1,6),(25,'2023-10-11','2024-02-11',35,20,15,8,1,8),(26,'2023-07-29','2024-02-11',34,21,9,10,1,10),(27,'2023-12-30','2024-02-11',36,21,24,4,1,4),(28,'2023-07-29',NULL,36,20,24,5,1,5),(29,'2023-03-29',NULL,41,20,25,5,1,5),(30,'2023-01-01',NULL,41,20,25,7,1,7),(31,'2023-12-01','2024-02-11',35,20,15,6,1,6),(32,'2024-02-11','2024-02-11',41,20,25,5,1,5);
/*!40000 ALTER TABLE `scrutany` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(256) DEFAULT NULL,
  `faculty_id` int NOT NULL,
  `pattern_id` int NOT NULL,
  PRIMARY KEY (`subject_id`),
  KEY `fk_subject_id` (`faculty_id`),
  KEY `fk_patternid` (`pattern_id`),
  CONSTRAINT `fk_patternid` FOREIGN KEY (`pattern_id`) REFERENCES `pattern` (`pattern_id`),
  CONSTRAINT `fk_subject_id` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (22,'Physics',11,23),(23,'Chemistry',11,23),(24,'Electronics',11,23),(25,'Computer Science',11,23),(26,'Mathematics',11,23),(27,'Statistics',11,23),(28,'Botany',11,23),(29,'Zoology',11,23),(30,'Microbiology',11,23),(31,'Biotechnology Optional',11,23),(32,'Biotechnology Entire',11,23),(33,'Entire Computer Science',11,23),(34,'software engineering',11,56),(35,'java',11,56),(36,'computer',11,57),(37,'maths',11,57);
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `teacher_name` varchar(200) NOT NULL,
  `teacher_email` varchar(200) NOT NULL,
  `teacher_phoneno` bigint NOT NULL,
  `year` int NOT NULL,
  `sem` int NOT NULL,
  `faculty_id` int NOT NULL,
  `coursename_id` int NOT NULL,
  `subject_id` int NOT NULL,
  PRIMARY KEY (`teacher_id`),
  KEY `fk_fieldid` (`faculty_id`),
  KEY `fk_student_id` (`subject_id`),
  CONSTRAINT `fk_fieldid` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `fk_student_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (11,'Patil Poonam ','poonampatilp47@gmail.com',7757899082,3,6,11,64,27),(13,'Bhosale Ashok B','ashokbhosale98@gmail.com',9689850513,2,4,11,63,27),(14,'Powar V. V','varshavcr23@gmail.com',9823717300,1,1,11,64,27),(15,'G. B.Kolhe','gauravkolhe510@gmail.com',9404184405,1,1,11,61,26),(16,'S.P.Thorat ','thoratsanjay15@gmail.com',9970929595,2,3,11,59,26),(17,'S. M. Malvi','shital31malavi@gmail.com',9324368036,3,6,11,61,26),(18,'Mrunal dinde','mrunal123@gmail.com',7757899082,3,6,11,72,25),(19,'waghamare','waghamare123@gmail.com',1234456,3,6,11,59,25);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `time_table`
--

DROP TABLE IF EXISTS `time_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `time_table` (
  `timetable_id` int NOT NULL AUTO_INCREMENT,
  `examsession_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `coursename_id` int NOT NULL,
  `date` date NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `year` int NOT NULL,
  `sem` int NOT NULL,
  `faculty_id` int NOT NULL,
  PRIMARY KEY (`timetable_id`),
  KEY `fk_timecourse` (`coursename_id`),
  KEY `fk_timepattern` (`examsession_id`),
  KEY `fk_timesubject` (`subject_id`),
  KEY `fk_faculty_timetable` (`faculty_id`),
  CONSTRAINT `fk_faculty_timetable` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `fk_timecourse` FOREIGN KEY (`coursename_id`) REFERENCES `coursename` (`coursename_id`),
  CONSTRAINT `fk_timepattern` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `fk_timesubject` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time_table`
--

LOCK TABLES `time_table` WRITE;
/*!40000 ALTER TABLE `time_table` DISABLE KEYS */;
INSERT INTO `time_table` VALUES (7,11,22,50,'2022-02-03','11:00:00','12:00:00',2,4,11),(8,12,26,59,'2024-02-15','12:00:00','14:00:00',3,6,11),(9,13,27,64,'2023-03-29','23:00:00','13:00:00',2,4,11),(10,15,22,54,'2024-01-30','14:30:00','15:30:00',2,4,11),(11,15,22,55,'2024-01-30','15:00:00','16:30:00',2,4,11),(12,13,27,62,'2023-04-25','12:00:00','14:00:00',2,4,11),(13,13,27,63,'2023-04-13','13:00:00','16:00:00',2,4,11),(14,13,27,64,'2023-03-25','10:00:00','12:00:00',2,4,11),(15,13,27,65,'2023-03-29','11:00:00','14:00:00',2,4,11),(16,12,22,50,'2024-01-01','10:00:00','12:00:00',3,6,11),(17,12,22,52,'2024-01-02','10:00:00','12:00:00',3,6,11),(18,12,22,53,'2024-01-03','10:00:00','12:00:00',3,6,11),(19,12,22,54,'2024-01-04','10:00:00','12:00:00',3,6,11),(20,12,22,55,'2024-01-05','10:00:00','12:00:00',3,6,11),(21,12,26,56,'2024-02-24','10:00:00','12:00:00',2,4,11),(22,12,26,59,'2024-02-25','10:00:00','12:00:00',2,4,11),(23,12,26,60,'2024-02-26','10:00:00','12:00:00',2,4,11),(24,12,26,61,'2024-02-27','10:00:00','12:00:00',2,4,11),(25,12,24,66,'2024-02-27','10:00:00','12:00:00',3,6,11),(26,12,24,67,'2024-02-28','10:00:00','12:00:00',3,6,11),(27,12,24,68,'2024-02-29','10:00:00','12:00:00',3,6,11),(28,12,25,71,'2024-02-08','02:02:00','04:01:00',2,4,11),(29,11,22,55,'2024-02-08','00:54:00','01:54:00',3,6,11);
/*!40000 ALTER TABLE `time_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-25 14:40:39
