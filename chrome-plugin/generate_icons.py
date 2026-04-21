from PIL import Image, ImageDraw, ImageFont

def create_icon(size):
    img = Image.new('RGB', (size, size), color='#3b82f6')
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", size=int(size * 0.7))
    except:
        font = ImageFont.load_default()
    
    text = "A"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 5
    draw.text((x, y), text, fill="white", font=font)
    
    return img

for size in [16, 48, 128]:
    icon = create_icon(size)
    icon.save(f"icons/icon{size}.png")
