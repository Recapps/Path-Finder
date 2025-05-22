import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Graph setup
G = nx.Graph()
rooms = [
    "Entrance", "Special Exhibition Gallery 1", "Children's Museum", "Quiet Room",
    "Food Court 1", "Museum Shop", "Special Exhibition Gallery 2",
    "Immersive Digital Gallery 1", "Food Court 2", "Museum Shop 2", "Permanent Exhibition Hall"
]

for room in rooms:
    G.add_node(room)

G.add_edges_from([
    ("Entrance", "Special Exhibition Gallery 1"),
    ("Entrance", "Museum Shop 2"),
    ("Special Exhibition Gallery 1", "Children's Museum"),
    ("Children's Museum", "Quiet Room"),
    ("Quiet Room", "Food Court 1"),
    ("Food Court 1", "Museum Shop"),
    ("Museum Shop", "Special Exhibition Gallery 2"),
    ("Special Exhibition Gallery 2", "Immersive Digital Gallery 1"),
    ("Immersive Digital Gallery 1", "Food Court 2"),
    ("Food Court 2", "Museum Shop 2"),
])

for room in rooms:
    if room != "Permanent Exhibition Hall":
        G.add_edge("Permanent Exhibition Hall", room)

positions = {
    "Children's Museum": (-1, 1),
    "Special Exhibition Gallery 1": (-1, 0),
    "Entrance": (0, 0),
    "Museum Shop 2": (1, 0),
    "Food Court 2": (2, 0),
    "Immersive Digital Gallery 1": (2, 1),
    "Special Exhibition Gallery 2": (2, 2),
    "Museum Shop": (1, 2),
    "Food Court 1": (0, 2),
    "Quiet Room": (-1, 2),
    "Permanent Exhibition Hall": (1, 1)
}

# Draw map function
def draw_map(path=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("National Museum of South Korea Path Finder")

    # Draw all edges
    nx.draw_networkx_edges(G, pos=positions, ax=ax, edge_color='gray')

    # Draw rooms as rectangles
    for node, (x, y) in positions.items():
        width, height = 0.6, 0.3
        color = (
            'orange' if path and node in path else
            'lightgreen' if node == "Permanent Exhibition Hall" else
            'skyblue'
        )
        rect = patches.FancyBboxPatch(
            (x - width / 2, y - height / 2),
            width, height,
            boxstyle="round,pad=0.05",
            linewidth=1,
            edgecolor='black',
            facecolor=color
        )
        ax.add_patch(rect)
        ax.text(x, y, node, ha='center', va='center', fontsize=9, weight='bold')

    # Draw path
    if path:
        edge_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos=positions, edgelist=edge_path, edge_color='red', width=3, ax=ax)

    ax.set_axis_off()
    return fig

# Handle find path button
def on_find_path():
    start = entry_start.get().strip()
    end = entry_end.get().strip()
    try:
        path = nx.shortest_path(G, source=start, target=end)
        messagebox.showinfo("Path Found", f" → ".join(path))
        fig = draw_map(path)
        canvas.figure = fig
        canvas.draw()
    except nx.NetworkXNoPath:
        messagebox.showerror("No Path", f"No path found from '{start}' to '{end}'.")
    except nx.NetworkXError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Museum Path Finder")

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Point A:").grid(row=0, column=0)
entry_start = tk.Entry(frame)
entry_start.grid(row=0, column=1)

tk.Label(frame, text="Point B:").grid(row=1, column=0)
entry_end = tk.Entry(frame)
entry_end.grid(row=1, column=1)

btn = tk.Button(frame, text="Find Shortest Path", command=on_find_path)
btn.grid(row=2, column=0, columnspan=2, pady=5)

# Matplotlib Canvas
fig = draw_map()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
