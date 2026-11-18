CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE perfil (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    titulo VARCHAR(100),
    descripcion TEXT,
    banner VARCHAR(255),
    foto VARCHAR(255),
    github VARCHAR(255),
    linkedin VARCHAR(255)
);

CREATE TABLE experiencia (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    empresa VARCHAR(120),
    periodo VARCHAR(50)
);

CREATE TABLE educacion (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    institucion VARCHAR(120),
    periodo VARCHAR(50)
);

CREATE TABLE proyecto (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    fecha VARCHAR(50),
    link VARCHAR(255)
);

CREATE TABLE habilidad (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    nivel INTEGER DEFAULT 0,
    tipo VARCHAR(10) DEFAULT 'hard'
);
