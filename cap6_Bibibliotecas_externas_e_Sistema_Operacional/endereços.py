# API relacionada a localização (mapas)
from pygeocoder import Geocoder

endereco = 'avenida paulista, 1110 sao paulo'

# dentro das aspas ficaria a credencial dada pela API

resultado = Geocoder('').geocode(endereco).estado # -->  dará a localização completa de onde fica o lugar

# resultado = Geocoder('').reverse_geocode() # --> dentro dos parentes ficará as cordenadas e o sistema dará a localização

print(resultado)