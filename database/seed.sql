-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: student_result_db
-- ------------------------------------------------------
-- Server version	8.4.6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1500000$y8Jdim25fHHpUQHrONIbL7$EA3j5lZmWHlXbXVjDnb0QWbhMRnmhbhBNhqQIWwzqfE=','2026-09-22 12:48:34.605532',1,'admin','','','ujwalamohane@bitbaroda.com',1,1,'2026-09-22 08:05:15.610669'),(2,'pbkdf2_sha256$1500000$3NSQ2Y8CNrSkM5TzzCwXey$tlI1sXapC7980ak0NtNTlyNjjIx97D0EGPQM6SwjBF8=','2026-09-22 11:56:34.752103',0,'teacher1','teacher uj','m','',0,1,'2026-09-22 11:19:48.000000'),(3,'pbkdf2_sha256$1500000$Qpp2uKH9d7NJwUxMt4qYxt$Pt7u2ofFpHPQggjfBQonfQjRhQSvUrpNwbyE3nm7XYk=','2026-09-22 12:55:52.904197',0,'student1','','','',0,1,'2026-09-22 11:28:25.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (9,2,28),(1,2,32),(2,2,36),(3,2,40),(4,2,41),(5,2,42),(6,2,44),(7,2,45),(8,2,48),(14,3,28),(10,3,32),(11,3,36),(12,3,44),(13,3,48);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `classes_class`
--

LOCK TABLES `classes_class` WRITE;
/*!40000 ALTER TABLE `classes_class` DISABLE KEYS */;
INSERT INTO `classes_class` VALUES (1,'class 12th','A','2026-2027'),(2,'class 12th','A','2026-2027');
/*!40000 ALTER TABLE `classes_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-09-22 08:07:19.183685','1','class 12th - A',1,'[{\"added\": {}}]',7,1),(2,'2026-09-22 08:07:20.938589','2','class 12th - A',1,'[{\"added\": {}}]',7,1),(3,'2026-09-22 08:08:09.239001','1','PY01 - Python Programming',1,'[{\"added\": {}}]',8,1),(4,'2026-09-22 08:08:27.944648','1','semester I - 2026-2027',1,'[{\"added\": {}}]',11,1),(5,'2026-09-22 09:49:34.677354','1','01 - Ujwala Mohane',1,'[{\"added\": {}}]',9,1),(6,'2026-09-22 11:19:53.796761','2','teacher1',1,'[{\"added\": {}}]',4,1),(7,'2026-09-22 11:27:07.710194','2','teacher1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Groups\", \"User permissions\"]}}]',4,1),(8,'2026-09-22 11:28:31.932311','3','student1',1,'[{\"added\": {}}]',4,1),(9,'2026-09-22 11:31:28.240620','3','student1',2,'[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\"]}}]',4,1),(10,'2026-09-22 12:49:51.492191','2','02 - priyani',1,'[{\"added\": {}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `results_exam`
--

LOCK TABLES `results_exam` WRITE;
/*!40000 ALTER TABLE `results_exam` DISABLE KEYS */;
INSERT INTO `results_exam` VALUES (1,'semester I','2026-2027');
/*!40000 ALTER TABLE `results_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `results_result`
--

LOCK TABLES `results_result` WRITE;
/*!40000 ALTER TABLE `results_result` DISABLE KEYS */;
INSERT INTO `results_result` VALUES (1,90.00,100.00,'A+','excellent!!                    ','2026-09-22 11:57:04.409230','2026-09-22 12:38:15.503254',1,1,1);
/*!40000 ALTER TABLE `results_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `students_student`
--

LOCK TABLES `students_student` WRITE;
/*!40000 ALTER TABLE `students_student` DISABLE KEYS */;
INSERT INTO `students_student` VALUES (1,'01','Ujwala Mohane','uj@gmail.com','2017-09-22','Female','122124545','sayajigunj BIT',1,1),(2,'02','priyani','pri@gmail.com','2008-09-12','Female','8965663223','ratlam',1,3);
/*!40000 ALTER TABLE `students_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `subjects_subject`
--

LOCK TABLES `subjects_subject` WRITE;
/*!40000 ALTER TABLE `subjects_subject` DISABLE KEYS */;
INSERT INTO `subjects_subject` VALUES (1,'Python Programming','PY01');
/*!40000 ALTER TABLE `subjects_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `teachers_teacher`
--

LOCK TABLES `teachers_teacher` WRITE;
/*!40000 ALTER TABLE `teachers_teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `teachers_teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-23 13:06:12
