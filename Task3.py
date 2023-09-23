import tkinter as tk
import random


WIDTH = 300
HEIGHT = 300
SNAKE_SIZE = 10
DELAY = 100  


snake = [(100, 50), (90, 50), (80, 50)]
food = ()
direction = "Right"


def move():
    global direction
    new_head = ()
    
    if direction == "Right":
        new_head = (snake[0][0] + SNAKE_SIZE, snake[0][1])
    elif direction == "Left":
        new_head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
    elif direction == "Up":
        new_head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
    elif direction == "Down":
        new_head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
    
    snake.insert(0, new_head)
    
    if snake[0] == food:
        create_food()
    else:
        snake.pop()
    
    if check_collision():
        game_over()
        return
    
    draw_canvas()
    root.after(DELAY, move)

def draw_canvas():
    canvas.delete("all")
    
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + SNAKE_SIZE, segment[1] + SNAKE_SIZE, fill="green")
    
    canvas.create_oval(food[0], food[1], food[0] + SNAKE_SIZE, food[1] + SNAKE_SIZE, fill="red")

def create_food():
    global food
    x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    food = (x, y)

def check_collision():
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        return True
    
    for segment in snake[1:]:
        if snake[0] == segment:
            return True
    
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="red", font=("Helvetica", 24))

def change_direction(event):
    global direction
    if event.keysym in ("Right", "Left", "Up", "Down"):
        if (event.keysym == "Right" and direction != "Left") or \
           (event.keysym == "Left" and direction != "Right") or \
           (event.keysym == "Up" and direction != "Down") or \
           (event.keysym == "Down" and direction != "Up"):
            direction = event.keysym


root = tk.Tk()
root.title("Snake Game")


canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


root.bind("<Right>", change_direction)
root.bind("<Left>", change_direction)
root.bind("<Up>", change_direction)
root.bind("<Down>", change_direction)

create_food()
move()


root.mainloop()
