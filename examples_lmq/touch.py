from time import sleep

from pysphero.core import Sphero


def main():

    def callback(value):
        print(value.name)

    mac_address = "DB:B0:D9:EE:6C:06"
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()
        sleep(10)
        
        #enable capa touch
        sphero.user_io.enable_cap_touch(True, callback)
        sleep(30)

        sphero.power.enter_soft_sleep()

if __name__ == "__main__":
    main()
