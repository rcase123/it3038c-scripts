
#This script will display the amount of free space on your drive C:

import shutil

#shutil is the library that we can import that has the ability to see the drive sizes

Total, Used, Free=shutil.disk_usage("/")

#The slash is displayed as a C drive.
#Total, Used, and Free are the variables I used to store the information about the drives.
#It requires 3.


FREESPACE = Free/2**30
#I took the data from from freespace and divided by the power specifically to get GB size as the tutorial explained. 

print("The Total Amount of Free Space on Drive C:")

# Simple explanation of what is being printed

print(FREESPACE , "GB's")

#Printing the variable with the aditional GB string to explain the measurement.