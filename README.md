# Pyhsics Engine

> A small interactive 2D physics sandbox built with Python, Pygame, simple mathematical integration, AABB collision detection, and SQLite persistence.

Pyhsics Engine is an experimental physics playground where rectangular bodies fall under gravity, collide with each other, bounce using impulse response, and can be dragged around with the mouse. It also includes a slide-out menu for creating new objects and a small inspector panel for reading object information.

The project is intentionally compact: the application loop lives in `app.py`, while the physics primitives, UI widgets, world simulation, and persistence logic live in `source.py`.

---

## Preview

The app opens a `1280 x 720` Pygame window with:

- A beige simulation canvas.
- Dynamic rectangular objects affected by gravity.
- Static boundary walls, floor, and ceiling.
- A slide-out side panel styled with `window.png`.
- Menu controls for adding new objects.
- Right-click object inspection.

---

## Features

### Physics Simulation

- **Gravity-based motion** applied every frame.
- **Velocity and acceleration integration** using frame delta time.
- **Static and dynamic bodies** so walls and floors can stay fixed while objects move.
- **Mouse dragging** using a spring-like force model.
- **Axis-aligned bounding box collision detection** for rectangular objects.
- **Impulse-based collision response** using object mass and restitution.
- **Penetration correction** to separate overlapping objects after collision.

### Object System

Each simulated object stores:

- Position: `x`, `y`
- Size: `w`, `h`
- Mass
- Restitution
- Friction value
- Static/dynamic state
- Velocity and acceleration
- Color
- Name

### Interactive UI

- Left-click and drag dynamic objects.
- Right-click an object to inspect its name, mass, and color.
- Open the menu to add new objects.
- Type object name, mass, and Pygame color name.
- Validate required fields before creating an object.
- Animated side panel for add/inspect workflows.

### Persistence

Newly created objects are saved to:

```text
database/data.db
```

The SQLite database contains an `objects` table:

```sql
CREATE TABLE "objects" (
    "name" TEXT NOT NULL,
    "mass" INTEGER NOT NULL,
    "color" TEXT NOT NULL
);
```

Saved objects are loaded back into the world when the app starts.

---

## Project Structure

```text
pyhsics-engine/
|-- app.py              # Main Pygame application loop and UI flow
|-- source.py           # Physics objects, world simulation, buttons, text inputs
|-- window.png          # Side-panel image asset
|-- database/
|   `-- data.db         # SQLite database for saved objects
|-- objects.db          # Empty database file currently unused by the app
|-- requirements.txt    # Dependency list placeholder
`-- README.md           # Project documentation
```

---

## How It Works

### Main Loop

`app.py` creates the window, initializes the world, adds starter objects and static boundaries, then runs a 60 FPS loop:

1. Read Pygame events.
2. Handle mouse, keyboard, buttons, and text fields.
3. Update physics using `dt`.
4. Render all objects.
5. Draw the slide-out UI panel.
6. Save newly created objects to SQLite.

### Physics Object

The `object` class in `source.py` represents a rectangle in the world. Dynamic objects respond to forces and impulses:

```python
obj.appforce(fx, fy)
obj.appimp(jx, jy)
obj.update(dt)
```

Static objects ignore forces and are useful for boundaries such as the floor, ceiling, and walls.

### World Simulation

The `world` class owns all objects and handles:

- Applying gravity.
- Applying mouse drag forces.
- Updating object positions.
- Detecting pairwise rectangle collisions.
- Resolving collisions with impulses.
- Rendering objects.
- Loading and writing SQLite records.

Collision detection uses AABB overlap:

```text
overlap_x = min(a.right, b.right) - max(a.left, b.left)
overlap_y = min(a.bottom, b.bottom) - max(a.top, b.top)
```

The smaller overlap axis becomes the collision normal, then the engine applies an impulse based on relative velocity, inverse mass, and restitution.

---

## Controls

| Action | Control |
| --- | --- |
| Drag object | Left mouse button |
| Release object | Release left mouse button |
| Inspect object | Right mouse button on an object |
| Open add-object panel | `menu` button |
| Close panel | `X` button |
| Type in fields | Click a field, then type |
| Remove text | Backspace |

---

## Running Locally

### 1. Clone or open the project

```bash
cd /home/bro/my-creations/pyhsics-engine
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

`requirements.txt` is currently empty, but the app imports `pygame` and `numpy`.

```bash
pip install pygame numpy
```

### 4. Run the app

```bash
python app.py
```

---

## Adding Objects

Open the menu and fill in:

- `name`: any short object name.
- `mass`: a positive integer.
- `color`: a valid Pygame color name such as `red`, `blue`, `yellow`, `green`, or `purple`.

When the object is added, it appears in the simulation and is saved to SQLite.

---

## Current Limitations

This engine is a learning-focused sandbox, so a few parts are intentionally simple:

- Collision shapes are rectangles only.
- Collision detection is pairwise and not spatially optimized.
- Friction is stored on objects but is not yet fully applied in collision resolution.
- `requirements.txt` does not yet list runtime dependencies.
- The database path is currently absolute inside `source.py`.
- The class name `object` shadows Python's built-in `object` type.

---

## Roadmap Ideas

- Add circles and polygon collision shapes.
- Add friction response during contact resolution.
- Replace the absolute database path with a project-relative path.
- Fill `requirements.txt` with pinned dependencies.
- Add pause, reset, and clear-world controls.
- Add object editing and deletion.
- Add camera zoom and panning.
- Add broad-phase collision detection for better performance with many objects.
- Add tests for collision response and persistence.
- Rename `object` to `PhysicsBody` for clearer Python style.

---

## Tech Stack

- **Python** for application logic.
- **Pygame** for rendering, input, and window management.
- **NumPy** imported for future numerical work.
- **SQLite** for simple local persistence.

---

## Educational Value

This repository is a good foundation for learning:

- Game loops and frame delta timing.
- Force, acceleration, velocity, and position updates.
- Basic rigid body simulation.
- AABB collision detection.
- Impulse-based collision response.
- Simple immediate-mode UI in Pygame.
- Local persistence with SQLite.

---

## License

No license file is currently included. Add one before publishing or distributing the project.
