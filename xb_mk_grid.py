import numpy as np 
import scipy.interpolate 

field_vals = np.genfromtxt('COMB.csv', delimiter=' ') 

x_max, x_min = field_vals[:,0].max(), field_vals[:,0].min() 
y_max, y_min = field_vals[:,1].max(), field_vals[:,1].min() 

x_dist = x_max - x_min 
y_dist = y_max - y_min 

print ('x_dist is : {}, y_dist is : {}'.format(x_dist,y_dist))

res_required_x = 10.0
res_required_y = 10.0

num_of_rows = int(x_dist/res_required_x) 
num_of_cols = int(y_dist/res_required_y) 

print ('num_of_rows : {}, number_of_columns : {}'.format(num_of_rows,num_of_cols))


x_vals = np.linspace(x_min,x_max,num_of_rows) 
y_vals = np.linspace(y_min,y_max,num_of_cols) 


x_new = np.tile(np.array(x_vals), (num_of_cols,1)) 


print(np.shape(x_new)) 
np.savetxt('x_new.csv', x_new) 


y_new = np.empty_like(x_new)

for i in range (0,np.shape(x_new)[0],1):
    y_new[i,:] = y_vals[i]


np.savetxt('y_new.csv', y_new) 


interpolator_mv = scipy.interpolate.NearestNDInterpolator((field_vals[:,0], field_vals[:,1]), field_vals[:,2])


BATHY = []
NE_LAYER = []

for i in range (0,np.shape(x_new)[0],1):
    for j in range (0,np.shape(x_new)[1],1):
        BATH_VAL = interpolator_mv((x_new[i,j],y_new[i,j]))
        BATHY.append(BATH_VAL)
        if BATH_VAL < 0.0 and BATH_VAL > -3:
            NE = 2.0
            NE_LAYER.append(NE)
        else:
            NE = 0.0
            NE_LAYER.append(NE)
        print (x_new[i,j],y_new[i,j], BATH_VAL,NE)


bathy = np.array(BATHY) 
ne_lay = np.array(NE_LAYER) 

bathy = bathy.reshape(np.shape(x_new)[0],np.shape(x_new)[1]) 
ne_lay = ne_lay.reshape(np.shape(x_new)[0],np.shape(x_new)[1]) 


np.savetxt('z_new.csv', bathy) 
np.savetxt('ne_lay.csv', ne_lay) 