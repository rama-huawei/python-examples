import logging

a = 10
b = 20

logging.basicConfig(level=logging.DEBUG)
logging.debug("{} + {} = {}".format(a, b, a+b))