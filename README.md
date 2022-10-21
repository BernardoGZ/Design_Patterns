# Design_Patterns
Actividad: Refactorizacion con Design Patterns para Diseño y Arquitectura de Software
- Javier Martínez Olivares A01401017
- Alfredo Jose Welsh Martínez A00825988
- Bernardo Garcia Zermeño A00570682
- Gustavo Adolfo Benitez Leonés A00826760


## Patrones de diseño

- Builder: We used Builder Design Pattern to instanciate Ride objects
- Factory: We used Factory Design Pattern for different types of report generation.

## SOLID, POO o Mental models

- SRP: (ride.py and csv_utils.py) csv_utils should only be responsible for CSV management.
- OCP: (csv_utils.py) In case any other CSV functionalities added, can be added without.
- ISP: (ride.py) Ride dataclass used to depend in CSV functionalities. 
