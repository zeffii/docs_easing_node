from browser import document

document <= "The graphs below represent the easing functions implemented in the Easing node"

from sv_easing_functions import easing_dict

document <= easing_dict[0].__name__