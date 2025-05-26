from flask import Flask, render_template
from models import get_all_tickets, get_all_users

app = Flask(__name__)

@app.route("/")
def index():
    tickets = get_all_tickets()
    users = get_all_users()

    enriched_tickets = []
    for ticket in tickets:
        user = next((u for u in users if u["id"] == ticket["user_id"]), None)
        enriched_tickets.append({
            "id": ticket["id"],
            "title": ticket["title"],
            "status": "open" if ticket["status"] == "open" else "closed",
            "username": user["name"] if user else "Unknown"
        })

    user_ticket_counts = []
    for user in users:
        count = sum(1 for t in tickets if t["user_id"] == user["id"])
        user_ticket_counts.append({"user": user["name"], "count": count})

    return render_template("index.html", tickets=enriched_tickets, counts=user_ticket_counts)

if __name__ == "__main__":
    app.run(debug=True)
