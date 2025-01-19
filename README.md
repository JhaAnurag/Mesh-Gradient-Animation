# Mesh Gradient Animation

![Animation-ezgif com-optimize](https://github.com/user-attachments/assets/c3f75cf4-72d4-4918-927b-5dbebcb236aa)

This Pygame project visualizes a dynamic mesh gradient. It demonstrates how to create smoothly transitioning color gradients by interpolating colors from moving points across a grid.

## Features

*   **Dynamic Mesh Gradient:**  A visually smooth color gradient that changes in real-time as the color points move.
*   **Moving Gradient Points:**  Four color points that continuously move around the screen, bouncing off the edges.
*   **Interactive Points:** You can click and drag the color points to manually influence the gradient.
*   **Adjustable Spread:** Use the mouse wheel to control the "spread" or influence radius of each color point.
*   **Toggle Point Visibility:** Press the spacebar to show or hide the color points.
*   **Color Interpolation:** Smoothly transitions between colors based on the weighted influence of the gradient points.

## How to Use

1. **Prerequisites:**
    *   Ensure you have Python installed on your system.
    *   Install the Pygame library:
        ```bash
        pip install pygame
        ```

2. **Run the script:**
    Save the provided Python code as a `.py` file (e.g., `mesh_gradient.py`) and run it from your terminal:
    ```bash
    python mesh_gradient.py
    ```

3. **Interact with the animation:**
    *   **Observe the Gradient:** Watch the colors blend and shift as the points move.
    *   **Drag Points:** Click and hold the left mouse button on a colored circle to drag it around and see how it affects the gradient.
    *   **Adjust Spread:** Hover the mouse over a point and use the mouse wheel to increase or decrease its influence area.
    *   **Toggle Visibility:** Press the spacebar to hide or show the control points.

## Potential Improvements

*   **More Points:** Increase the number of gradient points for more complex and richer gradients.
*   **Customizable Colors:** Allow users to set the initial colors of the gradient points.
*   **Different Interpolation Methods:** Experiment with other color interpolation techniques.
*   **Performance Optimization:** For larger grids or more points, optimization might be needed.
*   **Shape Variations:** Instead of circles, use different shapes for the gradient points.
*   **Animation Controls:** Add controls to pause, resume, or reset the animation.
