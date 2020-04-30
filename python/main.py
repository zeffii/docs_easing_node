from browser import document, svg, html
import sv_easing_functions

# document <= "The graphs below represent the easing functions implemented in the Easing node"
num_points = 80
deltas = [i/num_points for i in range(num_points)]
scale = 150

path_y_offset = 210
rect_y_offset = path_y_offset - scale 
g_x_offset, g_y_offset = 25, 0

def get_points(name):
    func = getattr(sv_easing_functions, name)
    results = [(int(delta*scale), int(func(delta)*-scale)) for delta in deltas]

    format_item = lambda r: f"{r[0]},{r[1]}"
    return "M " + " ".join([format_item(r) for r in results])

for idx, easing_func in sv_easing_functions.easing_dict.items():
    easing_name = easing_func.__name__

    svg_tag = html.SVG(xmlns="http://www.w3.org/2000/svg", width=200, height=280, style={})
    svg_tag <= svg.g(id=easing_name, transform=f"translate({g_x_offset} {g_y_offset})")
    document <= svg_tag

    title = svg.text(easing_name, x=70, y=25, font_size=17, text_anchor="middle")
    bg = svg.rect(x=0, y=rect_y_offset, width=150, height=150, stroke="#999", fill="#ddd")
    path = svg.path(
        transform=f"translate(0, {path_y_offset})", fill="none", stroke="#33a", 
        stroke_width="2", d=get_points(easing_name))
    panel = document[easing_name]
    panel <= title
    panel <= bg
    panel <= path

