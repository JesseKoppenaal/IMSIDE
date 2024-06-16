# =============================================================================
# Runfile general network in equilibrium
# =============================================================================
# Bouke, December 2023
# =============================================================================
# import functions
# =============================================================================
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import settings_td_v1
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from core_td_v1 import mod42_netw
#from inputfile_v1 import input_network
#from functions_all_v1 import network_funcs

run_name = 'MRI_ssp2_SLR'

delta = mod42_netw(settings_td_v1.constants, settings_td_v1.geo_pars, settings_td_v1.forc_pars, settings_td_v1.phys_pars)#, pars_seadom = (25000,100,10), pars_rivdom = (200000,2000,0))

#calculate river discharge distribution
delta.run_model()
 

delta.calc_output()


#%%

X2_oude_maas, X2_nieuwe_maas = delta.calc_X2_td()
save_folder = '../../X2_results/' + run_name
os.makedirs(save_folder, exist_ok = True)

np.save(save_folder + '/oude_maas_X2.npy', X2_oude_maas)
np.save(save_folder + '/nieuwe_maas_X2.npy', X2_nieuwe_maas)


#visualisation
delta.plot_s_gen_td(0)
delta.plot_s_gen_td(-1)

#for Rhine-Meuse
out427 = delta.plot_salt_pointRM(4.2,51.95,1)
out427 = delta.plot_salt_pointRM(4.5,51.85,1)
out427 = delta.plot_salt_pointRM(4.5,51.92,1)
#delta.plot_salt_pointRM(4.5,51.9,1)
#delta.anim_RM_st('td_220224_v3')
