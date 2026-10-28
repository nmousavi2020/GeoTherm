

\# GeoTherm



GeoTherm is a Python-based project for calculating and visualizing global subsurface temperatures using surface temperature data and geothermal gradients.



\## Features



\- Calculates temperatures at depths of 100–600 m.

\- Generates global subsurface temperature maps.

\- Exports results to CSV and PNG files.

\- Supports user-defined plotting depths and temperature limits.



\## Temperature Model



`T(z) = ST + TG × z`



Where:



\- `T(z)`: Subsurface temperature (°C)

\- `ST`: Surface temperature (°C)

\- `TG`: Geothermal gradient (°C/km)

\- `z`: Depth (km)



\## Input Data



\- `IHFC\_with\_surface\_temperature.csv`



Required columns:



\- `lon`

\- `lat`

\- `elevation`

\- `TG`

\- `surface\_temperature`



\## Output Files



\- `IHCF\_subsurface\_temperature.csv`

\- `subsurface\_temperature\_<DEPTH>m.png`



\## Requirements



\- Python 3.10+

\- pandas

\- matplotlib

\- geopandas



\## Installation



```bash

git clone https://github.com/YOUR\_USERNAME/GeoTherm.git

cd GeoTherm

pip install -r requirements.txt

```



\## Usage



\### Calculate Subsurface Temperatures



```bash

python subsurface\_temperature.py

```



\### Generate a Global Temperature Map



```bash

python plot\_subsurface\_temperature.py

```



\## Customize the Plot



Edit these settings in the plotting script:



```python

DEPTH = 600

VMIN = 0

VMAX = 80

```



\## Project Structure



```text

GeoTherm/

├── subsurface\_temperature.py

├── plot\_subsurface\_temperature.py

├── requirements.txt

├── README.md

├── LICENSE

└── .gitignore

```



\## Author



N. Mousavi



\## Acknowledgments



Global land boundaries are obtained from Natural Earth.



\## License



This project is licensed under the MIT License. See \[LICENSE](LICENSE) for details.



\## Citation



If you use GeoTherm in your research, please acknowledge the project and its author.



