import PyDSTool as dst
import numpy as np
from matplotlib import pyplot as plt

# we must give a name
DSargs = dst.args(name='Calcium channel model')
# parameters
DSargs.pars = { 'alpha': 0.1,
               'beta': 0.01,
                 'k': 0.25,
                'gamm': 0.01
              }
# auxiliary helper function(s) -- function name: ([func signature], definition)
#DSargs.fnspecs  = {'minf': (['v'], '0.5 * (1 + tanh( (v-v1)/v2 ))') }
DSargs.fnspecs  = {'growth': (['a'], '(beta + a*a)/(1 + a*a)'),
		   'suppression': (['b'], '1/(1+(b/k)**2)')
		  }
# rhs of the differential equation, including dummy variable w
DSargs.varspecs = {'a': 'alpha * growth(a) * suppression(b) - a',
		   'b': 'gamm * (a - b)',
                   'w': 'a-w' }
# initial conditions
DSargs.ics      = {'a': 10, 'b':0, 'w': 0 }

DSargs.tdomain = [0,100]                         # set the range of integration.
ode  = dst.Generator.Vode_ODEsystem(DSargs)     # an instance of the 'Generator' class.
traj = ode.compute('polarization')              # integrate ODE
pts  = traj.sample(dt=0.1)                      # Data for plotting

# PyPlot commands
plt.plot(pts['t'], pts['a'])
plt.xlabel('time')                              # Axes labels
plt.ylabel('voltage')                           # ...
plt.ylim([0,65])                                # Range of the y axis
plt.title(ode.name)                             # Figure title from model name
plt.show()
