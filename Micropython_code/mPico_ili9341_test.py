import board
import busio
import displayio
import terminalio #Just a font
import adafruit_ili9341
from adafruit_display_text import label

dc=board.GP5
rst=board.GP6
blk=board.GP7
cs=board.GP8 #My display does not have it...

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

displayio.release_displays()
display_bus = displayio.FourWire(spi, command = dc, chip_select=cs, reset=rst)

display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)
splash = displayio.Group(max_size=10)
display.show(splash)

# Draw a green background
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(280, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(max_size=10, scale=3, x=57, y=120)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)