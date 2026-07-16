import pygame

pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    RED = (220, 20, 60)
    BLUE = (30, 144, 255)
    GREEN = (50, 205, 50)
    PURPLE = (186, 85, 211)
    ORANGE = (255, 165, 0)
    DARK_GREEN = (34, 139, 34)
    LIGHT_GREY = (180, 180, 180)
        
    BLOCK_GRADIENT = [
        (128, 128, 128),
        (160, 160, 160),
        (198, 198, 198)
    ]
    
    FONT = pygame.font.SysFont("Ariel", 30)
    LARGE_FONT = pygame.font.SysFont("Ariel", 40)
    
    SIDE_PAD = 100
    TOP_PAD = 150
    
    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self. window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)
        
    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)
        
        self.bin_width = round((self.width - self.SIDE_PAD)/len(list)) # each block = available width / n_bins
        self.bin_height = round((self.height - self.TOP_PAD)/(self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD//2

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", True, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 10))
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending Order | D - Descending Order", True, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 50))

    sorting_algos = draw_info.FONT.render("B - Bubble | I - Insertion | S - Selection | M - Merge | Q - Quick | H - Heap | K - Bucket", True, draw_info.BLACK)
    draw_info.window.blit(sorting_algos, (draw_info.width / 2 - sorting_algos.get_width() / 2, 70))
    
    draw_list(draw_info)
    pygame.display.update()
    
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.list
    
    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD//2, 
            draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, 
            draw_info.height - draw_info.TOP_PAD
        )
        
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    
    for i, val in enumerate(lst):
        x = draw_info.start_x + i*draw_info.bin_width
        # y = draw_info.bin_height - (val - draw_info.min_val)*draw_info.bin_height
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bin_height
        
        color = draw_info.BLOCK_GRADIENT[i%3]
        
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bin_width, draw_info.height))
        
    if clear_bg:
        pygame.display.update()  