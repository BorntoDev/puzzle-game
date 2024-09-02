import pygame
import random
from PIL import Image

# กำหนดขนาดของเกม
WINDOW_WIDTH = 640  # ปรับขนาดหน้าต่างให้เหมาะกับตาราง 16x16
WINDOW_HEIGHT = 640
TILE_SIZE = 40  # ขนาดชิ้นส่วนย่อย
ROWS, COLS = 16, 16  # จำนวนแถวและคอลัมน์เป็น 16x16

def load_and_split_image(image_path):
    """โหลดภาพและแบ่งเป็นชิ้นย่อย"""
    image = Image.open(image_path)
    image = image.resize((COLS * TILE_SIZE, ROWS * TILE_SIZE))  # ปรับขนาดภาพให้ตรงกับขนาดตาราง

    pieces = []
    for row in range(ROWS):
        for col in range(COLS):
            left = col * TILE_SIZE
            top = row * TILE_SIZE
            piece = image.crop((left, top, left + TILE_SIZE, top + TILE_SIZE))
            pieces.append(piece)

    return pieces

def shuffle_pieces(pieces):
    """สุ่มเรียงชิ้นส่วน"""
    random.shuffle(pieces)
    return pieces

def draw_puzzle(screen, pieces):
    """วาดภาพปริศนา"""
    index = 0
    for row in range(ROWS):
        for col in range(COLS):
            piece_image = pygame.image.fromstring(pieces[index].tobytes(), pieces[index].size, pieces[index].mode)
            screen.blit(piece_image, (col * TILE_SIZE, row * TILE_SIZE))
            index += 1

def main():
    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Puzzle Game")

    # โหลดและตัดภาพ
    image_path = '5.png'  # ใส่ path ของรูปที่ต้องการ
    pieces = load_and_split_image(image_path)
    pieces = shuffle_pieces(pieces)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # สีพื้นหลังขาว
        draw_puzzle(screen, pieces)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
