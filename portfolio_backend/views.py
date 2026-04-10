from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>slancer Portfolio Backend</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f7f6;
                color: #333;
                text-align: center;
                padding: 50px;
                margin: 0;
            }
            .container {
                background: white;
                max-width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1.1em;
                color: white;
                background-color: #3498db;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
            }
            .btn:hover {
                background-color: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the slancer Portfolio Backend</h1>
            <p>This is the Django backend gateway. Everything is working fine!</p>
            <p>You can manage your projects, blogs, and content from the admin panel.</p>
            <a href="/admin/" class="btn">Click here to Login to the Admin Page</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
