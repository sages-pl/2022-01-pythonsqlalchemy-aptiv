
from abc import ABCMeta, abstractproperty


class GEOProperty(metaclass=ABCMeta):
    _fieldname: str

    @abstractproperty
    def MIN(self) -> float:
        pass

    @abstractproperty
    def MAX(self) -> float:
        pass

    def __set_name__(self, owner, attrname):
        self._fieldname = f'__{attrname}'

    def __set__(self, instance, newvalue):
        if self.MIN <= newvalue <= self.MAX:
            setattr(instance, self._fieldname, newvalue)
        else:
            raise ValueError('Out of bounds')

    def __get__(self, instance, *args):
        return getattr(instance, self._fieldname)


class Latitude(GEOProperty):
    MIN: float = -90.0
    MAX: float = +90.0


class Longitude(GEOProperty):
    MIN: float = -180.0
    MAX: float = +180.0


class Elevation(GEOProperty):
    MIN: float = -10994.0
    MAX: float = +8848.0


class GeographicCoordinate:
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()
    __latitude: float
    __longitude: float
    __elevation: float

    def __init__(self, latitude, longitude, elevation):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __str__(self):
        return f'Latitude: {self.latitude}, ' + \
               f'Longitude: {self.longitude}, ' + \
               f'Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()
