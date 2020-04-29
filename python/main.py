from browser import document, svg, html
import sv_easing_functions

document <= "The graphs below represent the easing functions implemented in the Easing node"
num_points = 100
deltas = [i/num_points for i in range(num_points)]

def get_points(name):
    scale = 150
    func = getattr(sv_easing_functions, name)
    results = [(int(delta*scale), 150+int(func(delta)*-scale)) for delta in deltas]

    format_item = lambda r: f"{r[0]},{r[1]}"
    return "M " + " ".join([format_item(r) for r in results])

for idx, easing_func in sv_easing_functions.easing_dict.items():
    easing_name = easing_func.__name__

    svg_tag = html.SVG(
        xmlns="http://www.w3.org/2000/svg",
        width="200", height="200",
        style={"border-style": "solid", "border-width":1, "border-color": "#120"})
    svg_tag <= svg.g(id=easing_name)
    document <= svg_tag

    title = svg.text(easing_name, x=70, y=25, font_size=12, text_anchor="middle")
    path = svg.path(fill="none", stroke="#333", stroke_width="2", d=get_points(easing_name))

    panel = document[easing_name]
    panel <= title
    panel <= path

