create database BancoUnivap;
use BancoUnivap;

CREATE TABLE disciplinas (
    idDisciplina int primary key AUTO_INCREMENT,
    nomeDisciplina VARCHAR(45) NOT NULL
);

CREATE TABLE professores (
    idProfessor int primary key AUTO_INCREMENT,
    nomeProfessor varchar(45),
    telefoneProfessor varchar(45),
    salarioProfessor float,
    idadeProfessor int
);

CREATE TABLE disciplinasxprofessores (
    iddisciplinasxprofessores int primary key AUTO_INCREMENT,
    curso varchar(45),
    cargaHoraria int,
    anoLetivo int,
    ID_idprofessor int,
    ID_iddisciplina int,
    foreign key  (ID_idProfessor) references professores(idProfessor),
    foreign key (ID_idDisciplina) references disciplinas(idDisciplina)
);
