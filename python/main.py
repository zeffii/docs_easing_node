from browser import document, svg
import sv_easing_functions

document <= "The graphs below represent the easing functions implemented in the Easing node"


document <= sv_easing_functions.easing_dict[0].__name__
# print(easing_dict[0].__name__)


title = svg.text('Title', x=70, y=25, font_size=22, text_anchor="middle")
circle = svg.circle(cx=70, cy=120, r=40, stroke="black",stroke_width="2",fill="red")
panel = document['panel']
panel <= title
panel <= circle