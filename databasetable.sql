create database cap_project;
use cap_project
create table faculty(faculty_id int(200) primary key auto_increment,faculty varchar(200) not null unique,duration int(200) not null,sem_pattern varchar(256) not null);




create table subject(subject_id int primary key auto_increment,subject varchar(256),faculty_id int not null ,constraint fk_subject_id foreign key (faculty_id) references faculty(faculty_id));
alter table subject add pattern_id int not null;
SET FOREIGN_KEY_CHECKS = 0;
alter table subject add constraint fk_patternid foreign key (pattern_id) references pattern(pattern_id);



 create table coursename (coursename_id int primary key auto_increment,course_id varchar(200) unique,coursename varchar(200),coursefield_id int not null,constraint fk_coursename foreign key (coursefield_id) references coursefield(coursefield_id));

create table coursefield(coursefield_id int primary key auto_increment,faculty_id int not null,subject_id int not null,constraint fk_id foreign key (faculty_id) references faculty(faculty_id),constraint fk_studentid foreign key (subject_id) references subject(subject_id));
alter table coursefield add year int not null;

 alter table coursefield add sem int not null;

 create table teacher(teacher_id int primary key auto_increment,teacher_name varchar(200) not null,teacher_email varchar(200) not null,teacher_phoneno bigint(20) not null,year int not null,sem int not null,faculty_id int not null,coursename_id int not null,subject_id int not null,constraint fk_fieldid foreign key (faculty_id) references faculty(faculty_id),constraint fk_student_id foreign key (subject_id) references subject(subject_id));
#create table pattern(pattern_id int primary key auto_increment,pattern varchar(100) not null,theory_mark int(200) not null,internal_mark int(200) not null,faculty_id int not null,coursefield_id int not null,constraint fk_pattern_id foreign key (faculty_id) references faculty(faculty_id),constraint fk_patternfaculty_id foreign key (coursefield_id) references coursefield(coursefield_id));

 create table examsession(
    examsession_id int primary key auto_increment,
    month varchar(250) not null,
    exam_year year not null,
    pattern_id int not null,
    degree varchar(250) not null,
    year int not null,
    sem int not null,
    faculty_id int not null,
    constraint fk_examid foreign key (faculty_id) references faculty(faculty_id),
    constraint fk_examsession_id foreign key (pattern_id) references pattern(pattern_id)
    );




  create table time_table(
      timetable_id int primary key auto_increment,
      examsession_id int not null,
      subject_id int not null,
      coursename_id int not null,
      date date not null,
      starttime time not null,
      endtime time not null,
      constraint fk_timecourse foreign key (coursename_id) references coursename(coursename_id),
      constraint fk_timepattern foreign key (examsession_id) references examsession(examsession_id),
      constraint fk_timesubject foreign key (subject_id) references subject(subject_id)
     );   

    alter table time_table add year int not null; 
     alter table time_table add sem int not null;
     alter table time_table add faculty_id int not null;
     alter table time_table add constraint  fk_faculty_timetable foreign key (faculty_id) references faculty(faculty_id);



     create table paper_count(papercount_id int primary key auto_increment,quespaper_code varchar(200),count int,remark varchar(200),reason varchar(250),receiver_name varchar(200),received_date date,examsession_id int,timetable_id int,constraint fk_tt_id foreign key (timetable_id) references time_table(timetable_id),constraint fk_es_id foreign key (examsession_id) references examsession(examsession_id));
    alter table paper_count add column submited_name varchar(200);
    create table pattern(pattern_id int primary key auto_increment,pattern varchar(100) not null,theory_mark int(200) not null,internal_mark int(200) not null,year int not null,faculty_id int not null,constraint fk_pattern_id_fk foreign key (faculty_id) references faculty(faculty_id));

    create table issue_check(issue_check_id int primary key auto_increment,year int(50) not null,sem int not null,issue_time time not null,issue_date date not null,return_date date not null,faculty_id int,subject_id int,coursename_id int,papercount_id int,teacher_id int,constraint fk_faculty foreign key (faculty_id) references faculty(faculty_id),constraint fk_subject foreign key (subject_id) references subject(subject_id),constraint fk_coursename1 foreign key (coursename_id) references coursename(coursename_id),constraint fk_papercount foreign key (papercount_id) references paper_count(papercount_id),constraint fk_teacher foreign key (teacher_id) references teacher(teacher_id));
    ALTER TABLE issue_check DROP FOREIGN KEY fk_subject;
    ALTER TABLE issue_check DROP COLUMN subject_id;

    ALTER TABLE issue_check DROP FOREIGN KEY fk_coursename1;
    ALTER TABLE issue_check DROP COLUMN coursename_id;

    ALTER TABLE issue_check DROP FOREIGN KEY fk_faculty;
     ALTER TABLE issue_check DROP COLUMN faculty_id;

     
ALTER TABLE issue_check ADD COLUMN timetable_id INT,ADD CONSTRAINT fk_timetable FOREIGN KEY (timetable_id) REFERENCES time_table(timetable_id);

 alter table issue_check add remaining_paper int;

 alter table issue_check add teacher_paper_count int;


 <li class="sidebar-item"><a href="{{ url_for('paper_register.home') }}" class="sidebar-link"><i class="mdi mdi-note-outline"></i><span class="hide-menu"> Paper Register </span></a></li>
  <li class="sidebar-item"><a href="{{ url_for('paper_issue1.home') }}" class="sidebar-link"><i class="mdi mdi-note-outline"></i><span class="hide-menu"> Paper Issue </span></a></li>


ALTER TABLE remuneration
ADD COLUMN faculty_id INT AFTER rupees;

ALTER TABLE remuneration
ADD CONSTRAINT fk_faculty_id
FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id);

ALTER TABLE remu_perpaper
    -> ADD COLUMN faculty_id INT AFTER perpaper_rs;

 ALTER TABLE remu_perpaper
    -> ADD CONSTRAINT fk_facultyid
    -> FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id);

    #121f26;