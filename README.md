# 🗺️ National Museum of South Korea - Path Finder

A **graph-based interactive pathfinding tool** to visualize and explore the shortest paths between rooms in the **National Museum of South Korea**. The map is **generalized** and uses **simple rectangles to represent rooms**, rather than detailed architectural layouts or floor plans of the museum.

<p align="center">
  <img src="https://user-images.githubusercontent.com/00000000/museum-path-example.gif" width="700" alt="Pathfinding Demo">
</p>

---

## 📌 Features

* 🖱️ **Standalone Interactive GUI**: Built using **Tkinter** for a fully native desktop interface.
* 🧠 **Shortest Path Algorithm**: Computes the optimal route using **Dijkstra's algorithm** (via NetworkX).
* 🖼️ **Custom Floor Plan Visualization**: Rooms are displayed as rectangles with relative positioning.
* 🖍️ **Color-Coded Highlights**:
  * 🟧 Rooms in the selected path are highlighted in **orange**.
  * 🟩 The **Permanent Exhibition Hall** is shown in **green**.
  * 🟦 All other rooms are shown in **blue**.
* 🔄 **Real-Time Updates**: Enter new start and end rooms dynamically without restarting the app.

---

## 🛠️ Technologies Used

* **Python 3**
* **NetworkX** – for graph data structure and shortest path computation.
* **Matplotlib** – for plotting the map and paths.
* **Tkinter** – for building the desktop user interface.

---

## 🧪 How to Use

### 🐍 Run the Program

```bash
python museum_pathfinder.py
````

> Make sure you have `matplotlib` and `networkx` installed.

```bash
pip install matplotlib networkx
```

### 🧭 Steps:

1. Enter a valid **starting room name** in "Point A".
2. Enter a valid **ending room name** in "Point B".
3. Click **"Find Shortest Path"**.
4. The map will update and display the optimal path in **red**.

---

## 🏛️ Room Index

The following rooms are supported (use these exact names in the GUI inputs):

* Entrance
* Special Exhibition Gallery 1
* Children's Museum
* Quiet Room
* Food Court 1
* Museum Shop
* Special Exhibition Gallery 2
* Immersive Digital Gallery 1
* Food Court 2
* Museum Shop 2
* Permanent Exhibition Hall

---

## 📸 Example

**Shortest path from** `"Entrance"` **to** `"Immersive Digital Gallery 1"`:

```
Entrance → Museum Shop 2 → Food Court 2 → Immersive Digital Gallery 1
```

The path is displayed in red on the map.

---

## 👤 Author

* **Capps** – [@Recapps](https://github.com/Recapps)

---
