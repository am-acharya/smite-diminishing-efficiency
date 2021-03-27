import numpy as np

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

e_hp_variable_prots_no_mitigation = e_hp_vector(SAMPLE_HEALTH, mit_mult_vector(protections_space, MINIMUM_MITIGATION))
e_hp_variable_prots_sample_mitigation = e_hp_vector(SAMPLE_HEALTH, mit_mult_vector(protections_space, SAMPLE_MITIGATION))