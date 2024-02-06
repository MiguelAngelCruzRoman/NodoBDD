create database nodoITST;
use nodoITST;

CREATE TABLE ESTATUS (
    ID_Estatus INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Tipo VARCHAR(50) NOT NULL,
    Descripcion TEXT NOT NULL
);

CREATE TABLE ALUMNO (
    NoControl VARCHAR(8) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    PrimerNombre VARCHAR(50) NOT NULL,
    SegundoNombre VARCHAR(50) NULL,
    ApellidoPaterno VARCHAR(50) NOT NULL,
    ApellidoMaterno VARCHAR(50) NOT NULL,
    Fotografia BLOB NOT NULL,
    Semestre TINYINT(2) NOT NULL,
    CURP VARCHAR(18) UNIQUE NOT NULL,
    NSS LONG UNIQUE NOT NULL,
    CorreoInstitucional VARCHAR(37) UNIQUE NOT NULL,
    CorreoPersonal VARCHAR(100) NOT NULL,
    NumeroContacto LONG NOT NULL,
    CreditosAprobados INTEGER NOT NULL,
    FechaIngreso DATE NOT NULL,
    FechaEgreso DATE NULL,
    ID_Estatus_Estatus INT NOT NULL,
    FOREIGN KEY (ID_Estatus_Estatus)
        REFERENCES ESTATUS (ID_Estatus)
);

CREATE TABLE DIRECCION (
    ID_Direccion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    CP SMALLINT NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    Municipio VARCHAR(50) NOT NULL,
    Colonia VARCHAR(50) NOT NULL,
    Calle VARCHAR(50) NOT NULL,
    NoExt SMALLINT NOT NULL,
    NoInt VARCHAR(5) NULL,
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE SERVICIO_SOCIAL (
    ID_Servicio_Social INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    HorasPlaneadas FLOAT NOT NULL,
    HorasLaboradas FLOAT NOT NULL,
    NombreLugar VARCHAR(100) NOT NULL,
    AreaAplicacion VARCHAR(50) NOT NULL,
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE DOCUMENTO (
    ID_Documento INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion TEXT NOT NULL,
    Ejemplo BLOB NOT NULL,
    RequisitosAdicionales TEXT NULL
);

CREATE TABLE DOCUMENTO_ALUMNO (
    ID_Documento_Alumno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Documento INT NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    Archivo BLOB NOT NULL,
    FechaPresentacion DATE NOT NULL,
    FechaVencimiento DATE NULL,
    Observaciones TEXT NULL,
    Estado VARCHAR(10) NOT NULL,
    FOREIGN KEY (ID_Documento)
        REFERENCES DOCUMENTO (ID_Documento),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE BECA (
    ID_Beca INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Beneficios TEXT NOT NULL,
    Duracion VARCHAR(50) NOT NULL,
    Requsitos TEXT NOT NULL
);

CREATE TABLE BECA_ALUMNO (
    ID_Beca_Alumno INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    ID_Beca INT NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFinal DATE NULL,
    FOREIGN KEY (ID_Beca)
        REFERENCES BECA (ID_Beca),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE EMPLEADO (
    ID_Empleado INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    PrimerNombre VARCHAR(50) NOT NULL,
    SegundoNombre VARCHAR(50) NULL,
    ApellidoPaterno VARCHAR(50) NOT NULL,
    ApellidoMaterno VARCHAR(50) NOT NULL,
    CURP VARCHAR(18) UNIQUE NOT NULL,
    NSS LONG UNIQUE NOT NULL,
    Antiguedad TINYINT NOT NULL,
    Division VARCHAR(50) NULL,
    Ocupacion VARCHAR(50) NULL,
    GradoEscolar VARCHAR(100) NOT NULL,
    FechaContratacion DATE NOT NULL,
    DiasVacaciones TINYINT NOT NULL,
    Fecha_Jubilacion DATE NULL
);

CREATE TABLE DOCENTE (
    ID_Empleado INT PRIMARY KEY NOT NULL,
    TipoContrato BOOLEAN NOT NULL,
    AreaConocimiento VARCHAR(50) NOT NULL,
    Experiencia TINYINT(2) NOT NULL,
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE ADMINISTRATIVO (
    ID_Empleado INT PRIMARY KEY NOT NULL,
    Area VARCHAR(20) NOT NULL,
    Cargo VARCHAR(30) NOT NULL,
    DescripcionPuesto TEXT NOT NULL,
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE NORMATIVA (
    ID_Normativa INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(250) NOT NULL,
    Descripcion TEXT NOT NULL,
    Accion TEXT NOT NULL,
    Sancion TEXT NOT NULL,
    AdministrativoAprovador INTEGER NOT NULL,
    FOREIGN KEY (AdministrativoAprovador)
        REFERENCES ADMINISTRATIVO (ID_Empleado)
);


CREATE TABLE CONVENIO (
    ID_Convenio INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Representante INTEGER NOT NULL,
    Objetivo VARCHAR(50) NOT NULL,
    Descripcion TEXT NOT NULL,
    FechaPublicacion DATE NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    Participantes TEXT NOT NULL,
    FOREIGN KEY (Representante)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE CERTIFICADO (
    ID_Certificado INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Duracion TINYINT(2) NOT NULL,
    Modalidad VARCHAR(30) NOT NULL,
    ID_Convenio INTEGER NULL,
    FOREIGN KEY (ID_Convenio)
        REFERENCES CONVENIO (ID_Convenio)
);

CREATE TABLE CERTIFICACION_ALUMNO (
    ID_Certificacion_Alumno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    Observaciones TEXT NULL,
    ID_Certificado INT NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    ID_Estatus INT NOT NULL,
    FOREIGN KEY (ID_Certificado)
        REFERENCES CERTIFICADO (ID_Certificado),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl),
    FOREIGN KEY (ID_Estatus)
        REFERENCES ESTATUS (ID_Estatus)
);

CREATE TABLE CERTIFICADO_EMPLEADO (
    ID_Certificacion_Empleado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    Observaciones TEXT NULL,
    ID_Certificado INT NOT NULL,
    ID_Empleado INT NOT NULL,
    ID_Estatus INT NOT NULL,
    FOREIGN KEY (ID_Certificado)
        REFERENCES CERTIFICADO (ID_Certificado),
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado),
    FOREIGN KEY (ID_Estatus)
        REFERENCES ESTATUS (ID_Estatus)
);

CREATE TABLE CICLO (
    ID_Ciclo VARCHAR(9) NOT NULL PRIMARY KEY,
    Director INTEGER NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    FOREIGN KEY (Director)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE NOMINA (
    ID_Nomina INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_Empleado INTEGER NOT NULL,
    Monto FLOAT NOT NULL,
    Periodo VARCHAR(50) NOT NULL,
    DiasTrabajados INTEGER NOT NULL,
    Faltas INTEGER NOT NULL,
    Deducciones VARCHAR(50) NOT NULL,
    Sueldo FLOAT NOT NULL,
    TipoPago VARCHAR(30),
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE TITULACION (
    ID_Titulacion INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    Asesor INTEGER NOT NULL,
    Grado VARCHAR(100) NOT NULL,
    Area VARCHAR(50) NOT NULL,
    FechaTitulacion DATE NOT NULL,
    Division VARCHAR(20) NOT NULL,
    Objetivo TEXT NOT NULL,
    Calificacion FLOAT NOT NULL,
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl),
    FOREIGN KEY (Asesor)
        REFERENCES DOCENTE (ID_Empleado)
);

CREATE TABLE TESIS (
    ID_Tesis INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Titulo VARCHAR(100) NOT NULL,
    Resumen TEXT NOT NULL,
    FechaPublicacion DATE NOT NULL,
    Colaborador VARCHAR(250) NULL,
    ID_Titulacion INTEGER NOT NULL,
    FOREIGN KEY (ID_Titulacion)
        REFERENCES TITULACION (ID_Titulacion)
);

CREATE TABLE PLAN_ESTUDIO (
    Clave VARCHAR(20) NOT NULL PRIMARY KEY,
    Especialidad VARCHAR(50) NOT NULL,
    Grupos VARCHAR(10) NOT NULL,
    Sistema VARCHAR(20) NOT NULL,
    InicioVigengia DATE NOT NULL,
    FinVigencia DATE NOT NULL,
    FechaElaboracion DATE NOT NULL
);

CREATE TABLE LICENCIATURA (
    ID_Licenciatura VARCHAR(3) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(100) NOT NULL,
    Duracion TINYINT(2) NOT NULL,
    ObjetivoGeneral TEXT NOT NULL,
    Mision TEXT NOT NULL,
    Vision TEXT NOT NULL,
    PerfilAspirante TEXT NOT NULL,
    PerfilEgresado TEXT NOT NULL,
    Logo BLOB NOT NULL,
    Clave_Plan_Estudios VARCHAR(20),
    FOREIGN KEY (Clave_Plan_Estudios)
        REFERENCES PLAN_ESTUDIO (Clave)
);

CREATE TABLE ALUMNO_LICENCIATURA (
    ID_Alumno_Licenciatura INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_Licenciatura VARCHAR(3) NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    FOREIGN KEY (ID_Licenciatura)
        REFERENCES LICENCIATURA (ID_Licenciatura),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE MATERIA (
    ClaveOficial VARCHAR(8) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Unidades TINYINT(2) NOT NULL,
    Creditos TINYINT(2) NOT NULL,
    HorasPracticas TINYINT(2) NOT NULL,
    HorasTeoricas TINYINT(2) NOT NULL
);

CREATE TABLE RETICULA (
    Clave VARCHAR(13) NOT NULL PRIMARY KEY,
    ClaveOficial_Materia VARCHAR(8) NOT NULL,
    Clave_Plan_Estudios VARCHAR(20) NOT NULL,
    FOREIGN KEY (ClaveOficial_Materia)
        REFERENCES MATERIA (ClaveOficial),
    FOREIGN KEY (Clave_Plan_Estudios)
        REFERENCES PLAN_ESTUDIO (Clave)
);

CREATE TABLE CURSO (
    Clave VARCHAR(4) PRIMARY KEY,
    Semestre TINYINT(2) NOT NULL,
    LetraGrupo VARCHAR(1) NOT NULL,
    ID_Ciclo VARCHAR(9) NOT NULL,
    ID_Licenciatura VARCHAR(3) NOT NULL,
    ClaveOficial_Materia VARCHAR(8) NOT NULL,
    ID_Empleado_Docente INT NOT NULL,
    FOREIGN KEY (ID_Ciclo)
        REFERENCES CICLO (ID_Ciclo),
    FOREIGN KEY (ID_Licenciatura)
        REFERENCES LICENCIATURA (ID_Licenciatura),
    FOREIGN KEY (ClaveOficial_Materia)
        REFERENCES MATERIA (ClaveOficial),
    FOREIGN KEY (ID_Empleado_Docente)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE CALIFICACION (
    ID_Evalucacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Acreditacion BOOLEAN NOT NULL,
    Puntuacion INT NOT NULL,
    Clave_Curso VARCHAR(4) NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    ID_Estatus_Estatus INT NOT NULL,
    FOREIGN KEY (Clave_Curso)
        REFERENCES CURSO (Clave),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl),
    FOREIGN KEY (ID_Estatus_Estatus)
        REFERENCES ESTATUS (ID_Estatus)
);

CREATE TABLE EDIFICIO (
    ID_Edificio VARCHAR(1) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    FechaConstruccion DATE NOT NULL,
    Pisos TINYINT(1) NOT NULL,
    Proposito TEXT NOT NULL
);

CREATE TABLE DEPARTAMENTO (
    ID_Departamento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Finalidad TEXT NOT NULL,
    ID_Empleado_Responsable INT NOT NULL,
    ID_Edificio VARCHAR(1) NOT NULL,
    FOREIGN KEY (ID_Empleado_Responsable)
        REFERENCES EMPLEADO (ID_Empleado),
    FOREIGN KEY (ID_Edificio)
        REFERENCES EDIFICIO (ID_Edificio)
);

CREATE TABLE EMPLEADO_DEPARTAMENTO (
    ID_Empleado_Departamento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Empleado INT NOT NULL,
    ID_Departamento INT NOT NULL,
    FechaInicioLabor DATE NOT NULL,
    FechaFinLabor DATE NULL,
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado),
    FOREIGN KEY (ID_Departamento)
        REFERENCES DEPARTAMENTO (ID_Departamento)
);

CREATE TABLE AULA (
    ID_Aula INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Edificio VARCHAR(1) NOT NULL,
    NumeroSalon SMALLINT(3) NOT NULL,
    Capacidad TINYINT NOT NULL,
    Descripcion TEXT,
    FOREIGN KEY (ID_Edificio)
        REFERENCES EDIFICIO (ID_Edificio)
);

CREATE TABLE MOBILIARIO (
    ID_Mobiliario INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(50) NOT NULL,
    Estado VARCHAR(20) NOT NULL,
    Detalles TEXT NOT NULL
);

CREATE TABLE AULA_MOBILIARIO (
    ID_Aula_Mobiliario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Mobiliario INT NOT NULL,
    ID_Aula INT NOT NULL,
    FOREIGN KEY (ID_Mobiliario)
        REFERENCES MOBILIARIO (ID_Mobiliario),
    FOREIGN KEY (ID_Aula)
        REFERENCES AULA (ID_Aula)
);

CREATE TABLE HORARIO (
    ID_Horario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    DiaSemana VARCHAR(10) NOT NULL,
    HoraInicio TIME NOT NULL,
    HoraFinal TIME NOT NULL
);

CREATE TABLE CLASE (
    ID_CLASE INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ID_Aula INT NOT NULL,
    ID_Horario INT NOT NULL,
    Clave_Curso VARCHAR(4) NOT NULL,
    FOREIGN KEY (ID_Aula)
        REFERENCES AULA (ID_Aula),
    FOREIGN KEY (ID_Horario)
        REFERENCES HORARIO (ID_Horario),
    FOREIGN KEY (Clave_Curso)
        REFERENCES CURSO (Clave)
);

CREATE TABLE ALUMNO_CLASE (
    ID_GRUPO INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ID_CLASE INT NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    FOREIGN KEY (ID_CLASE)
        REFERENCES CLASE (ID_Clase),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE POSTGRADO (
    ID_Postgrado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Duracion TINYINT(2) NOT NULL,
    ObjetivoGeneral TEXT NOT NULL,
    ObjetivosEspecificos TEXT NOT NULL,
    LineaInvestigacion VARCHAR(50) NOT NULL,
    PerfilEgreso TEXT NOT NULL,
    PerfilIngreso TEXT NOT NULL
);

CREATE TABLE ALUMNO_POSTGRADO (
    ID_Alumno_Postgrado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Postgrado INT NOT NULL,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    FOREIGN KEY (ID_Postgrado)
        REFERENCES POSTGRADO (ID_Postgrado),
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl)
);

CREATE TABLE PLATAFORMA (
    ID_Plataforma INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    CapacidadUsuarios INTEGER NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Descripcion TEXT NOT NULL,
    URL VARCHAR(250) NOT NULL,
    ID_Ciclo VARCHAR(9) NOT NULL,
    FOREIGN KEY (ID_Ciclo)
        REFERENCES CICLO (ID_Ciclo)
);

CREATE TABLE PLATAFORMA_EMPLEADO (
    ID_Plataforma_Empleado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Plataforma INT NOT NULL,
    ID_Empleado INT NOT NULL,
    NombreUsuario VARCHAR(50) NOT NULL,
    Contrasenia VARCHAR(50) NOT NULL,
    FOREIGN KEY (ID_Plataforma)
        REFERENCES PLATAFORMA (ID_Plataforma),
    FOREIGN KEY (ID_Empleado)
        REFERENCES EMPLEADO (ID_Empleado)
);

CREATE TABLE PLATAFORMA_ALUMNO (
    ID_Plataforma_Alumno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NoControl_Alumno VARCHAR(8) NOT NULL,
    ID_Plataforma INT NOT NULL,
    NombreUsuario VARCHAR(50) NOT NULL,
    Contrasenia VARCHAR(50) NOT NULL,
    FOREIGN KEY (NoControl_Alumno)
        REFERENCES ALUMNO (NoControl),
    FOREIGN KEY (ID_Plataforma)
        REFERENCES PLATAFORMA (ID_Plataforma)
);