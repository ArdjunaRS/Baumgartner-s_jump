
import matplotlib.pyplot as plt
import numpy as np


###################################### INPUT FUNCTIONS

def asking_y0val():
    myinput_y0val= float(input("Enter the height of jumping (m): "))
    while myinput_y0val != float():
        if float(myinput_y0val)<0:
            myinput_y0val= input("Input a positive number: ")
        elif float(myinput_y0val)>=0:
            break
    y0val=float(myinput_y0val)
    print("you have chosen height = ",myinput_y0val," m")
    return y0val



def asking_x():
    asking_x_range= input("[Plotted height limits} \nWould you like to: \n(a) Plot the entire fall \n(b) Plot only a section of the fall \nChoice: ")
    while asking_x_range != "a" or asking_x_range != "b" or asking_x_range != "c":
        if asking_x_range == "a":
            xplot_lower=y0val
            xplot_upper=0
            break
        elif asking_x_range == "b":
            myinput_x_lower= input("Please enter the first height limit(m): ")
            myinput_x_upper= input("Please enter the second height limit (m): ")
            xplot_lower=float(myinput_x_lower)
            xplot_upper= float(myinput_x_upper)
            break

        else:
            asking_x_range= input("Please enter an option (a or b): ")
    return xplot_lower, xplot_upper


def asking_t():
    asking_t_range= input("[Plotted time limits] \nWould you like to: \n(a) Plot the entire fall \n(b) Plot only a section of the fall \nChoice: ")
    while asking_t_range != "a" or asking_t_range != "b" or asking_t_range != "c":
        if asking_t_range == "a":
            tplot_lower=0
            tplot_upper=60
            break
        elif asking_t_range == "b":
            myinput_t_lower= input("Please enter the first height limit(m): ")
            myinput_t_upper= input("Please enter the second height limit (m): ")
            tplot_lower=float(myinput_t_lower)
            tplot_upper= float(myinput_t_upper)
            break
        else:
            asking_t_range= input("Please enter an option (a or b): ")
    return tplot_lower, tplot_upper

def asking_dt():
    dt= input("Please input the time step size (s): ")
    delta_t=float(dt)
    return delta_t

def asking_euler():
    asking_euler= input("Would you like to: \n(a) Ignore the modified euler correction \n(b) Include a comparison with the modified euler method \nChoice: ")
    while asking_euler != "a" or asking_euler != "b" or asking_euler != "c":
        if asking_euler == "a":
            euler_t=0
            euler_y=0
            euler_v=0
            
            break
        elif asking_euler == "b":
            euler_t=velocity_modified_euler(v_n, delta_t, g, m, Cd)[2]
            euler_y=velocity_modified_euler(v_n, delta_t, g, m, Cd)[0]
            euler_v=velocity_modified_euler(v_n, delta_t, g, m, Cd)[1]
            break

        else:
            asking_euler= input("Please enter an option (a or b): ")
    return euler_t, euler_y, euler_v





###################### for part a (euler)

def velocity(v_n, delta_t, g, m, Cd):
    
    rho=1.2
    k = (Cd*rho*0.7)/2
    y0=y0val
    t0=t0val
    
    
    v_values=[]
    y_values=[]
    t_values=[]
    tmax=500
    while t0<= tmax:
        v_values.append(v_n)
        y_values.append(y0)
        t_values.append(t0)  
        v_n= v_n - delta_t*( g+ ((k/m)*abs(v_n)*v_n))
        y0=y0+ delta_t * v_n
        t0=t0+delta_t

         
    return y_values, v_values, t_values


###################### for part B
    #analytical y values
def y_cosh(m, t, g): 
    y0=y0val
    t=t0val
    tmax=500
    rho=1.2
    k = (0.47*rho*0.7)/2
    yvals=[]
    tvals=[]

    while t<= tmax:
        

        tvals.append(t)
        
        y = y0 - ((m/(2*k))*(np.log((np.cosh(t* np.sqrt(k*g/m)))**2))) 
        t = t + delta_t
        yvals.append(y)

########################## 
    return yvals, tvals



def v_tanh(m, g, t):
    y0=y0val
    rho=1.2
    k = (0.47*rho*0.7)/2
    tmax=500

    vvals=[]
    tvals= []
    t=t0val
    while t <= tmax:
        v= -1*np.sqrt(m*g/k) * (np.tanh(t* np.sqrt(k*g/m)))
        vvals.append(v)
        tvals.append(t)
        t = t + delta_t

    return vvals, tvals



##################### modified euler
def velocity_modified_euler(v_n, delta_t, g, m, Cd):
    
    rho=1.2
    k = (Cd*rho*0.7)/2
    y0=y0val
    t0=t0val
    v_values=[]
    y_values=[]
    t_values=[]
    tmax=500
    while t0 <= tmax:
        
        y_values.append(y0)
        t_values.append(t0) 
        v_values.append(v_n)
        
        v_mid= float(v_n - (delta_t/2)*( g+ (k/m)*float(abs(v_n))*v_n))
        v_n= float(v_mid - (delta_t)*( g+ (k/m)*float(abs(v_mid))*v_mid))
        

        

        t0=t0+(delta_t)
        y0=y0+ (delta_t) * v_n
        

        
        
    return y_values, v_values, t_values

############# with chaging density- Baumgartner
def velocity_real(v_n, delta_t, g, m, y0):
    
    t0=t0val
    v_values=[]
    y_values=[]
    t_values=[]
    tmax=500
    parachute_h=2500
        

    while t0 <= tmax:
        if y0>parachute_h: 
            A=0.7
        else:
            A=30

        rho=1.2* np.exp(-y0/h)
        k = (1.12*rho*A)/2       
        v_nplus1= float(v_n - delta_t*( g+ (k/m)*float(abs(v_n))*v_n))
        v_values.append(v_nplus1)
        v_n=v_nplus1
        
        y_values.append(y0)
        t_values.append(t0)  
        
        t0=t0+delta_t
        y0=y0+ delta_t * v_n
   
    return y_values, v_values, t_values



def velocity_real1(v_n, delta_t, g, m, y0):
    t0=t0val
    v_values=[]
    y_values=[]
    t_values=[]
    tmax=500
    parachute_h=2500
        

    while t0 <= tmax: #to add conditions of opening the parachute
        if y0>parachute_h: 
            A=0.7
        else:
            A=30

        rho=1.2
        k = (1.12*rho*A)/2       
        v_nplus1= float(v_n - delta_t*( g+ (k/m)*float(abs(v_n))*v_n))
        v_values.append(v_nplus1)
        v_n=v_nplus1
        
        y_values.append(y0)
        t_values.append(t0)  
        
        t0=t0+delta_t
        y0=y0+ delta_t * v_n
   
    return y_values, v_values, t_values

MyInput = '0'
while MyInput != 'q':
    MyInput = input("Please enter a choice: \n  \n(a) To plot velocity against height from the ground using Euler analysis (with option of modified Euler correction) \n \n(b) To compare part a to theoretical predictions  \n \n(c) To examine the results of the graphs with varying the step size (with option of modified Euler correction) \n  \n(d) To examine results by varying the ratio k/m \n  \n(e) To plot Baumgartner's original jump with changing air density (with an option to compare the mass of the jumper) \n  \n(f) To plot Baumgartner's original jump with changing air density (with an option to compare jumping heights) \n \n(q) Quit \n \nChoice:  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print('You entered the choice: ',MyInput)


########################################## PART A ##########################################
    if MyInput == 'a':
        print("The time step is set to 0.1 seconds.")
        print("g is set to 9.81 m/s^2")
        print("The default jumping height is 1 km.")
        
        Cd=0.47
        delta_t=0.1
        y0val=asking_y0val()
        t0val=0
        v_n=0
        v_nplus1=0

        g=9.81
        m= 75
        y_ending=0 #USED TO DETERMINE THE RANGE ON THE X AXIS OF THE GRAPH
        
        
        ta,tb= asking_t()
        aa,ab= asking_x()
        
        euler_t, euler_y, euler_v= asking_euler()
        
        
        plt.plot(velocity(v_n, delta_t, g, m, Cd)[0], velocity(v_n, delta_t, g, m, Cd)[1], label=("Euler"))
        plt.plot(euler_y, euler_v, label= ("Modified Euler"))
        
        
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.xlim(aa+10,ab)
        plt.legend()
        plt.show()


        plt.plot(velocity(v_n, delta_t, g, m, Cd)[2], velocity(v_n, delta_t, g, m, Cd)[0], label=("Euler"))
        plt.plot(euler_t, euler_y, label= ("Modified Euler"))
        
        plt.gca().invert_yaxis()
        plt.xlabel("Time")
        plt.ylabel("Height")
        plt.ylim(0,y0val+10)
        plt.xlim(ta,tb)  
        plt.legend()
        plt.show()        
        
        
        plt.plot(velocity(v_n, delta_t, g, m, Cd)[2], velocity(v_n, delta_t, g, m, Cd)[1], label=("Euler"))
        plt.plot(euler_t, euler_v, label= ("Modified Euler"))
        plt.gca().invert_yaxis()
        plt.xlabel("Time")
        plt.ylabel("Velocity (m/s)")
        plt.xlim(ta,tb)  
        plt.legend()
        plt.show() 
        
        print("\n \nTo change the x axis coordinate range, please select ", MyInput, " again and chose to 'plot only a section of the fall'")
####################################################################################################################################################################################################################################################################  
        
    if MyInput == 'b':
        print("The time step was set to 0.1 seconds.")
        print("g was set to 9.81 m/s^2")
        print("The default jumping height was 1 km.")
        Cd=0.47
        delta_t=asking_dt()
        y0val=asking_y0val() #the height at which the jumper jumps from
        t0val=0
        g=9.81
        m=75
        t=0
        t_measure=200  #indicates when the height measurement is taken (in seconds)
        v_n=0
        # the next line is to set the limits of the x axis.
        aa,ab=asking_x()
        ta,tb=asking_t()
        
        # HERE IS THE PLOT OF THE ANALYTICAL PREDICTION WITH COSH AND TANH
        #velocity against height
        plt.plot(y_cosh( m, t, g)[0],v_tanh(m, g, t)[0], label="Theoretical prediction")
        plt.plot(velocity(v_n, delta_t, g, m, Cd)[0], velocity(v_n, delta_t, g, m, Cd)[1], label="Euler")  
        plt.plot(velocity(v_n, 0.1, g, m, Cd)[0], velocity(v_n, 0.1, g, m, Cd)[1], label="Euler, step size= 0.1")  
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.legend()
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.xlim(aa,ab)
        plt.show() 
        
        #velocity against time
        plt.plot(y_cosh( m, t, g)[1],v_tanh(m, g, t)[0], label="Theoretical prediction")
        plt.plot(velocity(v_n, delta_t, g, m, Cd)[2], velocity(v_n, delta_t, g, m, Cd)[1], label=("Euler"))
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.legend()
        plt.gca().invert_yaxis()
        plt.xlim(ta,tb)
        plt.show() 
        
        #distance against time
        plt.plot(y_cosh( m, t, g)[1],y_cosh( m, t, g)[0], label="Theoretical prediction")
        plt.plot(velocity(v_n, delta_t, g, m, Cd)[2], velocity(v_n, delta_t, g, m, Cd)[0], label=("Euler")) 
        plt.xlabel("Time (m)")
        plt.ylabel("Height (m)")  
        plt.legend()
        plt.xlim(ta,tb+30)
        plt.ylim(0, y0val+10)
        plt.show()         

        print("To change the x axis coordinate range, please select ", MyInput, " again and chose to 'plot only a section of the fall")
####################################################################################################################################################################################################################################################################          
    if MyInput == 'c':

        print("the default step size is 0.1 seconds.")
        
        y0val=asking_y0val() #the height at which the jumper jumps from
        t0val=0
        g=9.81
        m=75
        t=0
        dt=0.005
        t_measure=15  #indicates when the height measurement is taken (in seconds)
        y_ending=0
        v_n=0
        Cd=0.47

        
        myinput_deltat_1= input("enter your first time step size: ")
        myinput_deltat_2= input("enter your second time step size: ")        
        myinput_deltat_3= input("enter your third time step size: ")    \
        
        delta_t_1= float(myinput_deltat_1)
        delta_t_2= float(myinput_deltat_2)
        delta_t_3= float(myinput_deltat_3)
        
        
        
        plt.plot(velocity(v_n, delta_t_1, g, m, Cd)[0], velocity(v_n, delta_t_1, g, m, Cd)[1], label= (delta_t_1,"Euler",  " seconds"))
        plt.plot(velocity_modified_euler(v_n, delta_t_1, g, m, Cd)[0], velocity(v_n, delta_t_1, g, m, Cd)[1], label= ("modified euler, ",delta_t_1, " seconds"))
        
        plt.plot(velocity(v_n, delta_t_2, g, m, Cd)[0], velocity(v_n, delta_t_2, g, m, Cd)[1], label= (delta_t_2,"Euler", " seconds")) 
        plt.plot(velocity_modified_euler(v_n, delta_t_2, g, m, Cd)[0], velocity(v_n, delta_t_2, g, m, Cd)[1], label= ("modified euler, ",delta_t_2, " seconds"))
        
        plt.plot(velocity(v_n, delta_t_3, g, m, Cd)[0], velocity(v_n, delta_t_3, g, m, Cd)[1], label= (delta_t_3,"Euler", " seconds")) 
        plt.plot(velocity_modified_euler(v_n, delta_t_2, g, m, Cd)[0], velocity(v_n, delta_t_2, g, m, Cd)[1], label= ("modified euler, ",delta_t_3, " seconds"))
        
        print(len(velocity(v_n, delta_t_1, g, m, Cd)[0]))
        print(len(velocity(v_n, delta_t_1, g, m, Cd)[1]))
        print(len(velocity(v_n, delta_t_2, g, m, Cd)[0]))
        print(len(velocity(v_n, delta_t_2, g, m, Cd)[1]))
        print(len(velocity(v_n, delta_t_3, g, m, Cd)[0]))
        print(len(velocity(v_n, delta_t_3, g, m, Cd)[1]))
        
        aa,ab=asking_x()
        
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.legend(loc='bottom right')
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.xlim(aa,ab)
        plt.show()  
        
        print("To change the x axis coordinate range, please select ", MyInput, " again and chose to 'plot only a section of the fall")


####################################################################################################################################################################################################################################################################      
    if MyInput == 'd':
        print("You have chosen to observe the changes to the graph by varying the jumper's weight and thus the ratio of k/m.")
       #here do the ratio of k/m is varied, original ratio was 0.00644
       
        print("hi")
        delta_t=0.1
        v_n=0
        v_nplus1=0
        g=9.81
        m= 75
        y_ending=0
        y0val=1000
        t0val=0
        k=(1.15*1.2*0.7)/2
        Cd=0.47
        t=0
        

        
        
        myinput_m_1= input("enter your first mass value: ")
        myinput_m_2= input("enter your second mass value: ")        
        myinput_m_3= input("enter your third mass value: ")
        
        m_1= float(myinput_m_1)
        m_2= float(myinput_m_2)
        m_3= float(myinput_m_3)  
        
        ratio1= k/m_1
        ratio2= k/m_2
        ratio3= k/m_3 
        
        aa,ab=asking_x()

        
        plt.plot(velocity(v_n, delta_t, g, m_1, Cd)[0], velocity(v_n, delta_t, g, m_1, Cd)[1], label = ("mass: ", m_1,"kg, ", "ratio: ",round(ratio1,5)))
        plt.plot(velocity(v_n, delta_t, g, m_2, Cd)[0], velocity(v_n, delta_t, g, m_2, Cd)[1], label = ("mass: ", m_2,"kg, ","ratio: ",round(ratio2,5)))
        plt.plot(velocity(v_n, delta_t, g, m_3, Cd)[0], velocity(v_n, delta_t, g, m_3, Cd)[1], label = ("mass: ", m_3,"kg, ","ratio: ",round(ratio3,5)))       
        
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.legend(loc='bottom right')
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.xlim(aa,ab)
        plt.show()  
        
        print("To change the x axis coordinate range, please select ", MyInput, " again and chose to 'plot only a section of the fall")
     
####################################################################################################################################################################################################################################################################          
    if MyInput == 'e':  
       #write down the definition of the euler method, then put input stuff for graphs to be plotted with different colours.
       # also allow for the moving of the range on the x graph.
       
       #here you are comparing the modified euler method with normal method from part a. introduce different time steps.

        
                
        y0val=39045
        delta_t=0.1
        t0val=0
        v_n=0
        v_nplus1=0
        h=7640
        g=9.81
        tmax=500
        
        y_ending=0 #USED TO DETERMINE THE RANGE ON THE X AXIS OF THE GRAPH
        '''
        g=9.81*(6400000/6400000+y0)
        '''
        myinput_asking_mass= input("Would you like to simulate the jump of different masses? \n \n(a) No, keep it at 90kg \n \n(b) Yes \n \nChoice: ")
        while myinput_asking_mass != "a" or myinput_asking_mass != "b" :
            if myinput_asking_mass == "a":
                m=90
                m1=90
                m2=90
                m3=90
                
                t1=velocity_real(v_n, delta_t, g, m, y0val)[2]
                t2=0
                t3=0
                t4=0
                v1=velocity_real(v_n, delta_t, g, m, y0val)[1]
                v2=0
                v3=0
                v4=0      
                y1=velocity_real(v_n, delta_t, g, m, y0val)[0]
                y2=0
                y3=0
                y4=0                   
                
                break
            elif myinput_asking_mass == "b":
        
                myinput_asking_mass_1= input("Please enter the first mass(kg): ")
                myinput_asking_mass_2= input("Please enter the second mass(kg): ")
                myinput_asking_mass_3= input("Please enter the third mass(kg): ")
                m1=float(myinput_asking_mass_1)
                m2=float(myinput_asking_mass_2)
                m3=float(myinput_asking_mass_3)
                m=90
                
                t1=0
                t2=velocity_real(v_n, delta_t, g, m1, y0val)[2]
                t3=velocity_real(v_n, delta_t, g, m2, y0val)[2]
                t4=velocity_real(v_n, delta_t, g, m3, y0val)[2]
                
                v1=0
                v2=velocity_real(v_n, delta_t, g, m1, y0val)[1]
                v3=velocity_real(v_n, delta_t, g, m2, y0val)[1]
                v4=velocity_real(v_n, delta_t, g, m3, y0val)[1] 
                
                y1=0
                y2=velocity_real(v_n, delta_t, g, m1, y0val)[0]
                y3=velocity_real(v_n, delta_t, g, m2, y0val)[0]
                y4=velocity_real(v_n, delta_t, g, m3, y0val)[0]                
                
                break
        
            else:
                asking_x_range= input("Please enter an option (a or b): ")
        
        
        
        ####### plotting time against velocity
        plt.plot(t1,v1 ,label=("Mass= 90 kg."))
        plt.plot(t2,v2 ,label=("Mass= ", m1, " kg."))
        plt.plot(t3,v3 ,label=("Mass= ", m2, " kg."))
        plt.plot(t4,v4 ,label=("Mass= ", m3, " kg."))
        plt.plot(velocity_real1(v_n, delta_t, g, m, y0val)[2],velocity_real1(v_n, delta_t, g, m, y0val)[1], label= "simulation with constant air density")
        plt.plot([0,500],[-373,-373],label=("maximum speed reached"))
        plt.plot([0,500],[-295,-295],label=("Speed of sound"))
        
        '''
        plt.plot(velocity(v_n, delta_t, g, m)[2], velocity(v_n, delta_t, g, m)[1], label=("Constant density"))
        '''
        plt.legend()
        plt.gca().invert_yaxis()
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity(m/s)")
        plt.xlim(0,tmax)
        plt.ylim(0,-400)
        plt.show()
        
        
        
        
        ###### plotting time against height
        plt.plot(t1,y1 ,label=("Mass= 39045 m."))
        plt.plot(t2,y2 ,label=("Mass= ", m1, " kg."))
        plt.plot(t3,y3 ,label=("Mass= ", m2, " kg."))
        plt.plot(t4,y4 ,label=("Mass= ", m3, " kg."))
        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m))")
        
        plt.show()       
        
        
        
        
        ######plotting velocity against height to compare to the speed of sound
        plt.plot(y1,v1 ,label=("Mass= 39045 m."))
        plt.plot(y2,v2 ,label=("Mass= ", m1, " kg."))
        plt.plot(y3,v3 ,label=("Mass= ", m2, " kg."))
        plt.plot(y4,v4 ,label=("Mass= ", m3, " kg."))
        plt.plot([0,500],[-373,-373],label=("maximum speed reached"))
        plt.plot([0,500],[-295,-295],label=("Speed of sound"))
        plt.legend()
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.gca().invert_yaxis()
        plt.gca().invert_xaxis()
        plt.show()                  
        
            
       
####################################################################################################################################################################################################################################################################         
    if MyInput == 'f':
        

        delta_t=0.1
        t0val=0
        v_n=0
        v_nplus1=0
        h=7640
        g=9.81
        tmax=500
        m= 90
        y_ending=0 #USED TO DETERMINE THE RANGE ON THE X AXIS OF THE GRAPH
        '''
        g=9.81*(6400000/6400000+y0)
        '''
        myinput_asking_height= input("Would you like to simulate a different jumping height? \n \n(a) No, keep it at 39045m \n \n(b) Yes \n \nChoice: ")
        while myinput_asking_height != "a" or myinput_asking_height != "b" :
            if myinput_asking_height == "a":
                y0val=39045
                y0val_1=0
                y0val_2=0
                y0val_3=0
                
                t1=velocity_real(v_n, delta_t, g, m, y0val)[2]
                t2=0
                t3=0
                t4=0
                v1=velocity_real(v_n, delta_t, g, m, y0val)[1]
                v2=0
                v3=0
                v4=0      
                y1=velocity_real(v_n, delta_t, g, m, y0val)[0]
                y2=0
                y3=0
                y4=0                   
                
                break
            elif myinput_asking_height == "b":
        
                myinput_asking_height_1= input("Please enter the first jumping height(m): ")
                myinput_asking_height_2= input("Please enter the second jumping height(m): ")
                myinput_asking_height_3= input("Please enter the third jumping height(m): ")
                y0val_1=float(myinput_asking_height_1)
                y0val_2=float(myinput_asking_height_2)
                y0val_3=float(myinput_asking_height_3)
                y0val=0
                
                t1=0
                t2=velocity_real(v_n, delta_t, g, m, y0val_1)[2]
                t3=velocity_real(v_n, delta_t, g, m, y0val_2)[2]
                t4=velocity_real(v_n, delta_t, g, m, y0val_3)[2]
                
                v1=0
                v2=velocity_real(v_n, delta_t, g, m, y0val_1)[1]
                v3=velocity_real(v_n, delta_t, g, m, y0val_2)[1]
                v4=velocity_real(v_n, delta_t, g, m, y0val_3)[1] 
                
                y1=0
                y2=velocity_real(v_n, delta_t, g, m, y0val_1)[0]
                y3=velocity_real(v_n, delta_t, g, m, y0val_2)[0]
                y4=velocity_real(v_n, delta_t, g, m, y0val_3)[0]                
                
                break
        
            else:
                asking_x_range= input("Please enter an option (a or b): ")
        
        
        

        ####### plotting time against velocity
        plt.plot(t1,v1 ,label=("Height= 39045 m."))
        plt.plot(t2,v2 ,label=("Height= ", y0val_1, " m."))
        plt.plot(t3,v3 ,label=("Height= ", y0val_2, " m."))
        plt.plot(t4,v4 ,label=("Height= ", y0val_3, " m."))
        plt.plot(velocity_real1(v_n, delta_t, g, m, y0val)[2],velocity_real1(v_n, delta_t, g, m, y0val)[1], label= "simulation with constant air density")
        plt.plot([0,500],[-373,-373],label=("maximum speed reached"))
        plt.plot([0,500],[-295,-295],label=("Speed of sound"))
        
        '''
        plt.plot(velocity(v_n, delta_t, g, m)[2], velocity(v_n, delta_t, g, m)[1], label=("Constant density"))
        '''
        plt.legend()
        plt.gca().invert_yaxis()
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity(m/s)")
        plt.xlim(0,tmax)
        plt.ylim(0,-400)
        plt.show()
        
        
        
        
        ###### plotting time against height
        plt.plot(t1,y1 ,label=("Height= 39045 m."))
        plt.plot(t2,y2 ,label=("Height= ", y0val_1, " m."))
        plt.plot(t3,y3 ,label=("Height= ", y0val_2, " m."))
        plt.plot(t4,y4 ,label=("Height= ", y0val_3, " m."))
        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m))")
        
        plt.show()       
        
        
        
        
        ######plotting velocity against height to compare to the speed of sound
        plt.plot(y1,v1 ,label=("Height= 39045 m."))
        plt.plot(y2,v2 ,label=("Height= ", y0val_1, " m."))
        plt.plot(y3,v3 ,label=("Height= ", y0val_2, " m."))
        plt.plot(y4,v4 ,label=("Height= ", y0val_3, " m."))
        plt.plot([0,500],[-373,-373],label=("maximum speed reached"))
        plt.plot([0,500],[-295,-295],label=("Speed of sound"))
        plt.legend()
        plt.xlabel("Height (m)")
        plt.ylabel("Velocity (m/s)")
        plt.gca().invert_yaxis()
        plt.gca().invert_xaxis()
        plt.show()          
        
  
        '''
        plt.plot(velocity_real(v_n, delta_t, g, m, k)[2], velocity_real(v_n, delta_t, g, m, k)[0], label=("realistic"))

        plt.plot(velocity(v_n, delta_t, g, m, k)[2], velocity(v_n, delta_t, g, m, k)[0], label=("simulation"))
        plt.legend()
        plt.gca().invert_yaxis()
        plt.xlabel("time")
        plt.ylabel("Distance)")
        plt.show()
        '''
        
    elif MyInput == 'q':
        print('You have chosen to finish - goodbye.')

#done