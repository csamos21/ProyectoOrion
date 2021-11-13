import sqlite3

#Conexión a la Base de Datos
con = sqlite3.connect('orion.db')

#Creando cursor
pibote = con.cursor()

#Creando la tabla
try:
    pibote.execute ("""
    CREATE TABLE usuarios (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
    codigo_usuario varchar (15) NOT NULL UNIQUE, 
    email_usuario varchar (255) NOT NULL, 
    nombre_usuario varchar (255) NOT NULL, 
    cargo varchar (15) DEFAULT NULL, 
    foto varchar (100) DEFAULT NULL, 
    codigo_rol varchar (15) NOT NULL, 
    password varchar (102) NOT NULL, 
    codigo_pais varchar (15) DEFAULT NULL, 
    direccion varchar (255) DEFAULT NULL, 
    telefono varchar (50) NOT NULL, 
    celular varchar (50) NOT NULL, 
    ciudad varchar (50) DEFAULT NULL, 
    fecha_ult_con datetime DEFAULT NULL, 
    intentos decimal (15, 0) DEFAULT NULL, 
    bloqueo decimal (15, 0) DEFAULT NULL, 
    fecha_usuario datetime DEFAULT NULL, 
    fecha_password datetime DEFAULT NULL, 
    estado char (1) NOT NULL DEFAULT 1, 
    estado_password INT DEFAULT (0));
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE baja_productos(
  id_baja INTEGER PRIMARY KEY AutoIncrement, 
  id_prod_lote INTEGER NOT NULL, 
  fecha_baja DATE NOT NULL DEFAULT (2000-01-01), 
  motivo_baja TEXT, 
  cod_usuario VARCHAR(15), 
  fecha_sistema DATE DEFAULT CURRENT_TIMESTAMP
  );
    """)
except Exception as e:
    print(e)


try:
    pibote.execute ("""
CREATE TABLE productos(
  id_producto INTEGER PRIMARY KEY AutoIncrement, 
  cod_producto VARCHAR(10) NOT NULL UNIQUE ON CONFLICT ROLLBACK, 
  nombre VARCHAR(255) NOT NULL, 
  descripcion TEXT,
  imagen VARCHAR(255) NOT NULL DEFAULT "../static/img/None.png",
  tipo_unidad CHAR(2) NOT NULL DEFAULT 01, 
  valor_unitario DOUBLE NOT NULL DEFAULT 0, 
  calificacion_producto INT NOT NULL DEFAULT 5, 
  descuento CHAR(1) NOT NULL DEFAULT 0, 
  comentarios TEXT,
  fecha_sistema datetime DEFAULT CURRENT_TIMESTAMP
  );    
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE lote_productos(
  id_prod_lote INTEGER PRIMARY KEY AutoIncrement, 
  cod_lote VARCHAR(15) NOT NULL, 
  id_producto INTEGER NOT NULL REFERENCES productos(id_producto) ON DELETE RESTRICT ON UPDATE CASCADE, 
  cant_std_prod DOUBLE NOT NULL DEFAULT 0, 
  fecha_entrada_inv DATE NOT NULL DEFAULT (2000 - 01 - 01), 
  cant_salidas DOUBLE DEFAULT 0,
  fecha_sistema datetime DEFAULT CURRENT_TIMESTAMP
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE salidas_productos(
  id_salida INTEGER PRIMARY KEY AutoIncrement, 
  id_prod_lote INTEGER NOT NULL REFERENCES lote_productos(id_prod_lote) ON DELETE RESTRICT ON UPDATE CASCADE, 
  tipo_salida CHAR(2) NOT NULL DEFAULT 01, 
  fecha_salida DATE NOT NULL DEFAULT (2000 - 01 - 01), 
  descripcion TEXT,
  fecha_sistema DATE DEFAULT CURRENT_TIMESTAMP
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE baja_productos(
  id_baja INTEGER PRIMARY KEY AutoIncrement, 
  id_prod_lote INTEGER NOT NULL REFERENCES lote_productos(id_prod_lote) ON DELETE RESTRICT ON UPDATE CASCADE, 
  fecha_baja DATE NOT NULL DEFAULT (2000-01-01), 
  motivo_baja TEXT, 
  cod_usuario VARCHAR(15), 
  fecha_sistema DATE DEFAULT CURRENT_TIMESTAMP
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE roles (
  codigo_rol varchar(15) NOT NULL,
  nombre_rol varchar(255) NOT NULL,
  prioridad decimal(10,0) NOT NULL DEFAULT 1,
  PRIMARY KEY (codigo_rol)
);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX cod_producto_UNIQUE on productos(codigo_producto);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX codigo_usuario_UNIQUE on usuarios(codigo_usuario);
    """)
except Exception as e:
    print(e)

try: 
    pibote.execute("""
insert into productos (cod_producto, nombre, descripcion, tipo_unidad, valor_unitario, calificacion_producto, descuento, comentarios)
Values ('001', 'Orion-SHOCK', '','PZA' , 125000, 5, 1, ""), ('100', 'TREX-Orion', '', 'PZA' , 125000, 5, 1, ""),
       ('011', 'Orion-GAMER', '', 'PZA' , 125000, 5, 1, "") ,('101', 'BLACK-Orion', '', 'KIT' , 125000, 5, 1, ""),
       ('021', 'Orion-SHOOT', '', 'PZA' , 125000, 5, 1, "") ,('111', 'ORANGE-Orion', '', 'PZA' , 125000, 5, 1, ""),
       ('031', 'Orion-KSIUS', '', 'KIT' , 125000, 5, 1, "") ,('121', 'SHOW-Orion', '', 'PZA' , 125000, 5, 1, ""),
       ('041', 'Orion-MOON', '', 'PZA' , 125000, 5, 1, "") ,('131', 'WATER-Orion', '', 'PZA' , 125000, 5, 1, ""),
       ('051', 'Orion-DREAM', '', 'PZA' , 125000, 5, 1, "") ,('141', 'SPLASH-Orion-SHOCK', '', 'PZA' , 125000, 5, 1, ""),
       ('061', 'Orion-TEAM', '', 'PCK' , 125000, 5, 1, "") ,('151', 'WHIPLASH-Orion', '', 'DZN' , 125000, 5, 1, ""),
       ('071', 'Orion-SOCCER', '', 'PZA' , 125000, 5, 1, "") ,('161', 'CSAMOS-Orion', '', 'PZA' , 125000, 5, 1, "");
    """)
except Exception as e:
    print(e)

try: 
    pibote.execute("""
insert into lote_productos ( cod_lote, id_producto, cant_std_prod, fecha_entrada_inv)
Values ('0010000001',1,100, date('now')),('1000000001',2,100, date('now')),
       ('0110000001',3,100, date('now')),('1010000001',4,100, date('now')),
       ('0210000001',5,100, date('now')),('1110000001',6,100, date('now')),
       ('0310000001',7,100, date('now')),('1210000001',8,100, date('now')),
       ('0410000001',9,100, date('now')),('1310000001',10,100, date('now')),
       ('0510000001',11,100, date('now')),('1410000001',12,100, date('now')),
       ('0610000001',13,100, date('now')),('1510000001',14,100, date('now')),
       ('0710000001',15,100, date('now')),('1610000001',16,100, date('now')),
       ('0010000002',1,100, date('now')),('1000000002',2,100, date('now')),
       ('0010000003',1,100, date('now')),('1000000003',2,100, date('now')),
       ('0010000004',1,100, date('now')),('1000000004',2,100, date('now')),
       ('0310000002',7,100, date('now')),('1000000005',2,100, date('now')),
       ('0310000003',7,100, date('now')),('1310000002',10,100, date('now')),
       ('0310000004',7,100, date('now')),('1310000003',10,100, date('now')),
       ('0310000005',7,100, date('now')),('1310000004',10,100, date('now')),
       ('0710000002',15,100, date('now')),('1310000005',10,100, date('now'));
    """)
except Exception as e:
    print(e)

try: 
    pibote.execute("""
    INSERT INTO usuarios (codigo_usuario, nombre_usuario, email_usuario, cargo, foto, codigo_rol,
                password, codigo_pais, direccion, telefono, celular, ciudad, fecha_ult_con, intentos, bloqueo,
                fecha_usuario, fecha_password, estado ) 
    VALUES ('asesor01', 'Asesor Virtual 01', 'asesor@orion.com.co', 'Administrador Tienda', '', 'USER', 'pbkdf2:sha256:260000$JDJagGGCvlRU6aUM$0a2ef98b09f2a496ed4a20a4c73c8718e8fe77e1f7362d403f4715746f10ae6c', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' ),
           ('SuperAdministrador', 'SUPERADMIN', 'superadmin@orion.com.co', 'Super Administrador', '', 'SADMIN', 'pbkdf2:sha256:260000$JDJagGGCvlRU6aUM$0a2ef98b09f2a496ed4a20a4c73c8718e8fe77e1f7362d403f4715746f10ae6c', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' ),
           ('cliente01', 'Comprador Virtual', 'user01@hotmail.com', 'Usuario Final', '', 'CLIENT', 'pbkdf2:sha256:260000$JDJagGGCvlRU6aUM$0a2ef98b09f2a496ed4a20a4c73c8718e8fe77e1f7362d403f4715746f10ae6c', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' );
        """)
except Exception as e:
    print(e)


try: 
    pibote.execute("""
    INSERT INTO roles (codigo_rol, nombre_rol, prioridad) 
    VALUES ('USER', 'Usuario Interno', 100),
           ('SADMIN', 'Super Administrador', 200),
           ('CLIENT', 'Uusario Externo - Cliente', 10);
        """)
except Exception as e:
    print(e)

con.commit()

con.close()