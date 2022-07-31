# Read in the file
with open('1.txt', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('OVR', 'WRP')
filedata = filedata.replace('Outfit', 'PTW')
filedata = filedata.replace('outfit', 'PTW')
filedata = filedata.replace('OVKV', 'HVAC')
filedata = filedata.replace('those', '')
filedata = filedata.replace('IAD', 'WRP')


# Write the file out again
with open('2.txt', 'w') as file:
    file.write(filedata)