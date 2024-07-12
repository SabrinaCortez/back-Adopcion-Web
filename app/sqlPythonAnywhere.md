Database host address:adrianreciomdq.mysql.pythonanywhere-services.com
Username:adrianreciomdq
Clave Base www.pythonanywhere.com
base adrianreciomdq$adopciones

use adrianreciomdq$adopciones;
show tables;

CREATE TABLE tipoanimal(
    cidTipoAnimal VARCHAR(2) PRIMARY KEY,
    cDescripcion VARCHAR(45) NOT NULL
);
CREATE TABLE tipoestado(
    cidTipoEstado  VARCHAR(2) PRIMARY KEY,
    cDescripcion VARCHAR(45) NOT NULL
);

INSERT INTO tipoestado (cidTipoEstado,cDescripcion) VALUES ('AD','Adoptado');
INSERT INTO tipoestado (cidTipoEstado,cDescripcion) VALUES ('TR','En transito');
INSERT INTO tipoestado (cidTipoEstado,cDescripcion) VALUES ('PU','Publicado');

INSERT INTO tipoanimal (cidTipoAnimal,cDescripcion) VALUES ('PE','Perro');
INSERT INTO tipoanimal (cidTipoAnimal,cDescripcion) VALUES ('GA','Gato');
INSERT INTO tipoanimal (cidTipoAnimal,cDescripcion) VALUES ('CO','Conejo');

CREATE TABLE animales (
    idAnimales INT AUTO_INCREMENT PRIMARY KEY,
    cNombre VARCHAR(45) NOT NULL,
    cRaza VARCHAR(45) NOT NULL,
    cEdad varchar(10), 
    cCondicionEspecial VARCHAR(45) NOT NULL,
    cSexo char(1) NOT NULL,
    cidTipoAnimal VARCHAR(2) NOT NULL,
    cImagen VARCHAR(45) NOT NULL

);

CREATE TABLE estados(
    idAnimales INT NOT NULL,
    cidTipoEstado  VARCHAR(2) NOT NULL,
    dDesde date NOT NULL,
    dHasta date,
    cDNI varchar(8) ,
    cDescripcion VARCHAR(45)
);

CREATE TABLE adoptante(
    cDNI varchar(8)  NOT NULL,
    cNombreyApellido varchar(45) NOT NULL,
    cCorreo varchar(45) NOT NULL,
    cLinkInstagram varchar(45) NOT NULL,
    cTelefono varchar(45) NOT NULL,
    dFechaNacimiento date,
    cGenero char(1),
    nPrimeraMascota  int,
    nTieneMascota  int,
    nEstaCastrada   int,
    cCasaDepartamento char(1),
    nTieneBalcon int,
    nCantidadPersonaEnElhogar int,
    nDispuestoAsumirCostos int,
    nSuscribirme int,
    cMensaje varchar(250)

);

INSERT INTO animales (cNombre, cRaza, cEdad, cCondicionEspecial, cSexo, cidTipoAnimal, cImagen) 
VALUES 
('Balto', 'mestizo', '1', 'Ninguna', 'M', 'PE', 'perros/balto.jpeg'),
('Chuletas', 'bulldog frances', '1', 'Ninguna', 'H', 'PE', 'perros/chuletas.jpeg'),
('Firulais', 'mestizo', '2', 'Ninguna', 'M', 'PE', 'perros/firulais.jpg'),
('Reino', 'chihuahua', '1', 'Ninguna', 'M', 'PE', 'perros/reino.jpg'),
('Bigotes', 'mestizo', '1', 'diabetes', 'M', 'GA', 'gatos/bigotes.jpg'),
('Pelusa', 'mestizo', '1', 'diabetes', 'H', 'GA', 'gatos/pelusa.jpg'),
('Nube', 'mestizo', '2', 'diabetes', 'H', 'GA', 'gatos/nube.jpg'),
('Rayito', 'mestizo', '1', 'diabetes', 'M', 'GA', 'gatos/rayito.jpeg'),
('Fidel', 'mestizo', '2', 'diabetes', 'M', 'GA', 'gatos/fidel.jpg'),
('Cleo', 'Siames', '2', 'diabetes', 'H', 'GA', 'gatos/cleo.jpg'),
('Polo', 'mestizo', '1', 'Ninguna', 'M', 'PE', 'perros/polo.jpg'),
('Copito', 'mestizo', '1 año', 'Ninguna', 'M', 'GA', 'gatos/copito.jpg'),
('Robin', 'mestizo', '3 años', 'Ninguna', 'M', 'GA', 'gatos/robin.jpg'),
('Milan', 'mestizo', '2 meses', 'Ninguna', 'M', 'GA', 'gatos/mmilan.jpg'),
('Loki', 'mestizo', '1', 'Ninguna', 'M', 'PE', 'perros/loki.jpeg');

 INSERT INTO  estados (idAnimales, cidTipoEstado, dDesde, dHasta, cDNI, cDescripcion) 
 VALUES
  (15, 'TR', '2024-07-01', null, null, 'Feliz'),
 (11, 'TR', '2024-07-01', null, null, 'Feliz'),
 (12, 'TR', '2024-07-01', null, null, 'Muy Feliz'),
 (13, 'TR', '2024-07-01', null, null, 'Muy Feliz'),
 (14, 'TR', '2024-07-01', null, null, 'Muy Feliz'),
   (1, 'PU', '2024-07-01', null, null, 'Feliz'),
  (2, 'PU', '2024-07-01', null, null, 'Feliz'),
  (3, 'PU', '2024-07-01', null, null, 'Feliz'),
  (4, 'PU', '2024-07-01', null, null, 'Feliz'),
  (5, 'PU', '2024-07-01', null, null, 'Feliz'),
  (6, 'PU', '2024-07-01', null, null, 'Feliz'),
  (7, 'PU', '2024-07-01', null, null, 'Feliz'),
  (8, 'PU', '2024-07-01', null, null, 'Feliz'),
  (9, 'PU', '2024-07-01', null, null, 'Feliz'),
  (10, 'PU', '2024-07-01', null, null, 'Feliz');