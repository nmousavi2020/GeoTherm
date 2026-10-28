
# GeoTherm

## Copyright (c) 2026 N. Mousavi. All rights reserved.

GeoTherm is a Python-based project for calculating and visualizing global subsurface temperatures using surface temperature data and geothermal gradients.

## Citation

If you use GeoTherm or its datasets in your research, please cite:

Mousavi, N. (2026). GeoTherm: A Package for Global Subsurface Thermal Calculations (0–600 m) for Geothermal Engineering Applications (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23735491

## Features

- Calculates temperatures at depths of 100–600 m.
- Generates global subsurface temperature maps.
- Exports results to CSV and PNG files.
- Supports user-defined plotting depths and temperature limits.

## Temperature Model

T(z) = ST + TG × z

Where:
- T(z): Subsurface temperature (°C)
- ST: Surface temperature (°C)
- TG: Geothermal gradient (°C/km)
- z: Depth (km)

## Input Data

- IHFC_with_surface_temperature.csv

Required columns:
- lon
- lat
- elevation
- TG
- surface_temperature

## Output Files

- IHCF_subsurface_temperature.csv
- subsurface_temperature_<DEPTH>m.png

## Requirements

- Python 3.10+
- pandas
- matplotlib
- geopandas

## Installation

```bash
git clone https://github.com/nmousavi2020/GeoTherm.git
cd GeoTherm
pip install -r requirements.txt
```

## Usage

### Calculate Subsurface Temperatures

```bash
python forward.py
```

### Generate a Global Temperature Map

```bash
python plotSubtemp.py
```

## Customize the Plot

```python
DEPTH = 600
VMIN = 0
VMAX = 80
```

## Project Structure

```text
GeoTherm/
├── subsurface_temperature.py
├── plot_subsurface_temperature.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Author

N. Mousavi

## Acknowledgments

Global land boundaries are obtained from Natural Earth.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use GeoTherm in your research, please acknowledge the project and its author.
