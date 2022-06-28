from time import sleep

from pysphero.core import Sphero


def main():
    mac_address = "DB:B0:D9:EE:6C:06"
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()
        sleep(2)
        sphero.power.enter_soft_sleep()


if __name__ == "__main__":
    main()
