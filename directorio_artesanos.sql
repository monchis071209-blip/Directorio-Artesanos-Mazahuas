-- ==========================================
-- PROYECTO TRANSVERSAL
-- DIRECTORIO DIGITAL DE ARTESANOS MAZAHUAS
-- ==========================================

CREATE DATABASE directorio_artesanos;
USE directorio_artesanos;

-- ==========================================
-- TABLA ARTESANOS
-- ==========================================

CREATE TABLE artesanos(
id_artesano INT PRIMARY KEY,
nombre VARCHAR(100),
apellido VARCHAR(100),
telefono VARCHAR(20),
email VARCHAR(100),
direccion VARCHAR(150),
municipio VARCHAR(100),
descripcion VARCHAR(150),
pagina_web VARCHAR(150),
redes_sociales VARCHAR(150)
);

CREATE TABLE categorias(
id_categoria INT PRIMARY KEY,
nombre_categoria VARCHAR(100)
);

CREATE TABLE productos(
id_producto INT PRIMARY KEY,
id_artesano INT,
id_categoria INT,
nombre_producto VARCHAR(100),
descripcion_producto VARCHAR(200),
precio DECIMAL(10,2),
FOREIGN KEY(id_artesano) REFERENCES artesanos(id_artesano),
FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria)
);

-- ==========================================
-- INSERT ARTESANOS
-- ==========================================

INSERT INTO artesanos(id_artesano, nombre, apellido, telefono, email, direccion, municipio, descripcion, pagina_web, redes_sociales)
VALUES(1,'Eleazar','García Cruz','712000001','eleazar.garcia@email.com','Cabecera','San Felipe del Progreso','Elabora piezas de orfebrería y joyería tradicional mazahua.','No aplica','Facebook/EleazarGarcia'),
(2,'Abel','García Cruz','712000002','abel.garcia@email.com','San Juan Jalpa','San Felipe del Progreso','Especialista en joyería de plata con técnicas mazahuas.','No aplica','Facebook/AbelGarcia'),
(3,'Alma Rosy','Sánchez Tapia','712000003','alma.sanchez@email.com','San Pedro','San Felipe del Progreso','Elabora joyería artesanal en plata.','No aplica','Instagram/AlmaRosy'),
(4,'María Isabel','Sánchez Tapia','712000004','mariaisabel@email.com','Palmillas','San Felipe del Progreso','Diseña y fabrica joyería artesanal en plata.','No aplica','Facebook/MariaIsabel'),
(5,'Victoria Marina','García García','712000005','victoria.garcia@email.com','Dolores Hidalgo','San Felipe del Progreso','Artesana dedicada a textiles y cultura mazahua.','No aplica','Facebook/VictoriaGarcia'),
(6,'Ángela','Medrano Álvarez','712000006','angela.medrano@email.com','Tepetitlán','San Felipe del Progreso','Elabora textiles tradicionales mazahuas.','No aplica','Instagram/AngelaMedrano'),
(7,'María Rosario','Medrano Álvarez','712000007','mariarosario@email.com','San Miguel','San Felipe del Progreso','Confecciona prendas y bordados artesanales.','No aplica','Facebook/MariaRosario'),
(8,'Matías','Medrano Vilchis','712000008','matias.medrano@email.com','Barrio Norte','San Felipe del Progreso','Realiza textiles típicos de la región mazahua.','No aplica','Facebook/MatiasVilchis'),
(9,'Delfina','Olmos Esquivel','712000009','delfina.olmos@email.com','Centro','San Felipe del Progreso','Artesana especializada en tejidos y bordados.','No aplica','Facebook/DelfinaOlmos'),
(10,'Alejo','Molina Olvera','712000010','alejo.molina@email.com','Cabecera','San Felipe del Progreso','Elabora artesanías textiles tradicionales.','No aplica','Facebook/AlejoMolina'),
(11,'Elvira','Cruz Medrano','712000011','elvira.cruz@email.com','San Juan Jalpa','San Felipe del Progreso','Produce prendas y accesorios de cultura mazahua.','No aplica','Instagram/ElviraCruz'),
(12,'Graciela','Onofre León','712000012','graciela.onofre@email.com','San Pedro','San Felipe del Progreso','Confecciona textiles tradicionales hechos a mano.','No aplica','Facebook/GracielaOnofre'),
(13,'José Luis','Martínez Hernández','712000013','joseluis.martinez@email.com','Palmillas','San Felipe del Progreso','Artesano dedicado a la elaboración de textiles y bordados tradicionales mazahuas.','No aplica','Facebook/JoseLuisMartinez'),
(14,'María Fernanda','López García','712000014','mariafernanda.lopez@email.com','Dolores Hidalgo','San Felipe del Progreso','Elabora accesorios artesanales y prendas textiles con diseños tradicionales.','No aplica','Instagram/MariaFernandaLopez'),
(15,'Pedro Antonio','Ramírez Sánchez','712000015','pedro.ramirez@email.com','Tepetitlán','San Felipe del Progreso','Especialista en la elaboración de artesanías textiles hechas a mano con técnicas mazahuas.','No aplica','Facebook/PedroRamirez');

-- ==========================================
-- INSERT CATEGORIAS
-- ==========================================

INSERT INTO categorias (id_categoria, nombre_categoria) 
VALUES(1,'Orfebrería'),
(2,'Joyería'),
(3,'Joyería'),
(4,'Textil'),
(5,'Textil'),
(6,'Textil'),
(7,'Textil'),
(8,'Textil'),
(9,'Textil'),
(10,'Textil'),
(11,'Textil'),
(12,'Textil'),
(13,'Joyería'),
(14,'Textil'),
(15,'Orfebrería');

-- ==========================================
-- INSERT PRODUCTOS
-- ==========================================
INSERT INTO productos
(id_producto,id_artesano,id_categoria,nombre_producto,descripcion_producto,precio)
VALUES(1,1,4,'Anillos Mazahuas','Anillos artesanales elaborados en plata con diseño tradicional.',450.00),
(2,2,4,'Collares Artesanales','Collares tejidos y decorados con acabados artesanales.',120.00),
(3,3,4,'Pulseras Bordadas','Pulseras elaboradas con textiles y bordados mazahuas.',350.00),
(4,4,4,'Bolsa Artesanal','Bolsa de tela con bordados tradicionales hechos a mano.',280.00),
(5,5,4,'Muñeca Mazahua','Muñeca artesanal confeccionada con vestimenta tradicional.',200.00),
(6,6,4,'Mantel Bordado','Mantel bordado a mano con diseños típicos mazahuas.',600.00),
(7,7,4,'Faja Bordada','Faja tejida con colores representativos de la región.',180.00),
(8,8,4,'Collar de Chaquira','Collar elaborado con chaquira y detalles artesanales.',150.00),
(9,9,4,'Pulsera Artesanal','Pulsera tejida a mano con materiales tradicionales.',80.00),
(10,10,4,'Aretes de Chaquira','Aretes artesanales decorados con chaquira de colores.',90.00),
(11,11,4,'Morral Mazahua','Morral tejido con diseños tradicionales mazahuas.',320.00),
(12,12,4,'Portavasos Bordados','Juego de portavasos bordados a mano.',100.00),
(13,13,2,'Tapete Artesanal','Tapete tejido con fibras textiles tradicionales.',450.00),
(14,14,4,'Chal Tradicional','Chal tejido con bordados representativos de la cultura mazahua.',550.00),
(15,15,1,'Carpeta Bordada','Carpeta decorativa bordada a mano para mesa.',180.00),
(16,1,4,'Monedero Artesanal','Monedero elaborado con tela y bordados tradicionales.',90.00),
(17,2,4,'Cojín Bordado','Cojín decorativo con bordados artesanales.',250.00),
(18,3,2,'Bolsa de Mano','Bolsa pequeña confeccionada con textiles mazahuas.',150.00),
(19,4,4,'Llavero Artesanal','Llavero elaborado con figuras representativas de la cultura mazahua.',80.00),
(20,5,1,'Figura Decorativa','Figura artesanal para decoración del hogar.',260.00),
(21,6,4,'Centro de Mesa','Centro de mesa decorado con textiles y bordados.',200.00),
(22,7,4,'Bufanda Tejida','Bufanda elaborada con tejido artesanal.',190.00),
(23,8,4,'Cinturón Artesanal','Cinturón tejido con diseños tradicionales.',300.00),
(24,9,4,'Mantel Individual','Mantel individual bordado a mano.',400.00),
(25,10,4,'Bolsa Ecológica','Bolsa reutilizable con bordados artesanales.',350.00);

-- ==========================================
-- CONSULTAS
-- ==========================================
-- Mostrar todos los artesanos
SELECT * FROM artesanos;

-- Mostrar todas las categorías
SELECT * FROM categorias;

-- Mostrar todos los productos
SELECT * FROM productos;

-- Buscar un artesano por ID
SELECT * FROM artesanos
WHERE id_artesano = 1;

-- Buscar una categoría por ID
SELECT * FROM categorias
WHERE id_categoria = 1;

-- Buscar un producto por ID
SELECT * FROM productos
WHERE id_producto = 1;

-- Buscar productos por nombre
SELECT * FROM productos
WHERE nombre_producto LIKE '%Bolsa%';

-- Buscar artesanos por nombre
SELECT * FROM artesanos
WHERE nombre LIKE '%María%';

-- Modificar un artesano
UPDATE artesanos
SET
nombre='Nuevo Nombre',
apellido='Nuevo Apellido',
telefono='7121234567',
email='nuevo@email.com',
direccion='Nueva Dirección',
municipio='San Felipe del Progreso',
descripcion='Nueva descripción',
pagina_web='No aplica',
redes_sociales='Facebook/Nuevo'
WHERE id_artesano=1;

-- Modificar una categoría
UPDATE categorias
SET
nombre_categoria='Textil Tradicional'
WHERE id_categoria=1;

-- Modificar un producto
UPDATE productos
SET
id_artesano=1,
id_categoria=1,
nombre_producto='Producto Modificado',
descripcion_producto='Descripción modificada',
precio=250.00
WHERE id_producto=1;

-- Eliminar un artesano
DELETE FROM artesanos
WHERE id_artesano=15;

-- Eliminar una categoría
DELETE FROM categorias
WHERE id_categoria=15;

-- Eliminar un producto
DELETE FROM productos
WHERE id_producto=25;
