# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import cities_light

from cities_light.receivers import connect_default_signals
from cities_light.abstract_models import (AbstractCountry, AbstractRegion, AbstractCity)


# Create your models here.
class Country(AbstractCountry):
    pass
connect_default_signals(Country)

class Region(AbstractRegion):
    pass
connect_default_signals(Region)

class City(AbstractCity):
    pass
connect_default_signals(City)