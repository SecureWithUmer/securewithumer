import json

file_path = 'D:/A Midnight Thought/github-profile/gitascii.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

layout = {
    'header': {'x': 0, 'y': 0, 'width': 800, 'height': 90},
    'asciiprofile-portrait': {'x': 0, 'y': 100, 'width': 280, 'height': 288},
    'terminal-info': {'x': 296, 'y': 100, 'width': 504, 'height': 280},
    'languages': {'x': 0, 'y': 400, 'width': 540, 'height': 160},
    'tech-stack': {'x': 560, 'y': 400, 'width': 240, 'height': 160},
    'github-readme-stats': {'x': 0, 'y': 580, 'width': 390, 'height': 210},
    'streak-stats': {'x': 410, 'y': 580, 'width': 390, 'height': 210},
    'profile-trophy': {'x': 0, 'y': 810, 'width': 800, 'height': 200},
    'godprofile-marquee': {'x': 0, 'y': 1030, 'width': 800, 'height': 120}
}

for w in data['widgets']:
    wid = w['widgetId']
    if wid in layout:
        w['visible'] = True
        w['position']['x'] = layout[wid]['x']
        w['position']['y'] = layout[wid]['y']
        w['size']['width'] = layout[wid]['width']
        w['size']['height'] = layout[wid]['height']
    else:
        w['visible'] = False

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("JSON layout updated successfully.")
