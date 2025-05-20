import enum
from sqlalchemy import Enum, create_engine, DateTime, Column, Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DB_NAME = 'tarea2'
DB_USERNAME = 'cc5002'
DB_PASSWORD = 'programacionweb'
DB_HOST = '127.0.0.1'
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()




class Actividad(Base):
    __tablename__ = 'actividad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), default=None)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), default=None)
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime, default=None)
    descripcion = Column(String(500), default=None)

    temas = relationship("ActividadTema", back_populates="actividad", cascade="all, delete", lazy='subquery')
    fotos = relationship("Foto", back_populates="actividad", cascade="all, delete", lazy='subquery')
    contactar_por = relationship("ContactarPor", back_populates="actividad", cascade="all, delete")
    comuna = relationship("Comuna", back_populates="actividades", lazy='subquery')


class TemaEnum(enum.Enum):
    música = 1
    deporte = 2
    ciencias = 3
    religión = 4
    política = 5
    tecnología = 6
    juegos = 7
    baile = 8
    comida = 9
    otro = 10

class ActividadTema(Base):
    __tablename__ = 'actividad_tema'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tema = Column(Enum(TemaEnum), nullable=False)
    glosa_otro = Column(String(15), default=None)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False, primary_key=True)

    actividad = relationship("Actividad", back_populates="temas")

class Comuna(Base):
    __tablename__ = 'comuna'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna", cascade="all, delete")

class NombreEnum(enum.Enum):
    whatsapp = 1
    telegram= 2
    instagram = 3
    tiktok = 4
    otra = 5

class ContactarPor(Base):
    __tablename__ = 'contactar_por'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(Enum(NombreEnum), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False, primary_key=True)

    actividad = relationship("Actividad", back_populates="contactar_por")

class Foto(Base):
    __tablename__ = 'foto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False, primary_key=True)

    actividad = relationship("Actividad", back_populates="fotos")

class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="region", cascade="all, delete")

def create_actividad(comuna, nombre, email, dia_hora_inicio, temas, glosa_otro, foto_filenames, descripcion=None, dia_hora_termino=None, celular=None, sector=None):
    session = SessionLocal()
    actividad = Actividad(
        comuna_id=comuna,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion,
    )

    session.add(actividad)
    actividad.temas = []
    for tema in temas:
        if tema == 'otro':
            new_tema = ActividadTema(tema=tema, glosa_otro=glosa_otro)
        else:
            new_tema = ActividadTema(tema=tema)

        actividad.temas.append(new_tema)

    actividad.fotos  = []
    for foto_filename in foto_filenames:
        actividad.fotos.append(Foto(ruta_archivo='uploads', nombre_archivo=foto_filename))

    session.commit()
    session.close()

def get_last_actividades(limit):
    session = SessionLocal()
    actividades = session.query(Actividad).order_by(Actividad.id.desc()).limit(limit).all()
    session.close()

    return actividades

def get_all_actividades():
    session = SessionLocal()
    actividades = session.query(Actividad).order_by(Actividad.id.desc()).all()
    session.close()

    return actividades

def get_actividad(id):
    session = SessionLocal()
    actividad = session.query(Actividad).get(id)

    return actividad