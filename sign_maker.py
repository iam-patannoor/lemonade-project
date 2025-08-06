# sign_maker.py
import datetime

# Create the content for our sign
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Lemonade Stand</title>
    <style>
        body {{
            font-family: 'Comic Sans MS', cursive, sans-serif; /* Fun font for kids! */
            background-color: #FFFACD; /* Lemon Chiffon */
            color: #8B4513; /* Saddle Brown */
            text-align: center;
            padding: 50px;
            border: 5px dashed #FFD700; /* Gold dashed border */
            margin: 20px;
        }}
        h1 {{
            color: #FF4500; /* OrangeRed */
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        p {{
            font-size: 1.5em;
        }}
        .update-time {{
            font-size: 0.9em;
            color: #696969;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <h1>Fresh Lemonade!</h1>
    <p>Best lemonade in town!</p>
    <p>Come get yours today!</p>
    <div class="update-time">
        (Sign last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    </div>
</body>
</html>
"""

# Save the sign content into a file named index.html
with open('index.html', 'w') as f:
    f.write(html_content)

print("Sign (index.html) created successfully!")
