from supersetapiclient.client import SupersetClient

client = SupersetClient(
    host="http://localhost:8088",
    username="admin",
    password="admin",
)
# Get all dashboards
dashboards = client.dashboards.find()

# Get a dashboard by name
dashboard = client.dashboards.find(dashboard_title="New title")[0]

# Update label_colors mapping
print(dashboard.colors)
dashboard.update_colors({"label": "#aaaaaa"})
print(dashboard.colors)

# Change dashboard title
dashboard.dashboard_title = "weather_trend"

# Save all changes
dashboard.save()
