# =============================================================================
# Copyright (c) 2026 N. Mousavi
# All rights reserved.
#
# Project:
#     GeoTherm
#
# Description:
#     Global visualization of subsurface temperatures at a user-defined depth
#     using geographic coordinates and geothermal temperature data.
#
# Input:
#     IHCF_subsurface_temperature.csv
#
# Output:
#     subsurface_temperature_<DEPTH>m.png
#
# Dependencies:
#     pandas, matplotlib, geopandas
#
# =============================================================================

print()
print("╭────────────────────────────────────────────────────────────────────╮")
print("│                              GeoTherm                              │")
print("│             Global Subsurface Temperature Mapping                  │")
print("│                                                                    │")
print("│                    Copyright © 2026 N. Mousavi                     │")
print("│       For license and citation information, see README.md.         │")
print("╰────────────────────────────────────────────────────────────────────╯")
print()

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from pathlib import Path

# ============================================================
# SETTINGS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "IHCF_subsurface_temperature.csv"

# USER DEFINED DEPTH (m)
DEPTH = 600

# Plot limits (°C)
VMIN = 0
VMAX = 80

# ============================================================
# TEMPERATURE COLUMN
# ============================================================

TEMP_COLUMN = f"T{DEPTH}"

# ============================================================
# READ DATA
# ============================================================

df = pd.read_csv(CSV_FILE, encoding="utf-8-sig")

# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip().str.replace("\ufeff", "", regex=False)

print("Columns:")
print(df.columns.tolist())

# ============================================================
# CHECK TEMPERATURE COLUMN
# ============================================================

if TEMP_COLUMN not in df.columns:
    raise ValueError(f"{TEMP_COLUMN} does not exist.\nAvailable columns: {df.columns.tolist()}")

# ============================================================
# CONVERT TO NUMERIC
# ============================================================

df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
df[TEMP_COLUMN] = pd.to_numeric(df[TEMP_COLUMN], errors="coerce")

# ============================================================
# REMOVE INVALID POINTS
# ============================================================

df = df.dropna(subset=["lon", "lat", TEMP_COLUMN])

# ============================================================
# LOAD CONTINENTAL LAND
# ============================================================

WORLD_URL = "https://naturalearth.s3.amazonaws.com/110m_physical/ne_110m_land.zip"
land = gpd.read_file(WORLD_URL)

# ============================================================
# PLOT
# ============================================================

fig, ax = plt.subplots(figsize=(18, 9), dpi=150)

# Continental borders
land.boundary.plot(ax=ax, color="black", linewidth=0.6)

# ============================================================
# TEMPERATURE POINTS
# ============================================================

sc = ax.scatter(
    df["lon"], df["lat"],
    c=df[TEMP_COLUMN],
    cmap="turbo",
    vmin=VMIN,
    vmax=VMAX,
    s=8,
    alpha=0.8,
    edgecolors="none"
)

# ============================================================
# MAP SETTINGS
# ============================================================

ax.set_xlim(-180, 180)
ax.set_ylim(-90, 90)
ax.set_aspect("equal", adjustable="box")
ax.grid(alpha=0.3, linestyle="--")
ax.set_xlabel("Longitude (°)")
ax.set_ylabel("Latitude (°)")
ax.set_title(f"Global Subsurface Temperature at {DEPTH} m")

# ============================================================
# COLORBAR
# ============================================================

cbar = plt.colorbar(sc, ax=ax, shrink=0.75, pad=0.02)
cbar.set_label(f"Temperature at {DEPTH} m (°C)")

# ============================================================
# SAVE
# ============================================================

OUTPUT_FILE = BASE_DIR / f"subsurface_temperature_{DEPTH}m.png"

plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
plt.show()

# ============================================================
# SUMMARY
# ============================================================

print()
print("==============================================")
print("DONE")
print("==============================================")
print(f"Depth plotted : {DEPTH} m")
print(f"Column        : {TEMP_COLUMN}")
print(f"Points        : {len(df):,}")
print(f"Output        : {OUTPUT_FILE}")
print("==============================================")