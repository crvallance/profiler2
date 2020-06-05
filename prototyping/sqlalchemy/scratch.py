from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, null
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.sql import expression
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    client_mac = Column(String, nullable=False, unique=True)
    oui = Column(String, nullable=False)
    oui_manuf = Column(String)
    friendly_name = Column(String)

    def __repr__(self):
        return f"<Device(client_mac='{self.client_mac}', oui='{self.oui}', oui_manuf='{self.oui_manuf}', friendly_name='{self.friendly_name}')>"


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, ForeignKey("devices.id"), nullable=False, primary_key=True)
    client_mac = Column(String, nullable=False, unique=True)
    db_version = Column(String, nullable=False)
    timestamp = Column(DateTime)
    spatial_streams = Column(Integer)
    band = Column(Integer)
    dot11n = Column(String)
    dot11ac = Column(String)
    dot11ax = Column(String)
    dot11k = Column(String)
    dot11r = Column(String)
    dot11v = Column(String)
    dot11w = Column(String)
    power = Column(String)
    supported_channels = Column(String)

    def __repr__(self):
        return f"<Profile(client_mac='{self.client_mac}', db_version='{self.db_version}', timestamp='{self.timestamp}', spatial_streams='{self.spatial_streams}', band='{self.band}', dot11n='{self.dot11n}', dot11ac='{self.dot11ac}', dot11ax='{self.dot11ax}', dot11k='{dot11k}', dot11r='{self.dot11r}', dot11v='{self.dot11v}', dot11w='{dot11w}', power='{self.power}', supported_channels='{self.supported_channels}')>"

Base.metadata.create_all(engine)

new_device = Device(id="1", client_mac="11:22:33:44:55:66", oui="11:22:33", oui_manuf="NA", friendly_name="TEST")
new_profile = Profile(id="1", client_mac="11:22:33:44:55:66", db_version="0.1", timestamp=datetime.datetime.now(), spatial_streams=2, band=5, dot11n="True", dot11ac="True", dot11ax="True", dot11k="True", dot11v="True", dot11r="True", dot11w="Sure", power="1million", supported_channels="all_of_them")

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

print("\n# add new device")
session.add(new_device)
print(session.commit())
print("# finish add new device\n")


print("\n# add new profile")
session.add(new_profile)
print(session.commit())
print("# finish add new profile\n")

print(f"session.dirty: {session.dirty}")
print(f"session.new: {session.new}")
print("\n# query for our device")
our_device = session.query(Device).filter_by(oui='11:22:33').first() 
print("# finish query for our device") 
print("# our device:")
print(our_device)
print()

print("modify our device")
our_device.oui_manuf="SOMETHING"
print("finish modifying our device")

print(f"session.dirty: {session.dirty}")
print(f"session.new: {session.new}")
print()
print(session.commit())