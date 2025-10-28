# elevatelabs-RDS

##  Steps Followed

1. **Create RDS Instance**
   - Engine: MySQL 8.0
   - Instance type: db.t3.micro (Free Tier)
   - Public Access: Enabled
   - Username: admin
   - Database name: elevate
  
   - <img width="1442" height="596" alt="image" src="https://github.com/user-attachments/assets/0eb217ac-7521-4637-b916-6989956f7cc8" />
  
   - <img width="1384" height="590" alt="image" src="https://github.com/user-attachments/assets/076389c5-5258-488c-8043-15f07e928fe6" />

   - <img width="682" height="673" alt="image" src="https://github.com/user-attachments/assets/5d6acb31-a8a8-4f44-be6d-aaae541e0dfa" />


2. **Configure Access**
   - Added 0.0.0.0/0 in the security group inbound rule.
   - Allowed port 3306 for MySQL connections.

3. **Connect**
   - From AWS Cloud Shell:
  
   - <img width="1614" height="217" alt="image" src="https://github.com/user-attachments/assets/7ddfc306-0045-4f95-af9a-a5b11a8ee6ff" />
  
   - mysql -h elevate.cli40464cqa5.eu-north-1.rds.amazonaws.com -p 3306 -u admin -p
  
   - <img width="611" height="160" alt="image" src="https://github.com/user-attachments/assets/3f1d51cf-09c4-43f1-beaf-b6aa52cb2ed5" />


4. **Run SQL Commands**
   
   CREATE DATABASE demo;
   USE demo;

   CREATE TABLE students (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(50),
     domain VARCHAR(30),
     score INT
   );

   INSERT INTO students (name, domain, score)
   VALUES ('Aarav', 'Cloud', 95), ('Diya', 'DevOps', 89);

   SELECT * FROM students;

   <img width="613" height="478" alt="image" src="https://github.com/user-attachments/assets/bd26c273-4101-40e0-b6f1-23ef0e08ce72" />
5. Exit

   <img width="307" height="61" alt="image" src="https://github.com/user-attachments/assets/699b1ab6-0559-40a4-b98b-f82f4ae595a3" />

6. Delete RDS

   <img width="1600" height="270" alt="image" src="https://github.com/user-attachments/assets/1eacaa8a-95c4-4ba8-9106-d88c507eb58d" />



