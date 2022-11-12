import logging
from montoenletra.functions import numeroaletra

#logging.basicConfig(level = logging.DEBUG) # en desarrollo
#logging.basicConfig(level = logging.WARNING) # en produccion
logging.basicConfig(level = logging.INFO) # en produccion

def main():
    logging.info(numeroaletra(92514072))

if __name__ == "__main__":
    #print("SON "+numeroaletra(92514072)+" DE PESOS M/L.")
    #logging.debug(numeroaletra.__doc__)
    #logging.debug(help(numeroaletra))

    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    main()
    logging.debug('>>> Estamos finalizando la ejecución del paquete.')