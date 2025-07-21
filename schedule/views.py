from django.shortcuts import render


def schedule(request, year):
    tabs = [
        {
            "id": "day1",
            "label": "Day 1 (9th October)",
            "rooms": {
                "PACIFIC HALL": [
                    {"title": "Tea", "time": "7:00 - 9:00", "category": "break"},
                    {"title": "Registration and Badge Pickup", "time": "9:00 - 11:00", "category": "logistics"},
                    {"title": "Welcome and PyCon Official Opening Address", "time": "11:00 - 12:00", "category": "keynote"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Python for Data Science", "time": "13:30 - 14:15", "category": "talk"},
                    {"title": "Django Best Practices", "time": "14:30 - 15:15", "category": "talk"},
                    {"title": "Coffee Break", "time": "15:15 - 15:45", "category": "break"},
                    {"title": "Web Development with Flask", "time": "15:45 - 16:30", "category": "talk"},
                ],
                "VOLTA ROOM": [
                    {"title": "Tea", "time": "7:00 - 9:00", "category": "break"},
                    {"title": "Registration and Badge Pickup", "time": "9:00 - 11:00", "category": "logistics"},
                    {"title": "Welcome and PyCon Official Opening Address", "time": "11:00 - 12:00", "category": "keynote"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Django Girls Workshop", "time": "13:30 - 16:30", "category": "django-girls"},
                ],
                "VIDEO CONFERENCE ROOM": [
                    {"title": "Tea", "time": "7:00 - 9:00", "category": "break"},
                    {"title": "Registration and Badge Pickup", "time": "9:00 - 11:00", "category": "logistics"},
                    {"title": "Welcome and PyCon Official Opening Address", "time": "11:00 - 12:00", "category": "keynote"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Remote Participation Setup", "time": "13:30 - 14:00", "category": "logistics"},
                    {"title": "Virtual Networking Session", "time": "14:00 - 16:30", "category": "networking"},
                ],
            },
        },
        {
            "id": "day2",
            "label": "Day 2 (10th October)",
            "rooms": {
                "PACIFIC HALL": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Keynote: Python in Africa", "time": "9:00 - 9:45", "category": "keynote"},
                    {"title": "Machine Learning with Python", "time": "10:00 - 10:45", "category": "talk"},
                    {"title": "Coffee Break", "time": "10:45 - 11:15", "category": "break"},
                    {"title": "API Development with FastAPI", "time": "11:15 - 12:00", "category": "talk"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Python Testing Strategies", "time": "13:30 - 14:15", "category": "talk"},
                    {"title": "Lightning Talks", "time": "14:30 - 15:30", "category": "lightning"},
                ],
                "VOLTA ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Community Building Workshop", "time": "9:00 - 12:00", "category": "community"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "PyLadies Session", "time": "13:30 - 16:00", "category": "pyladies"},
                ],
                "VIDEO CONFERENCE ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Remote Workshop: Python Automation", "time": "9:00 - 12:00", "category": "workshop"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Virtual Career Fair", "time": "13:30 - 16:00", "category": "networking"},
                ],
            },
        },
        {
            "id": "day3",
            "label": "Day 3 (11th October)",
            "rooms": {
                "PACIFIC HALL": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Open Source in Uganda", "time": "9:00 - 9:45", "category": "talk"},
                    {"title": "Community Summit Planning", "time": "10:00 - 12:00", "category": "community"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Project Showcase", "time": "13:30 - 15:00", "category": "showcase"},
                    {"title": "Closing Ceremony", "time": "15:00 - 16:00", "category": "ceremony"},
                ],
                "VOLTA ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Women in Tech Panel", "time": "9:00 - 10:30", "category": "pyladies"},
                    {"title": "Coffee Break", "time": "10:30 - 11:00", "category": "break"},
                    {"title": "Mentorship Program Launch", "time": "11:00 - 12:00", "category": "community"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Networking & Job Fair", "time": "13:30 - 16:00", "category": "networking"},
                ],
                "VIDEO CONFERENCE ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Global Python Community Connect", "time": "9:00 - 12:00", "category": "networking"},
                    {"title": "Lunch Break", "time": "12:00 - 13:30", "category": "break"},
                    {"title": "Virtual After-party", "time": "13:30 - 16:00", "category": "social"},
                ],
            },
        },
        {
            "id": "day4",
            "label": "Day 4 (12th October)",
            "rooms": {
                "PACIFIC HALL": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Advanced Python Patterns", "time": "9:00 - 10:30", "category": "talk"},
                    {"title": "Coffee Break", "time": "10:30 - 11:00", "category": "break"},
                    {"title": "Django Advanced Workshop", "time": "11:00 - 12:30", "category": "workshop"},
                    {"title": "Lunch Break", "time": "12:30 - 14:00", "category": "break"},
                    {"title": "PyData Analytics Session", "time": "14:00 - 16:00", "category": "pydata"},
                ],
                "VOLTA ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Startup Pitch Session", "time": "9:00 - 12:30", "category": "startup"},
                    {"title": "Lunch Break", "time": "12:30 - 14:00", "category": "break"},
                    {"title": "Investor Meetup", "time": "14:00 - 16:00", "category": "networking"},
                ],
                "VIDEO CONFERENCE ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "International Speakers Series", "time": "9:00 - 12:30", "category": "keynote"},
                    {"title": "Lunch Break", "time": "12:30 - 14:00", "category": "break"},
                    {"title": "Remote Collaboration Workshop", "time": "14:00 - 16:00", "category": "workshop"},
                ],
            },
        },
        {
            "id": "day5",
            "label": "Day 5 (13th October)",
            "rooms": {
                "PACIFIC HALL": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Open Source Sprint Setup", "time": "9:00 - 9:30", "category": "open-source"},
                    {"title": "Sprint Session 1", "time": "9:30 - 12:00", "category": "open-source"},
                    {"title": "Lunch Break", "time": "12:00 - 13:00", "category": "break"},
                    {"title": "Sprint Session 2", "time": "13:00 - 15:30", "category": "open-source"},
                    {"title": "Sprint Presentations", "time": "15:30 - 16:00", "category": "showcase"},
                ],
                "VOLTA ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Code Review Workshop", "time": "9:00 - 12:00", "category": "workshop"},
                    {"title": "Lunch Break", "time": "12:00 - 13:00", "category": "break"},
                    {"title": "Contribution Guidelines", "time": "13:00 - 14:00", "category": "open-source"},
                    {"title": "Final Networking", "time": "14:00 - 16:00", "category": "networking"},
                ],
                "VIDEO CONFERENCE ROOM": [
                    {"title": "Breakfast", "time": "8:00 - 9:00", "category": "break"},
                    {"title": "Remote Sprint Coordination", "time": "9:00 - 12:00", "category": "open-source"},
                    {"title": "Lunch Break", "time": "12:00 - 13:00", "category": "break"},
                    {"title": "Global Contributors Meetup", "time": "13:00 - 16:00", "category": "networking"},
                ],
            },
        },
    ]

    template_name = f"{year}/schedule/schedule.html"
    context = {"tabs": tabs, "year": year}

    return render(request, template_name, context)