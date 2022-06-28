from time import sleep

from pysphero.core import Sphero


def main():

    mac_address = "DB:B0:D9:EE:6C:06"
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()
        sleep(10)

        #Force front headlight on
        sphero.user_io.set_headlights(255)
        #Headlight in automatic
        sphero.user_io.set_headlights(0)


        for x in range(0x0,0x39, 0x2):
            sphero.user_io.set_taillights(x)
            sleep(0.1)

        sphero.power.enter_soft_sleep()

if __name__ == "__main__":
    main()
