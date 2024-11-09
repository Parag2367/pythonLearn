# Modules

import define  # one way of referring module

x = define.circle(5)
print(x)

define.rectangle(23, 34)


# another way
from define import rectangle, square

from define import *

square(5)

# most preferred way is first one
