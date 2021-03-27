import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from effective_hp import protections_space, e_hp_variable_prots_no_mitigation, e_hp_variable_prots_sample_mitigation

x = protections_space
y = e_hp_variable_prots_no_mitigation # effective hp with sample health and no %mitigation
z = e_hp_variable_prots_sample_mitigation # effective hp with sample health and sample %mitigation

plt.plot(x,y, 'm-.', x, z, 'c:')
plt.xlabel('Protections', color='#1e8bc3')
plt.ylabel('Effective HP', color='#e74c3c')
plt.title('Efficiency of Protections', color='#34495e')
high_legend = mpatches.Patch(color='magenta', label='2000HP, 0% Mitigation')
low_legend = mpatches.Patch(color='cyan', label='2000HP, 20% Mitigation')
plt.legend(handles=[high_legend,low_legend])
plt.show()