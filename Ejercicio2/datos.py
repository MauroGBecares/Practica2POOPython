from pais import Pais
from localidad import Localidad
from provincia import Provincia

rosario = Localidad("Rosario", 254, 2000)
buenos_aires = Localidad("Buenos Aires", 549, 6444)
cordoba = Localidad("Cordoba", 547, 5477)
los_angeles = Localidad("Los Angeles", 668, 4222)
san_diego = Localidad("Sant Diego", 222, 6442)

california = Provincia("California", 5477)
santa_fe = Provincia("Santa Fe", 5426)
prov_cordoba = Provincia("Cordoba", 5412)
prov_bsar = Provincia("Buenos Aires", 1123)

argentina = Pais("Argentina", 3333)
eeuu = Pais("Estados Unidos", 4578)

argentina.add_provincia(santa_fe)
argentina.add_provincia(prov_cordoba)
argentina.add_provincia(prov_bsar)
eeuu.add_provincia(california)

california.add_localidad(los_angeles)
california.add_localidad(san_diego)
santa_fe.add_localidad(rosario)
prov_bsar.add_localidad(buenos_aires)
prov_cordoba.add_localidad(cordoba)

localidades = [rosario, buenos_aires, cordoba, los_angeles, san_diego]
paises = [argentina, eeuu]
provincias = [santa_fe, prov_cordoba, prov_bsar, california]