import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def effective_hp (hp, damage_mitigation_multiplier):
    return hp / damage_mitigation_multiplier
e_hp_vector = np.vectorize(effective_hp)

def mitigation_multiplier (protections, percent_mitigation):
    return (1-percent_mitigation) * (100/(100+protections))
mit_mult_vector = np.vectorize(mitigation_multiplier)

MINIMUM_HEALTH = 431
MAXIMUM_HEALTH = 5500
health_space = np.linspace(MINIMUM_HEALTH, MAXIMUM_HEALTH, 3000)

MINIMUM_PROTECTIONS = 11
MAXIMUM_PROTECTIONS = 325
protections_space = np.linspace(MINIMUM_PROTECTIONS, MAXIMUM_PROTECTIONS, 3000)

MINIMUM_MITIGATION = 0
SAMPLE_MITIGATION = 0.2
SAMPLE_HEALTH = 2000
SAMPLE_PROTECTIONS = 80

e_hp_variable_health_no_mitigation = e_hp_vector(health_space, mitigation_multiplier(SAMPLE_PROTECTIONS, MINIMUM_MITIGATION))
e_hp_variable_health_sample_mitigation = e_hp_vector(health_space, mitigation_multiplier(SAMPLE_PROTECTIONS, SAMPLE_MITIGATION))

x = health_space
y = e_hp_variable_health_no_mitigation # effective hp with sample protections and no %mitigation
z = e_hp_variable_health_sample_mitigation # effective hp with sample protections and sample %mitigation

plt.plot(x,y, 'm-.', x, z, 'c:')
plt.xlabel('Health Points', color='#1e8bc3')
plt.ylabel('Effective HP', color='#e74c3c')
plt.title('Diminishing Efficiency of Health', color='#34495e')
high_legend = mpatches.Patch(color='magenta', label='80 Prot, 0% Mitigation')
low_legend = mpatches.Patch(color='cyan', label='80 Prot, 20% Mitigation')
plt.legend(handles=[high_legend,low_legend])
plt.show()