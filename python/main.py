from browser import document, svg, html
import sv_easing_functions

document <= "The graphs below represent the easing functions implemented in the Easing node"


# document <= sv_easing_functions.easing_dict[0].__name__
# print(easing_dict[0].__name__)
def get_points(name):
    if name == "star":
        return "M 75,38 90,80 135,80 98,107 111,150 75,125 38,150 51,107 15,80 60,80 Z"


svg_tag = html.SVG(
    xmlns="http://www.w3.org/2000/svg",
    width="200", height="200",
    style={"border-style": "solid", "border-width":1, "border-color": "#120"})
svg_tag <= svg.g(id="panel2")

document <= svg_tag

title = svg.text('Title', x=70, y=25, font_size=22, text_anchor="middle")
# circle = svg.circle(cx=70, cy=120, r=40, stroke="black",stroke_width="2",fill="red")
path_1 = svg.path(fill="red", stroke="blue", stroke_width="10", d=get_points("star"))
panel = document["panel2"]
panel <= title
panel <= path_1

