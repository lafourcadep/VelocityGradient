# VelocityGradient


## Description
  
Computes the velocity gradient tensor per atom from neighbors velocities and positions.
    
## Parameters 

| GUI name                        | Python name       | Description                                                      | Default Value |
|---------------------------------|-------------------|------------------------------------------------------------------|---------------|
| **Cutoff radius**               | `cutoff`          | Cutoff radius for fetching neighbors positions and velocities    | `4.0`         |


## GUI Screenshot

![Example Screenshot](examples/strain_rate_demo.png)
  
## Installation

- OVITO Pro [integrated Python interpreter](https://docs.ovito.org/python/introduction/installation.html#ovito-pro-integrated-interpreter):
  ```
  ovitos -m pip install --user git+https://github.com/lafourcadep/VelocityGradient.git
  ``` 
  The `--user` option is recommended and [installs the package in the user's site directory](https://pip.pypa.io/en/stable/user_guide/#user-installs).

- Other Python interpreters or Conda environments:
  ```
  pip install git+https://github.com/lafourcadep/VelocityGradient.git
  ```

## Technical information / dependencies

- Tested on OVITO version 3.14.0

## Contact

Paul Lafourcade paul.lafourcade@cea.fr
