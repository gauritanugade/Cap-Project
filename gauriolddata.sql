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
  `contact_number` bigint NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `biometric` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`capfaculty_id`),
  KEY `fk_exam_id` (`examsession_id`),
  CONSTRAINT `fk_exam_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cap_faculty`
--

LOCK TABLES `cap_faculty` WRITE;
/*!40000 ALTER TABLE `cap_faculty` DISABLE KEYS */;
INSERT INTO `cap_faculty` VALUES (1,'Ajit Powar','Q.Director','2024-01-23','D:\\project_cap\\static\\appoiment_letters\\report (1).pdf',10,56789999,'ajit@gmail.com','yes'),(2,'Ajit Powar','Q.Director','2024-01-23','D:\\project_cap\\static\\appoiment_letters\\report (1).pdf',10,56789999,'ajit@gmail.com','yes'),(3,'Mujavar','Q.Director','2024-01-04','D:\\project_cap\\static\\appoiment_letters\\Assignment No5_shruti.pdf',11,456789543,'mujavar@gmail.com','yes'),(4,'Sagar ','Pea','2024-01-11','D:\\project_cap\\static\\appoiment_letters\\Assignment No2-shruti.pdf',12,1234567808,'sagar@123gmail.com','yes'),(5,'rajshree','Scrutiny Clerk','2024-01-12','D:\\project_cap\\static\\appoiment_letters\\Assignment No5_shruti.pdf',9,876434,'rajshree@gmail.com','yes'),(6,'Ajit Powar','Q.Director','2024-02-14','D:\\central system\\static\\appoiment_letters\\Screenshot (2).png',1,567899,'powar@gmail.com','yes');
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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursefield`
--

LOCK TABLES `coursefield` WRITE;
/*!40000 ALTER TABLE `coursefield` DISABLE KEYS */;
INSERT INTO `coursefield` VALUES (1,3,1,3,5),(2,3,1,3,5),(3,3,2,3,5),(4,3,2,3,5),(5,3,3,3,5),(6,3,3,3,5),(7,3,3,3,5),(8,3,4,3,5),(9,3,4,3,5),(10,3,4,3,5),(11,3,4,3,5),(12,3,4,3,5),(13,3,4,3,5),(14,3,4,3,5),(15,3,5,3,5),(16,3,5,3,5),(17,3,6,3,5),(18,3,6,3,5),(19,3,6,3,5),(20,3,6,3,5),(21,3,6,3,5),(22,3,6,3,5),(23,3,7,3,5),(24,3,7,3,5),(25,3,7,3,5),(26,3,7,3,5),(27,3,7,3,5),(28,3,18,3,5),(29,3,18,3,5),(30,3,18,3,5),(31,3,18,3,5),(32,3,18,3,5),(33,3,18,3,5),(34,3,18,3,5),(35,3,18,3,5);
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
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursename`
--

LOCK TABLES `coursename` WRITE;
/*!40000 ALTER TABLE `coursename` DISABLE KEYS */;
INSERT INTO `coursename` VALUES (1,'DSC-1001E1','Mathematical',1),(2,'DSC-1001E2','Nuclear and partial physics',1),(3,'DSC-1001E3','Quantum Mechanics',1),(4,'DSC-1001E4','Solid State physics',1),(6,'DSC-1002E1','Physical Chemistry',3),(7,'DSC-1002E2','Inorganic Chemistry',3),(8,'DSC-1002E3','Organic Chemistry',3),(9,'DSC-1002E4','Analytical Chemistry',3),(11,'DSC-1003E1','Real analysis',5),(12,'DSC-1003E2','Modern Algebra',5),(13,'DSC-1003E3','Partial Differential equation',5),(14,'DSC-1003E4','Numerical methods-1',5),(17,'DSC-1004E1','Probability Distriubution',8),(18,'DSC-1004E2','Statistical Inference',8),(25,'DSC-1005E1','Fundamentals and instrumention',15),(26,'DSC-1005E2','8051 Microcontroller Interfacing',15),(28,'DSC-1006E1','Computer Network',17),(29,'DSC-1006E2','Software Engineering',17),(35,'DSC-1007E1','Cytology & Research Technique in life Science',23),(36,'DSC-1007E2','Microbiology,plantpathlogy & biofertilizer',23),(41,'DSC-1008E1','Plant Biotechnology',28),(42,'DSC-1008E2','Animal tissue Culture',28);
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examsession`
--

LOCK TABLES `examsession` WRITE;
/*!40000 ALTER TABLE `examsession` DISABLE KEYS */;
INSERT INTO `examsession` VALUES (1,'January-February',2022,2,'UG',2,3,1),(2,'January-February',2022,2,'UG',2,3,2),(3,'January-February',2022,2,'UG',2,3,3),(4,'February-March',2022,3,'UG',3,6,3),(5,'February-March',2022,3,'UG',3,6,4),(6,'February-March',2022,3,'UG',3,6,6),(7,'February-March',2022,3,'UG',3,6,7),(8,'January-February',2024,5,'UG',1,1,1),(9,'January-February',2024,5,'UG',1,1,2),(10,'January-February',2024,5,'UG',1,1,3),(11,'January-February',2024,5,'UG',2,3,1),(12,'January-February',2024,5,'UG',2,3,2),(13,'January-February',2024,5,'UG',2,3,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (1,'B.A',3,'bimester'),(2,'B.Com',3,'bimester'),(3,'B.sc',3,'bimester'),(4,'B.C.S',3,'bimester'),(5,'B.Sc. Biotech-Entire',3,'bimester'),(6,'B.B.A.',3,'bimester'),(7,'B.C.A.',3,'bimester'),(8,'B.Voc.',3,'bimester'),(9,'B.Sc.',3,'bimester'),(11,'xyz',2,'bimester'),(12,'abc',1,'bimester'),(13,'rtyyu',1,'Bimester'),(14,'errr',2,'Bimester'),(15,'sdddf',1,'Bimester'),(16,'opt',1,'Bimester'),(17,'trw',2,'Bimester'),(18,'avde',1,'Bimester'),(19,'mn',1,'Bimester'),(20,'bv',2,'Bimester');
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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_check`
--

LOCK TABLES `issue_check` WRITE;
/*!40000 ALTER TABLE `issue_check` DISABLE KEYS */;
INSERT INTO `issue_check` VALUES (5,'2024-01-27','2024-01-31',1,3,17,2,NULL,NULL),(6,'2024-01-27','2024-02-08',1,3,10,2,NULL,NULL),(7,'2024-01-26','2024-01-31',1,3,10,2,NULL,NULL),(8,'2024-01-24','2024-02-14',1,3,20,2,NULL,NULL),(9,'2024-01-17','2024-01-22',2,3,100,2,NULL,NULL),(10,'2024-01-25','2024-01-24',1,3,10,2,NULL,NULL),(11,'2024-01-09','2024-01-23',3,4,200,3,NULL,NULL),(12,'2024-01-23','2024-01-29',6,8,200,5,NULL,NULL),(13,'2024-01-23','2024-01-08',6,8,10,5,NULL,NULL),(14,'2024-02-01','2024-02-07',1,1,200,7,NULL,NULL),(15,'2024-01-29','2024-01-31',1,3,10,2,NULL,NULL),(16,'2024-01-25','2024-02-02',5,1,100,4,NULL,NULL),(17,'2024-01-30','2024-02-01',6,8,10,5,NULL,NULL),(18,'2024-01-27','2024-01-24',6,8,10,5,NULL,NULL),(19,'2024-02-13','2024-02-28',2,7,56,2,NULL,NULL),(20,'2024-02-21','2024-02-15',1,1,78,1,NULL,NULL),(21,'2024-02-19','2024-02-28',1,1,6,7,NULL,NULL),(22,'2024-02-19','2024-05-02',2,7,50,2,1,50),(23,'2024-02-13','2024-02-16',2,7,100,2,1,100),(24,'2023-10-10','2023-10-10',4,1,2,4,10,30),(25,'2024-02-07','2024-02-01',4,1,1,4,20,30),(26,'2024-02-14','2024-02-28',2,6,1,6,15,25),(27,'2024-02-14','2024-02-28',2,6,3,6,1,30),(28,'2024-02-15','2024-02-21',2,7,4,2,10,50),(29,'2024-02-27','2024-02-09',18,11,65,7,3,67),(30,'2024-02-20',NULL,44,7,3,2,3,5),(31,'2024-02-14',NULL,45,10,46,4,5,50),(32,'2024-02-09','2024-02-10',46,10,50,4,1,50),(33,'2024-02-21',NULL,20,7,6,2,20,25),(34,'2024-02-20',NULL,20,7,16,2,10,25),(35,'2024-02-20',NULL,58,7,11,2,20,30),(36,'2024-02-15',NULL,41,6,16,6,15,30),(37,'2024-02-13',NULL,41,6,16,6,15,30),(38,'2024-02-11',NULL,41,6,16,6,15,30),(39,'2024-02-11',NULL,56,10,5,4,1,5),(40,'2024-02-11',NULL,56,10,5,4,1,5),(41,'2024-02-11',NULL,56,10,5,4,1,5),(42,'2024-02-11',NULL,56,10,5,4,1,5),(43,'2024-02-11',NULL,56,10,5,4,1,5),(45,'2024-02-11',NULL,56,10,5,4,1,5),(46,'2024-02-11',NULL,56,10,10,4,31,40),(47,'2024-02-11',NULL,56,10,10,4,41,50),(48,'2024-02-11',NULL,56,10,10,4,51,60),(49,'2024-02-11',NULL,56,10,3,4,61,63),(50,'2024-02-11',NULL,56,10,3,4,64,66);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moderation`
--

LOCK TABLES `moderation` WRITE;
/*!40000 ALTER TABLE `moderation` DISABLE KEYS */;
INSERT INTO `moderation` VALUES (1,'2024-02-04','2024-02-13','2',3,5,3,NULL,NULL,NULL),(2,'2024-02-05','2024-02-14','6',3,5,3,NULL,NULL,NULL),(3,'2024-02-19','2024-02-15','2',3,5,3,NULL,NULL,NULL),(4,'2024-02-11','2024-02-13','4',7,6,6,NULL,NULL,NULL),(5,'2024-02-20','2024-02-29','6',31,1,5,50,NULL,NULL),(6,'2024-01-03','2024-02-13','3',38,6,5,50,NULL,NULL),(7,'2024-02-13',NULL,'5',39,1,5,NULL,1,67),(8,'2024-02-21','2024-02-08','5',31,1,5,26,5,30),(9,'2024-02-21',NULL,'3',38,1,5,11,15,25);
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
  `remaining_paper` int,
  `capfaculty_id` int DEFAULT NULL,
  `sign` varchar(200) DEFAULT NULL,
  `moderation_remaining` int DEFAULT NULL,
  `scrutany_remaining` int DEFAULT NULL,
  PRIMARY KEY (`papercount_id`),
  KEY `fk_tt_id` (`timetable_id`),
  KEY `fk_es_id` (`examsession_id`),
  KEY `fk_paper_count_capfaculty` (`capfaculty_id`),
  CONSTRAINT `fk_es_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `fk_paper_count_capfaculty` FOREIGN KEY (`capfaculty_id`) REFERENCES `cap_faculty` (`capfaculty_id`),
  CONSTRAINT `fk_tt_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count`
--

LOCK TABLES `paper_count` WRITE;
/*!40000 ALTER TABLE `paper_count` DISABLE KEYS */;
INSERT INTO `paper_count` VALUES (1,'Ext-5677',100,'OK','ok','2022-01-06',1,1,'shruti',22,NULL,NULL,NULL,NULL),(2,'Ext-5666',300,'OK','ok','2022-01-10',4,2,'gauri',140,NULL,NULL,NULL,NULL),(3,'Ext-5660',300,'OK','ok','2022-01-11',3,3,'Prachi Patil',100,NULL,NULL,NULL,NULL),(4,'Ext-5699',500,'OK','ok','2024-01-16',8,4,'Hema naik',500,NULL,NULL,NULL,NULL),(5,'Ext-2023',700,'Pending','Pending','2024-01-16',8,4,'Anuja chaugale',600,NULL,NULL,NULL,NULL),(6,'Ext-8764',500,'OK','ok','2024-01-16',8,5,'Anuja chaugale',270,NULL,NULL,NULL,NULL),(7,'EXT-6543',200,'OK','ok','2024-01-16',8,6,'Anuja chaugale',200,NULL,NULL,NULL,NULL),(17,'Ext-8888',56,'OK','ok','2022-01-11',4,2,'shruti',6,NULL,NULL,NULL,NULL),(18,'Ext-111',350,'OK','Pending','2024-01-30',13,7,'Sayali Patil',85,3,'yes',NULL,NULL),(19,'Ext-111',56,'Pending','Pending','2024-01-30',13,7,'Hema naik',50,2,NULL,NULL,NULL),(20,'Ext-5670',789,'Pending','Pending','2024-01-30',4,2,'Janvi',617,3,NULL,NULL,NULL),(21,'Ext-234',76,'OK','ok','2024-02-13',8,4,'Anuja chaugale',76,2,NULL,NULL,NULL),(22,'Ext-231',300,'OK','ok','2024-02-13',8,6,'Anuja chaugale',300,2,NULL,NULL,NULL),(23,'Ext-5600',550,'OK','ok','2024-02-20',8,4,'Hema malini',550,5,NULL,NULL,500),(24,'Ext-5622',750,'OK','ok','2024-02-20',8,6,'Hema malini',747,5,NULL,NULL,750),(25,'Ext-5677',678,'OK','ok','2024-02-13',8,4,'Sayali Patil',678,4,NULL,NULL,678),(26,'Ext-5621',199,'OK','ok','2024-02-05',8,4,'aanchal',199,4,NULL,NULL,199),(27,'Ext-5622',200,'OK','ok','2024-02-05',8,5,'aanchal',200,4,NULL,NULL,200),(28,'Ext-5622',56,'OK','ok','2024-02-12',8,5,'website',56,4,NULL,56,56),(29,'Ext-5688',57,'OK','ok','2024-02-12',8,6,'website',56,4,NULL,57,57),(30,'Ext-66666',180,'OK','ok','2024-02-05',8,4,'anjali',180,5,NULL,180,180),(31,'Ext-11111',200,'OK','ok','2024-02-05',8,5,'anjali',200,5,NULL,124,200),(37,'Ext-5644',100,'OK','ok','2024-02-06',8,5,'Hema naik',100,2,NULL,100,100),(38,'Ext-233',220,'OK','ok','2024-02-06',8,5,'Prachi Patil',220,4,NULL,159,220),(39,'Ext-5666',350,'OK','ok','2024-02-06',8,5,'Prachi Patil',350,1,NULL,NULL,350),(40,'Ext-5623',100,'OK','ok','2024-02-14',8,5,'Anuja chaugale',100,2,NULL,100,100),(41,'Ext-77777',100,'OK','ok','2024-02-07',8,6,'Sayali Patil',52,1,NULL,100,100),(42,'Ext-3499',100,'OK','ok','2024-02-14',8,8,'Nilam',100,3,NULL,100,50),(43,'Ext-9999',20,'OK','ok','2024-02-20',2,9,'Anuja chaugale',20,2,NULL,20,15),(44,'Ext-0000',11,'OK','ok','2024-02-14',4,2,'kritu',8,5,NULL,11,11),(45,'Ext-56666',139,'OK','ok','2024-02-06',8,4,'Prachi',93,4,NULL,139,139),(46,'Ext-2222',100,'OK','ok','2024-02-20',8,4,'swara',47,3,NULL,100,100),(47,'Ext-5666',900,'OK','ok','2024-02-08',8,4,'shruti',900,1,NULL,900,900),(48,'Ext-0000',300,'OK','ok','2024-02-08',8,4,'shruti',300,1,NULL,300,300),(49,'Ext-5677',56,'OK','ok','2024-02-29',1,1,'Anuja chaugale',56,1,NULL,NULL,NULL),(50,'Ext-77777',100,'OK','ok','2024-02-22',3,3,'Hema naik',100,2,NULL,100,100),(51,'Ext-8888',987,'OK','ok','2024-02-28',8,5,'Hema naik',987,3,NULL,987,987),(52,'Ext-5666	',56,'OK','ok','2024-02-10',3,3,'kiyara',56,4,NULL,56,56),(53,'Ext-5666	',56,'OK','ok','2024-02-10',3,3,'kiyara',56,4,NULL,56,56),(54,'Ext-5666',56,'OK','ok','2024-02-16',3,3,'kritika',56,3,NULL,56,56),(55,'Ext-0101',350,'OK','ok','2024-02-10',2,9,'himanshi',350,5,NULL,350,350),(56,'Ext-4444',150,'OK','ok','2024-02-11',8,4,'supriya',74,4,NULL,150,150),(57,'Ext-6829',50,'OK','ok','2024-02-15',3,3,'Sayali Patil',50,5,NULL,50,50),(58,'Ext-6671',100,'OK','ok','2024-02-29',4,2,'Anuja chaugale',89,4,NULL,100,100);
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
  `status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`paperpending_id`),
  KEY `fk_t_id` (`timetable_id`),
  KEY `fk_esid_id` (`examsession_id`),
  KEY `fk_faculty_paper` (`capfaculty_id`),
  CONSTRAINT `fk_esid_id` FOREIGN KEY (`examsession_id`) REFERENCES `examsession` (`examsession_id`),
  CONSTRAINT `fk_faculty_paper` FOREIGN KEY (`capfaculty_id`) REFERENCES `cap_faculty` (`capfaculty_id`),
  CONSTRAINT `fk_t_id` FOREIGN KEY (`timetable_id`) REFERENCES `time_table` (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count_pending`
--

LOCK TABLES `paper_count_pending` WRITE;
/*!40000 ALTER TABLE `paper_count_pending` DISABLE KEYS */;
INSERT INTO `paper_count_pending` VALUES (1,'Ext-233',120,'Pending','Pending','2024-02-13',8,5,'Anuja chaugale',2,1),(2,'Ext-5611',650,'Pending','Pending','2024-02-20',8,5,'Hema malini',5,0),(3,'Ext-8888',987,'Pending','Pending','2024-02-13',8,5,'Sayali Patil',4,1),(4,'Ext-5666',234,'Pending','Pending','2024-02-13',8,6,'Sayali Patil',4,1),(5,'Ext-5623',201,'Pending','Pending','2024-02-05',8,6,'aanchal',4,1),(6,'Ext-5644',55,'Pending','Pending','2024-02-12',8,4,'website',4,1),(7,'Ext-77777',50,'Pending','Pending','2024-02-05',8,6,'anjali',5,1),(8,'Ext-9999',300,'Pending','Pending','2024-02-05',8,5,'John Doe',3,1),(9,'EXT-3499',50,'Pending','Pending','2024-02-07',12,8,'shruti',3,1),(10,'Ext-9999',60,'Pending','Pending','2024-02-07',2,9,'shruti',3,1),(11,'Ext-0000',100,'Pending','Pending','2024-02-15',4,2,'neha',4,1),(12,'Ext-4444',120,'Pending','Pending','2024-02-06',8,4,'Prachi',4,0),(13,'Ext-2222',200,'Pending','Pending','2024-02-06',8,4,'Prachi',4,1),(14,'Ext-5666',600,'Pending','Pending','2024-02-08',8,4,'shruti',1,1),(15,'Ext-5666',56,'Pending','Pending','2024-02-22',3,3,'Anuja chaugale',5,1),(16,'Ext-9191',30,'Pending','Pending','2024-02-10',2,12,'sima',3,0),(17,'Ext-5555',40,'Pending','Pending','2024-02-11',8,4,'supriya',4,0),(18,'Ext-3333',50,'Pending','Pending','2024-02-11',8,4,'supriya',4,0),(19,'Ext-6671',100,'Pending','Pending','2024-02-17',4,2,'Hema naik',6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pattern`
--

LOCK TABLES `pattern` WRITE;
/*!40000 ALTER TABLE `pattern` DISABLE KEYS */;
INSERT INTO `pattern` VALUES (1,'Old',40,10,1,3),(2,'Old',40,10,1,1),(3,'New',15,35,1,2),(4,'New',15,35,1,3),(5,'NEP',10,40,1,3);
/*!40000 ALTER TABLE `pattern` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrutany`
--

LOCK TABLES `scrutany` WRITE;
/*!40000 ALTER TABLE `scrutany` DISABLE KEYS */;
INSERT INTO `scrutany` VALUES (1,'2024-02-28','2024-02-22',19,5,7,NULL,NULL,NULL),(2,'2024-02-28','2024-02-29',20,5,2,NULL,NULL,NULL),(3,'2024-02-13','2024-02-13',2,5,2,NULL,NULL,NULL),(4,'2024-02-05','2024-02-29',4,5,4,NULL,NULL,NULL),(6,'2024-02-13','2024-02-21',23,5,4,50,NULL,NULL),(7,'2024-02-20','2024-02-28',43,5,9,5,NULL,NULL),(8,'2024-02-06','2024-02-19',42,5,8,50,1,50);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'Physics',3,3),(2,'Chemistry',3,3),(3,'Maths',3,3),(4,'Statistics',3,3),(5,'Electronics',3,3),(6,' Computer Science',3,3),(7,'Botany',3,3),(8,'Zoology ',3,3),(9,'Microbiology',3,3),(10,'Biotechnology',3,3),(11,'Physics',3,3),(12,'Chemistry',3,3),(13,'Maths',3,3),(14,'Statistics',3,3),(15,'Electronics',3,3),(16,' Computer Science',3,3),(17,'Botany',3,3),(18,'Zoology ',3,3),(19,'Microbiology',3,3),(20,'Biotechnology',3,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'Mr.Thorat Sanjay','thorat@123gmail.com',4563217865,2,4,3,1,3),(2,'Mr.Thorat Sanjay','thorat@123gmail.com',4563217865,2,4,3,1,3),(3,'Miss.Summaya Inamdar','summaya@123gmail.com',1234567845,2,4,3,25,1),(4,'Mr.N.P.Mote','motenamdev@gmail.com',9921990399,3,5,3,26,5),(5,'Mr.N.P.Mote','motenamdev@gmail.com',9921990399,3,5,3,26,5),(6,'Dr.C.B.Patil ','patilcb.ele@gmail.com',9922049750,3,5,3,3,1),(7,'Mr.P.R.Bagade ','pravinbagade333@gmail.com',9890063936,2,4,3,25,5),(8,'Miss.Summaya Inamdar','summaya@123gmail.com',1234567845,3,6,3,2,1),(10,'Mr.Thorat Sanjay','thorat@123gmail.com',4563217865,1,1,3,13,3),(11,'Varsha Powar','varsha123@gmail.com',1234876534,2,3,3,17,4);
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time_table`
--

LOCK TABLES `time_table` WRITE;
/*!40000 ALTER TABLE `time_table` DISABLE KEYS */;
INSERT INTO `time_table` VALUES (1,1,1,1,'2022-01-04','11:00:00','13:00:00',2,3,3),(2,4,5,25,'2022-01-06','11:00:00','13:00:00',2,4,3),(3,3,5,26,'2022-01-06','13:00:00','15:00:00',3,6,3),(4,8,3,13,'2024-01-12','11:00:00','13:00:00',1,1,3),(5,8,1,2,'2024-01-12','12:00:00','14:00:00',2,3,3),(6,8,1,3,'2024-01-12','11:00:00','13:00:00',2,3,3),(7,13,4,17,'2024-01-29','11:00:00','01:00:00',2,3,3),(8,12,2,7,'2024-01-31','11:00:00','00:00:00',2,4,3),(9,2,6,28,'2024-01-23','15:55:00','15:51:00',2,4,3),(10,2,6,29,'2024-01-31','16:51:00','17:51:00',2,4,3),(11,2,5,25,'2024-01-28','04:03:00','05:03:00',2,4,3),(12,2,5,26,'2024-01-25','05:03:00','04:03:00',2,4,3),(13,3,5,25,'2020-10-10','10:10:00','10:10:00',3,5,3),(14,3,5,26,'2020-12-10','00:00:00','01:00:00',3,5,3);
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

-- Dump completed on 2024-02-11 19:14:28
