import tkinter as tk

def create_doublecircle(canvas, x, y):
    # Flower petals (ovals)
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill='purple')
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill='pink')
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill='pink')

    # Flower center (circle)
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='aqua')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Graphic Model")

    # Create a canvas widget to draw on
    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack()

    # Draw the flower model at the center of the canvas
    create_doublecircle(canvas, 200, 200)

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()