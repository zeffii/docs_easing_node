from browser import document
from sv_easing_functions import easing_dict

document <= "The graphs below represent the easing functions implemented in the Easing node"


document <= easing_dict[0].__name__
# print(easing_dict[0].__name__)
