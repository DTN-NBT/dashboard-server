from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# כתובת השרת הראשי
DATA_SERVER_URL = "https://flask-server-0jtj.onrender.com/devices"

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Device Dashboard</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        h1 { color: #176e61; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f3f3f3; }
    </style>
</head>
<body>
    <h1>📱 Connected Devices Dashboard</h1>
    {% if devices %}
    <table>
        <tr>
            <th>#</th>
            <th>Device Name</th>
            <th>Model</th>
            <th>OS</th>
            <th>System Version</th>
            <th>Compute Power</th>
        </tr>
        {% for device in devices %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ device['Device Name'] }}</td>
            <td>{{ device['Model'] }}</td>
            <td>{{ device['OS'] }}</td>
            <td>{{ device['System Version'] }}</td>
            <td>{{ device['Estimated Compute Power'] }}</td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>No devices connected yet.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def dashboard():
    try:
        response = requests.get(DATA_SERVER_URL)
        devices = response.json()
    except Exception as e:
        devices = []
        print("Error fetching data:", e)
    return render_template_string(TEMPLATE, devices=devices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

