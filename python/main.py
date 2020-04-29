from browser import document, svg, html
import sv_easing_functions

document <= "The graphs below represent the easing functions implemented in the Easing node"
deltas = [i/40 for i in range(40)]

def get_points(name):
    scale = 150
    func = getattr(sv_easing_functions, name)
    results = [(int(delta*scale), int(func(delta)*scale)) for delta in deltas]

    format_item = lambda r: f"{r[0]},{r[1]}"
    return "M " + " ".join([format_item(r) for r in results]) + " Z"

for idx, easing_func in sv_easing_functions.easing_dict.items():
    if idx > 4:
        break
    easing_name = easing_func.__name__

    svg_tag = html.SVG(
        xmlns="http://www.w3.org/2000/svg",
        width="200", height="200",
        style={"border-style": "solid", "border-width":1, "border-color": "#120"})
    svg_tag <= svg.g(id=easing_name)
    document <= svg_tag

    title = svg.text(easing_name, x=70, y=25, font_size=12, text_anchor="middle")
    path_1 = svg.path(fill="red", stroke="blue", stroke_width="10", d=get_points(easing_name))

    panel = document[easing_name]
    panel <= title
    panel <= path_1

