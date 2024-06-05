import pyautogui as ag

ag.FAILSAFE = True

class MenuNavigator():
    def __init__(self, items:iter, columns:int, rows:int, wrap_mode):
        self.items = items
        self.columns = max(columns, 1)
        self.rows = max(rows, 1)
        self.wrap_mode = wrap_mode
        self.cursor_pos = 0

    def move_cursor_to(self, item):
        available_paths = {}

        cursor_x = self.cursor_pos % self.columns
        cursor_y = self.cursor_pos // self.columns

        target_pos = self.items.index(item)
        target_x = target_pos % self.columns
        target_y = target_pos // self.columns

        delta_x = target_x - cursor_x
        delta_y = target_y - cursor_y
        available_paths["normal"] = [delta_x, delta_y]

        if self.wrap_mode == 1:

            wrap_dy = self.wrap_delta(self.rows, delta_y)
            available_paths["wrap_vertical"] = [delta_x, wrap_dy]

            row_offset = 1
            wrap_dx = self.wrap_delta(self.columns, delta_x)
            if (cursor_y == 0 and wrap_dx < 0) or (cursor_y == self.rows - 1 and wrap_dx > 0):
                row_offset = 1 - self.rows
            wrap_dy = delta_y + row_offset * (-1 if wrap_dx > 0 else 1)
            available_paths["wrap_horizontal"] = [wrap_dx, wrap_dy]

            wrap_dy = self.wrap_delta(self.rows, wrap_dy)
            available_paths["wrap_hv"] = [wrap_dx, wrap_dy]

        best_solution = "normal"
        best_steps = self.columns + self.rows - 2
        for k,v in available_paths.items():
            s = sum([abs(i) for i in v])
            if s < best_steps:
                best_steps = s
                best_solution = k

        for _ in range(abs(available_paths[best_solution][0])):
            if available_paths[best_solution][0] > 0:
                ag.press("right")
            else:
                ag.press("left")
        for _ in range(abs(available_paths[best_solution][1])):
            if available_paths[best_solution][1] > 0:
                ag.press("down")
            else:
                ag.press("up")

        self.cursor_pos = target_pos

    def wrap_delta(self, dimension, delta):
        return (dimension - abs(delta)) * (-1 if delta > 0 else 1)

    def quit(self):
        self.cursor_pos = 0
        ag.press("esc")

