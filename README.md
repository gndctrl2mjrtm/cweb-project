![alt text](./docs/source/images/logo_color.png?raw=true "Icon")

# ClusterWeb: Distributed System Python API

ClusterWeb is a Python library for creating compute clusters out of any devices that use SSH. 

#### Documentation: https://cweb-project.readthedocs.io/en/latest/

### Compatiable Devices

- CPUs nodes
- Desktops 
- GPUs workstations
- Laptops
- Raspberry Pi
- Android phones


### Requirements

- Python 3.6 or above
- SSH
- Linux or OSX
- pickle
- cloudpickle (host machine)


### Basic Usage:

```python
from clusterweb.pbs.qsub import Qsub
import time

def job(arg):
  a,b = 0,1
  for _ in range(int(arg)):
     a,b = b,a+b
  return a 

q = Qsub(job,1e5)
q.push()
q.pull(thread=False)

print(q.result)
```
