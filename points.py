import numpy as np
import pandas as pd
image_file = 'lroc_color_poles_4k.tif'
data = pd.read_csv('Craters.csv')

name = []
latitude = []
longitude = []
diameter = []

with open('craters.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        nam  = line[:17]
        lat  = line[18:24]
        long = line[24:31]
        diam = line[31:36]
        name.append(nam.strip())
        lat2 = lat.strip()
        long2= long.strip()
        for i in range(len(lat2)):
            if i == len(lat2) - 1:
                if lat2[i] == 'N':
                    latitude.append(np.pi/2 - np.deg2rad(float(lat2[:-1])))
                else:
                    latitude.append(np.pi/2 + np.deg2rad(float(lat2[:-1])))
        for i in range(len(long2)):
            if i == len(long2) - 1:
                if long2[i] == 'E':
                    longitude.append(np.deg2rad(float(long2[:-1])))
                else:
                    longitude.append(2 * np.pi - np.deg2rad(float(long2[:-1])))
        diameter.append(int(diam.strip()))

df = pd.DataFrame({'latitude': latitude, 'longitude': longitude, 'diameter': diameter},
                  index=name)
dfs = df.sort_values('diameter')
phi_ = dfs['longitude'].tolist()
theta_ = dfs['latitude'].tolist()
size = dfs['diameter'].tolist()
size.reverse()
phi_.reverse()
theta_.reverse()

data_x = []
data_y = []
data_z = []
size_ = []

#Number of points
nr = 100

for i in range(nr):
    data_x.append(np.sin(theta_[i])*np.cos(phi_[i]))
    data_y.append(np.sin(theta_[i])*np.sin(phi_[i]))
    data_z.append(np.cos(theta_[i]))
    size_.append(size[i])

with open('data_x', 'w') as f1:
    for i in range(len(data_x)):
        f1.write(str(data_x[i]) + '\n')

with open('data_y', 'w') as f2:
    for i in range(len(data_y)):
        f2.write(str(data_y[i]) + '\n')

with open('data_z', 'w') as f3:
    for i in range(len(data_z)):
        f3.write(str(data_z[i]) + '\n')

with open('size', 'w') as f4:
    for i in range(len(size_)):
        f4.write(str(size_[i]) + '\n')
