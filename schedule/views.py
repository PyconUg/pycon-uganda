from django.shortcuts import render


def schedule(request, year):
    tabs = [
        {
            "id": "day1-track1",
            "label": "Day 1 - Track 1 (7th August)",
            "rooms": {
                "Seminar Room 1": [
                    {
                        "title": "Registration",
                        "time": "8:30 - 9:00",
                        "category": "logistics",
                    },
                    {
                        "title": "Beyond the Model: Engineering Intelligent Systems with Python and Kubernetes",
                        "time": "9:00 - 11:00",
                        "category": "",
                        "speaker": "Ernest Kabahima",
                    },
                    {
                        "title": "Building Serverless Web Apps with Python and AWS Amplify",
                        "time": "11:00 - 13:00",
                        "category": "keynote",
                        "speaker": "Felix Jumason",
                    },
                    {
                        "title": "Lunch",
                        "time": "13:00 - 14:00",
                        "category": "break",
                        "speaker": "PyCon Volunteers",
                    },
                    {
                        "title": "Supercharge Your API Development with FastAPI",
                        "time": "14:00 - 16:30",
                        "category": "talk",
                        "speaker": "Anne Namuli",
                    },
                ]
            },
        },
        {
            "id": "day1-track2",
            "label": "Day 1 - Track 2 (7th August)",
            "rooms": {
                "Seminar Room 2": [
                    {
                        "title": "Registration",
                        "time": "8:30 - 9:00",
                        "category": "logistics",
                    },
                    {
                        "title": "An Introduction to Plotnine: Visualising Data using The Grammar of Graphics",
                        "time": "9:00 - 12:30",
                        "category": "keynote",
                        "speaker": "Hassan Kibirige",
                    },
                    {
                        "title": "Lunch",
                        "time": "12:50 - 13:55",
                        "category": "break",
                        "speaker": "PyCon Volunteers",
                    },
                    {
                        "title": "Use Your Python to Create Documents and Reproducible Reports with Quarto",
                        "time": "14:00 - 16:30",
                        "category": "talk",
                        "speaker": "Kirabo Atuhurira",
                    },
                ]
            },
        },
        {
            "id": "day2",
            "label": "Day 2 (8th August)",
            "rooms": {
                "MAIN HALL": [
                    {
                        "title": "Registration",
                        "time": "8:30 - 9:00",
                        "category": "logistics",
                    },
                    {
                        "title": "Welcome to PyCon Uganda 2025",
                        "time": "9:00 - 9:15",
                        "category": "keynote",
                        "speaker": "Kirabo Atuhurira",
                    },
                    {
                        "title": "Opening Keynote",
                        "time": "9:15 - 10:15",
                        "category": "keynote",
                        "speaker": "Dan Carpenter",
                    },
                    {
                        "title": "Coffee/Tea Break",
                        "time": "10:15 - 11:00",
                        "category": "break",
                    },
                    {
                        "title": "Build single-page apps, without building an API In Django",
                        "time": "11:05 - 11:35",
                        "category": "talk",
                        "speaker": "Afasha Isakiye",
                    },
                    {
                        "title": "Crafting Real-World Agents: Web, Email, and Your Desktop",
                        "time": "11:40 - 12:10",
                        "category": "talk",
                        "speaker": "Edmond Musiitwa",
                    },
                    {
                        "title": "The FastAPI Beyond CRUD: Build Powerful, Scalable Applications With Python",
                        "time": "12:15 - 13:00",
                        "category": "talk",
                        "speaker": "Jonathan Ssali",
                    },
                    {"title": "Lunch", "time": "13:00 - 14:00", "category": "break"},
                    {
                        "title": "When Code Becomes Art: Building Animations with Python and Manim",
                        "time": "14:05 - 14:35",
                        "category": "talk",
                        "speaker": "Daniel Mwiine",
                    },
                    {
                        "title": "Simulating MicroPython Projects with Raspberry Pi Pico Using Wokwi",
                        "time": "14:40 - 15:10",
                        "category": "talk",
                        "speaker": "Samuel Lunghe",
                    },
                    {
                        "title": "Deploy Django APIs Fearlessly: Azure Terraform & Postman Power!",
                        "time": "15:15 - 15:45",
                        "category": "talk",
                        "speaker": "Samuel Macharis",
                    },
                    {
                        "title": "Closing Keynote",
                        "time": "15:45 - 16:45",
                        "category": "keynote",
                        "speaker": "Lynn Asiimwe, Software Engineer, Google",
                    },
                    {
                        "title": "PyCon Africa 2026 Announcement",
                        "time": "17:00 - 18:00",
                        "category": "announcement",
                        "speaker": "Brian Kayongo",
                    },
                    {
                        "title": "Closing",
                        "time": "18:00 - 18:30",
                        "category": "ceremony",
                    },
                ]
            },
        },
        {
            "id": "day3",
            "label": "Day 3 (9th August - Tutorials Track)",
            "rooms": {
                "MAIN HALL": [
                    {
                        "title": "Coffee/Tea and Registration",
                        "time": "8:00 - 8:55",
                        "category": "break",
                    },
                    {
                        "title": "Beyond the Model: Engineering Intelligent Systems with Python and Kubernetes",
                        "time": "9:00 - 11:00",
                        "category": "tutorial",
                        "speaker": "Ernest Kabahima",
                    },
                    {
                        "title": "Building Serverless Web Apps with Python and AWS Amplify",
                        "time": "11:00 - 13:00",
                        "category": "tutorial",
                        "speaker": "Felix Jumason",
                    },
                    {"title": "Lunch", "time": "13:00 - 14:00", "category": "break"},
                    {
                        "title": "End-to-End ML Pipelines in Python: From Notebook to Production",
                        "time": "14:00 - 16:00",
                        "category": "tutorial",
                        "speaker": "Wesley Kambale",
                    },
                    {
                        "title": "Supercharge Your API Development with FastAPI",
                        "time": "16:00 - 18:00",
                        "category": "tutorial",
                        "speaker": "Anne Namuli",
                    },
                    {"title": "Close", "time": "18:00", "category": "ceremony"},
                ]
            },
        },
    ]

    template_name = f"{year}/schedule/schedule.html"
    context = {"tabs": tabs, "year": year}

    return render(request, template_name, context)
