from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import os

FONTS = {
    "Arial": "arial.ttf",
    "Impact": "impact.ttf",
    "Georgia": "georgia.ttf",
    "Comic Sans MS": "comic.ttf",
    "Times New Roman": "times.ttf",
    "Courier New": "courier.ttf",
    "Verdana": "verdana.ttf",
    "Trebuchet MS": "trebuc.ttf"
}


def get_available_fonts():
    return list(FONTS.keys())


def add_emojis_to_text(text, style="happy"):
    """Add random beautiful emojis around text"""
    emoji_sets = {
        "happy": ["✨", "🌟", "💫", "⭐", "🌸", "💖", "😊", "🌈"],
        "motivational": ["💪", "🔥", "🚀", "⭐", "🎯", "💯", "⚡"],
        "calm": ["🌊", "🍃", "🌙", "💫", "🕊️", "🌸", "🌿"]
    }
    emojis = emoji_sets.get(style, emoji_sets["happy"])
    chosen = random.sample(emojis, min(2, len(emojis)))
    return f"{chosen[0]} {text} {chosen[1]}"


def create_quote_sticker(quote_text, font_name="Arial", add_emojis=False, emoji_style="happy"):
    try:
        # Add emojis if requested
        final_text = quote_text
        if add_emojis:
            final_text = add_emojis_to_text(quote_text, emoji_style)

        # Find font path
        font_path = FONTS.get(font_name, "arial.ttf")
        possible_paths = [
            f"C:/Windows/Fonts/{font_path}",
            f"/usr/share/fonts/truetype/{font_path}",
            f"/Library/Fonts/{font_path}",
            font_path
        ]
        real_path = None
        for p in possible_paths:
            if os.path.exists(p):
                real_path = p
                break
        if not real_path:
            real_path = "arial.ttf"

        # Wrap text
        wrapped = textwrap.wrap(final_text, width=30)
        if not wrapped:
            wrapped = [final_text[:80]]

        line_height = 45
        img_width = 900
        img_height = max(250, len(wrapped) * line_height + 120)

        # Create gradient background
        img = Image.new('RGB', (img_width, img_height), color='#1a1a2e')
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(real_path, 32)
        except:
            font = ImageFont.load_default()

        y = 60
        for line in wrapped:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (img_width - text_width) // 2
            draw.text((x, y), line, font=font, fill='#ffffff')
            y += line_height

        filename = f"sticker_{random.randint(1, 1000000)}.png"
        img.save(filename)
        return filename
    except Exception as e:
        print(f"Sticker error: {e}")
        # Fallback
        img = Image.new('RGB', (800, 200), color='black')
        draw = ImageDraw.Draw(img)
        draw.text((20, 80), quote_text[:80], fill='white')
        filename = f"sticker_{random.randint(1, 1000000)}.png"
        img.save(filename)
        return filename