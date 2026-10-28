# =============================================================================
# Copyright (c) 2026 N. Mousavi
# All rights reserved.
#
# Project:
#     GeoTherm
#
# Description:
#     Calculation of subsurface temperatures at depths of 100–600 m using
#     surface temperature and geothermal gradient (TG).
#
# Input:
#     IHFC_with_surface_temperature.csv
#
# Output:
#     IHCF_subsurface_temperature.csv
#
# Temperature model:
#     T(z) = ST + TG × z
#     TG: °C/km; z: km
#
# =============================================================================

print()
print("╭────────────────────────────────────────────────────────────────────╮")
print("│                              GeoTherm                              │")
print("│              Geothermal Gradient-Based Calculation                 │")
print("│                                                                    │")
print("│                    Copyright © 2026 N. Mousavi                     │")
print("│       For license and citation information, see README.md.         │")
print("╰────────────────────────────────────────────────────────────────────╯")
print()

import pandas as pd
from pathlib import Path

# ============================================================
# SETTINGS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "IHFC_with_surface_temperature.csv"
OUTPUT_FILE = BASE_DIR / "IHCF_subsurface_temperature.csv"

# ============================================================
# READ DATA
# ============================================================

df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip().str.replace("\ufeff", "", regex=False)

# ============================================================
# PRINT COLUMNS
# ============================================================

print("Input columns:")
print(df.columns.tolist())

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required = ["lon", "lat", "elevation", "TG", "surface_temperature"]

for col in required:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}\nAvailable columns: {df.columns.tolist()}")

# ============================================================
# CONVERT TO NUMERIC
# ============================================================

for col in required:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ============================================================
# CALCULATE SUBSURFACE TEMPERATURE
# ============================================================

# TG = °C/km
# T(z) = ST + TG × z
# where z is in km

for depth in [100, 200, 300, 400, 500, 600]:
    depth_km = depth / 1000.0
    df[f"T{depth}"] = df["surface_temperature"] + df["TG"] * depth_km

# ============================================================
# SELECT OUTPUT
# ============================================================

output = df[["lon", "lat", "TG", "surface_temperature", "T100", "T200", "T300", "T400", "T500", "T600"]].copy()

# ============================================================
# RENAME SURFACE TEMPERATURE
# ============================================================

output = output.rename(columns={"surface_temperature": "ST"})

# ============================================================
# SAVE
# ============================================================

output.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

# ============================================================
# SUMMARY
# ============================================================

print()
print("==============================================")
print("DONE")
print("==============================================")
print(f"Rows: {len(output):,}")
print("Depths: 100, 200, 300, 400, 500, 600 m")
print("TG unit: °C/km")
print()
print(f"Output: {OUTPUT_FILE}")
