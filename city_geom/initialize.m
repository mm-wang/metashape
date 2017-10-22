# =================================================
# Sample UWGv4.2 simulation initialization parameters
# Chris Mackey,2017
# =================================================

# =================================================
# REQUIRED PARAMETERS
# =================================================

# Urban characteristics
bldHeight = 10          # average building height (m)
bldDensity = 0.5        # urban area building plan density (0-1)
verToHor = 0.8          # urban area vertical to horizontal ratio
h_floor = 3.05          # average floor height
h_mix = 1               # fraction of waste heat to canyon
charLength = 1000       # urban area characteristic length (m)
alb_road = 0.2          # road albedo (0 - 1)
maxdx = 250             # Max Dx (m)
d_road = 0.5            # road pavement thickness (m)
sensAnth = 20           # non-building sens heat (W/m^2)
latAnth = 2             # non-building latent heat (W/m^2) (currently not used)

# Vegetatin parameters
vegCover = 0.2          # urban area veg coverage ratio (0-1)
treeCoverage = 0.1      # urban area tree coverage ratio (0-1)
vegStart = 4            # vegetation start month
vegEnd = 10             # vegetation end month
albVeg = 0.25           # Vegetation albedo
latGrss = 0.5           # latent fraction of grass
latTree = 0.5           # latent fraction of tree
rurVegCover = 0.9       # rural vegetation cover

# Traffic schedule [1 to 24 hour]
SchTraffic = [0.2 0.2 0.2 0.2 0.2 0.4 0.7 0.9 0.9 0.6 0.6 0.6 0.6 0.6 0.7 0.8 0.9 0.9 0.8 0.8 0.7 0.3 0.2 0.2     # Weekday
    0.2 0.2 0.2	0.2	0.2	0.3	0.5	0.5 0.5	0.5	0.5	0.5	0.5	0.5	0.6	0.7	0.7	0.7	0.7	0.5	0.4	0.3	0.2	0.2                 # Saturday
    0.2 0.2 0.2	0.2	0.2	0.3	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.4	0.3	0.3	0.2	0.2]                # Sunday

# Fraction of DOE Building types (pre-80's build, post-80's build, new)
# Note that sum(bld) must be equal to 1
bld = [0 0 0        # FullServiceRestaurant
    0 0 0           # Hospital
    0 0 0           # LargeHotel
    0 0.4 0         # LargeOffice
    0 0 0           # MediumOffice
    0 0.6 0         # MidriseApartment
    0 0 0           # OutPatient
    0 0 0           # PrimarySchool
    0 0 0           # QuickServiceRestaurant
    0 0 0           # SecondarySchool
    0 0 0           # SmallHotel
    0 0 0           # SmallOffice
    0 0 0           # Stand-aloneRetail
    0 0 0           # StripMall
    0 0 0           # SuperMarket
    0 0 0]          # Warehouse
# =================================================
# OPTIONAL PARAMETERS FOR SIMULATION CONTROL,
# =================================================

# Main simulation parameters
Month = 1               # starting month (1-12)
Day = 1                 # starting day (1-31)
nDay = 31               # number of days
dtSim = 300             # simulation time step (s)
dtWeather = 3600        # weather time step (s)
autosize = 0            # autosize HVAC (1 or 0)
sensOcc = 100           # Sensible heat from occupant (W)
LatFOcc = 0.3           # Latent heat fraction from occupant (normally 0.3)
RadFOcc = 0.2           # Radiant heat fraction from occupant (normally 0.2)
RadFEquip = 0.5         # Radiant heat fraction from equipment (normally 0.5)
RadFLight = 0.7         # Radiant heat fraction from light (normally 0.7)
writeMAT = 'No'         # Save data to .mat file
writeEPW = 'No'        # Generate EPW format
writeXLS = 'Yes'         # Generate XLSX output (Excel needed)
EPW = 'C:\Sim\UWG4.1\data\MA_BOSTON-LOGAN-IAP_725090_15.epw'    # Rural weather data

# Urban microclimate parameters
h_ubl1 = 1000           # ubl height - day (m)
h_ubl2 = 80             # ubl height - night (m)
h_ref = 150             # inversion height (m)
h_temp = 2              # temperature height (m)
h_wind = 10             # wind height (m)
c_circ = 1.2            # circulation coefficient (default = 1.2 per Bruno (2012))
c_exch = 1.0            # exchange coefficient (default = 1  ref Bruno (2014))
maxDay = 150            # max day threshhold (W/m^2)
maxNight = 20           # max night threshhold (W/m^2)
windMin = 1.0           # min wind speed (m/s)
h_obs = 0.1             # rural average obstacle height (m)
