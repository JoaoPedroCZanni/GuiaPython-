# permite que você faça a transferencia de arquivos pela rede

from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print (ftp.getwelcome())
ftp.quit()