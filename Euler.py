from __future__ import division
import numpy as np
import pylab as py

#definition of the ODE
def ExplicitEuler(u,t):
        return np.array([ u[1],-u[0]+u[0]**3-u[1] ])

if __name__=='__main__':
        v_h = [] #list of steps size
        Er_h = [] #list of errors
        for n in xrange(50,200,5):
                y0= [0,1]#initial condition
                y= [y0]  #list of approximate solutions
                v = [y0] #initialize a list to compute the 
                h=1/n # delta
                v_h.append(h)
                #Euler Explicit 
                for i in xrange(n):
                        y.append(list(np.array(y[i])+ h*ExplicitEuler(y[i],i*h)))
                #Compute the global error changing the step
                for i in xrange(2*n):
                        v.append(list(np.array(v[i])+ (h/2)*ExplicitEuler(v[i],i*h/2)))
                #global error
                err = 2*np.linalg.norm(np.array(y[-1])- np.array(v[-1]))
                Er_h.append(err)
        #plot        
        py.plot(py.log(v_h),py.log(Er_h),'g*',py.log(v_h),py.log(Er_h),'r')
        #compute the order of convergence
        Slope = (py.log(Er_h[-1]) - py.log(Er_h[0]))/(py.log(v_h[-1])-py.log(v_h[0]))
        py.title("the graph of the error vs Delta t in log scale")
        py.xlabel("Change in time")
        py.ylabel("Error")
        print "The list of approximates solution",y[-1]
        print "order of convergence(Slope of Graph) ", Slope
        py.show()
