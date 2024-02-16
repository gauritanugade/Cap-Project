-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: cap_project
-- ------------------------------------------------------
-- Server version	8.0.28

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cap_faculty`
--

LOCK TABLES `cap_faculty` WRITE;
/*!40000 ALTER TABLE `cap_faculty` DISABLE KEYS */;
INSERT INTO `cap_faculty` VALUES (1,'Dr.Mujawar Irfan Kamaruddin','Scrutiny Clerk','2024-02-01','d:\\Cap-Project-master\\Cap-Project-master\\static/appoiment_letters\\report_8.pdf',3,8530804020,'mujawarirfan@gmail.com','nvhf');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursefield`
--

LOCK TABLES `coursefield` WRITE;
/*!40000 ALTER TABLE `coursefield` DISABLE KEYS */;
INSERT INTO `coursefield` VALUES (1,3,6,3,5),(2,3,6,3,6),(3,3,6,3,6),(4,3,6,1,1),(5,3,6,1,2),(6,3,6,2,3),(7,3,6,2,4),(8,3,3,3,5);
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
  `coursename` varchar(200) DEFAULT NULL,
  `coursefield_id` int NOT NULL,
  `course_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`coursename_id`),
  KEY `fk_coursename` (`coursefield_id`),
  CONSTRAINT `fk_coursename` FOREIGN KEY (`coursefield_id`) REFERENCES `coursefield` (`coursefield_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursename`
--

LOCK TABLES `coursename` WRITE;
/*!40000 ALTER TABLE `coursename` DISABLE KEYS */;
INSERT INTO `coursename` VALUES (1,'Computer Network',1,'DSE-1006E1'),(2,' Software Engineering',1,'DSE-1006E1'),(3,'Internet Technologies-I',1,'DSE-1006E2'),(4,'Introduction to Java',1,'DSE-1006E2'),(5,'Advanced Computer Network',2,'DSE-1006F1'),(6,' Internet Technologies-II',2,'DSE-1006F1'),(8,'Data Science using Python',2,'DSE-1006F2'),(9,'Object Oriented Software Engineering',3,'DSE-1006F1'),(10,'Section-I Problem Solving using computers',4,'DSC-1006A'),(11,'Section-II Database Management System',4,'DSC-1006A'),(12,'Section-I Problem solving using computers',5,'DSC-1006B'),(13,'Section-II Database Management System',5,'DSC-1006B'),(14,'Section-I Operating System',6,'DSC-1006C'),(15,'Section-II Object Oriented Programming',6,'DSC-1006C'),(16,'Section-I Operating System',7,'DSC-1006D'),(17,'Section-II Data Structures	',7,'DSC-1006D'),(18,'mathematics-I',8,'DSE-1006R1');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examsession`
--

LOCK TABLES `examsession` WRITE;
/*!40000 ALTER TABLE `examsession` DISABLE KEYS */;
INSERT INTO `examsession` VALUES (1,'November-December',2023,3,'UG',1,1,3),(2,'November-December',2023,1,'UG',2,3,3),(3,'November-December',2023,1,'UG',3,5,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (1,'B.A.',3,'Bimester'),(2,'B.Com',3,'Bimester'),(3,'B.Sc.',3,'Bimester'),(4,'B.Sc. Computer Science Emtire(BCS)',3,'Bimester'),(5,'B.Sc. Biotech-Entire',3,'Bimester'),(6,'B.B.A.',3,'Bimester'),(7,'B.C.A.',3,'Bimester'),(8,'B.Voc. and Community College',3,'Bimester');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_check`
--

LOCK TABLES `issue_check` WRITE;
/*!40000 ALTER TABLE `issue_check` DISABLE KEYS */;
INSERT INTO `issue_check` VALUES (1,'2024-02-12','2024-02-12',2,1,43,6,1,43),(2,'2024-02-12','2024-02-12',1,3,43,5,1,43);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moderation`
--

LOCK TABLES `moderation` WRITE;
/*!40000 ALTER TABLE `moderation` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count`
--

LOCK TABLES `paper_count` WRITE;
/*!40000 ALTER TABLE `paper_count` DISABLE KEYS */;
INSERT INTO `paper_count` VALUES (1,'ND-61',43,'OK','ok','2023-11-29',3,5,'Mr.P.R.Bagade',0,NULL,1,43,0),(2,'ND-71',43,'OK','ok','2023-11-30',3,6,' Dr.Patil Rajashri Yashwant',0,NULL,1,43,43),(3,'ND-81',43,'OK','ok','2023-11-30',3,7,'Mr.P.R.Bagade',43,NULL,1,43,43),(4,'ND-91',43,'OK','ok','2023-12-01',3,8,'Shruti',43,NULL,1,43,43),(13,'EX-1001',300,'OK','ok','2024-02-16',3,9,'Preeti',300,NULL,1,300,300);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper_count_pending`
--

LOCK TABLES `paper_count_pending` WRITE;
/*!40000 ALTER TABLE `paper_count_pending` DISABLE KEYS */;
INSERT INTO `paper_count_pending` VALUES (6,'EX-1001',300,'Pending','pending','2024-02-14',3,9,'Adhira',1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pattern`
--

LOCK TABLES `pattern` WRITE;
/*!40000 ALTER TABLE `pattern` DISABLE KEYS */;
INSERT INTO `pattern` VALUES (1,'New',15,35,3,3),(2,'Old',10,40,3,3),(3,'NEP',10,40,1,3);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remu_perpaper`
--

LOCK TABLES `remu_perpaper` WRITE;
/*!40000 ALTER TABLE `remu_perpaper` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remuneration`
--

LOCK TABLES `remuneration` WRITE;
/*!40000 ALTER TABLE `remuneration` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrutany`
--

LOCK TABLES `scrutany` WRITE;
/*!40000 ALTER TABLE `scrutany` DISABLE KEYS */;
INSERT INTO `scrutany` VALUES (1,'2024-02-12',NULL,1,1,5,43,1,43);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'Physics',3,1),(2,'Chemistry',3,1),(3,'Mathematics',3,1),(4,'Statistics',3,1),(5,'Electronics',3,1),(6,' Computer Science',3,1),(7,' Botany',3,1),(8,' Zoology ',3,1),(9,'Microbiology',3,1),(10,'Biotechnology',3,1),(11,'Maths',3,1);
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
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'Dr.Waghmare Vishal Bansi','vishal.pri12@gmail.com',9860625005),(2,'Mrs.Dinde Mrunal Pandit','dindemrunal1996@gmail.com',8999482347),(3,' Dr.Rajashri Yashwant Patil','rajashrishendre@gmail.com',9823122121),(4,' Dr.Mujawar Irfan Kamaruddin','mujawarirfan@gmail.com',8530804020);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_course`
--

DROP TABLE IF EXISTS `teacher_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_course` (
  `teachercourse_id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `sem` int NOT NULL,
  `faculty_id` int NOT NULL,
  `coursename_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  PRIMARY KEY (`teachercourse_id`),
  KEY `fk_fieldid` (`faculty_id`),
  KEY `fk_student_id` (`subject_id`),
  KEY `fk_teacher_id` (`teacher_id`),
  CONSTRAINT `fk_fieldid` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `fk_student_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`),
  CONSTRAINT `fk_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_course`
--

LOCK TABLES `teacher_course` WRITE;
/*!40000 ALTER TABLE `teacher_course` DISABLE KEYS */;
INSERT INTO `teacher_course` VALUES (1,2,3,3,14,6,1),(2,2,4,3,16,6,1),(3,3,5,3,1,6,1),(4,3,6,3,5,6,1),(5,3,5,3,2,6,2),(6,3,6,3,9,6,2),(7,1,1,3,10,6,3),(8,1,2,3,12,6,3),(9,3,5,3,3,6,3),(10,3,6,3,6,6,3),(11,1,1,3,11,6,4),(12,1,2,3,13,6,4),(13,3,5,3,4,6,4),(14,3,6,3,8,6,4);
/*!40000 ALTER TABLE `teacher_course` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time_table`
--

LOCK TABLES `time_table` WRITE;
/*!40000 ALTER TABLE `time_table` DISABLE KEYS */;
INSERT INTO `time_table` VALUES (1,3,6,10,'2023-12-08','12:00:00','02:00:00',1,1,3),(2,3,6,11,'2023-12-11','12:00:00','02:00:00',1,1,3),(3,3,6,14,'2023-12-26','12:00:00','02:00:00',2,3,3),(4,3,6,15,'2023-12-27','12:00:00','02:00:00',2,3,3),(5,3,6,1,'2023-11-28','12:00:00','02:00:00',3,5,3),(6,3,6,2,'2023-11-29','12:00:00','02:00:00',3,5,3),(7,3,6,3,'2023-11-30','12:00:00','02:00:00',3,5,3),(8,3,6,4,'2023-12-01','12:00:00','02:00:00',3,5,3),(9,3,3,18,'2024-02-12','01:36:00','04:36:00',3,5,3);
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

-- Dump completed on 2024-02-16 22:23:02
