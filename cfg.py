import math

##

inputtraj = "/temp/btd1y09/Lammps/Production/Ceramide/CeramideWater/DipoleProfile/NewHeadDipole/cer128_water3840_a_5_9_g_5_0D_50_deg_create_extend/dump.trj"

### Output data files

outputScd  = "cerScd.dat"
outputmScd = "cermScd.dat"
output2Sxx = "cer2Sxx.dat"
outputSzz  = "cerSzz.dat"

### Start and end atoms
### Remember atoms n-1 and n+1 will be pulled in

bilayernormal = [0, 0, 1]
start = 10 
end = 13 



startframe = 16000000
endframe = 17000000

startframe2 = 17000000
endframe2 = 18000000


 
### Data Formats

ROWDATA  = 7 ## This is the number of lumps of data we take from LAMMPS data file
ROWBOND  = 4 ## Bond data from the LAMMPS data file
ROWANGLE = 5 ## Angle data from the LAMMPS data file
