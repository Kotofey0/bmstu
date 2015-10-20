import subprocess
from subprocess import *


ls = check_output(['ls', '-la', '/'])

print ls