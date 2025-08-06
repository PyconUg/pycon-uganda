from django.shortcuts import render


def schedule(request, year):
    tabs = [
        {
            "id": "day1-track1",
            "label": "Day 1 - Track 1 (7th August)",
            "rooms": {
                "Seminar Room 1": [
                    {
                        "title": "Coffee/Tea and Registration",
                        "time": "8:00 - 10:00",
                        "category": "break",
                    },
                    # {
                    #     "title": "Beyond the Model: Engineering Intelligent Systems with Python and Kubernetes",
                    #     "time": "9:00 - 11:00",
                    #     "category": "",
                    #     "speaker": "Ernest Kabahima",
                    # },
                    # {
                    #     "title": "Building Serverless Web Apps with Python and AWS Amplify",
                    #     "time": "11:00 - 13:00",
                    #     "category": "keynote",
                    #     "speaker": "Felix Jumason",
                    # },
                    {"title": "Lunch", "time": "13:00 - 14:00", "category": "break"},
                    {
                        "title": "Supercharge Your API Development with FastAPI",
                        "time": "14:00 - 16:30",
                        "category": "talk",
                        "speaker": "Anne Namuli",
                    },
                    {"title": "Close", "time": "17:00", "category": "ceremony"},
                ]
            },
        },
        {
            "id": "day1-track2",
            "label": "Day 1 - Track 2 (7th August)",
            "rooms": {
                "Seminar Room 2": [
                    {
                        "title": "Coffee/Tea and Registration",
                        "time": "8:00 - 10:00",
                        "category": "break",
                    },
                    {
                        "title": "An Introduction to Plotnine: Visualising Data using The Grammar of Graphics",
                        "time": "10:15 - 12:30",
                        "category": "keynote",
                        "speaker": "Hassan Kibirige",
                    },
                    {"title": "Lunch", "time": "13:00 - 14:00", "category": "break"},
                    {
                        "title": "Use Your Python to Create Documents and Reproducible Reports with Quarto",
                        "time": "14:00 - 16:30",
                        "category": "talk",
                        "speaker": "Kirabo Atuhurira",
                    },
                    {
                        "title": "The API-First Approach",
                        "time": "17:00 - 17:30",
                        "category": "talk",
                        "speaker": "Felix Jumason",
                    },
                    {
                        "title": "The Python and the Soul: A Journey of Courage, Mistakes, and Second Chances",
                        "time": "17:00 - 17:30",
                        "category": "talk",
                        "speaker": " Winena Joann",
                    },
                    {"title": "Close", "time": "18:00", "category": "ceremony"},
                ]
            },
        },
        {
            "id": "day2",
            "label": "Day 2 (8th August)",
            "rooms": {
                "MAIN AUDITORIUM": [
                    {
                        "title": "Coffee/Tea and Registration",
                        "time": "8:00 - 10:00",
                        "category": "break",
                    },
                    {
                        "title": "Welcome to PyCon Uganda 2025",
                        "time": "10:15 - 10:30",
                        "category": "keynote",
                        "speaker": "-",
                    },
                    {
                        "title": "Opening Keynote",
                        "time": "10:30 - 11:00",
                        "category": "keynote",
                        "speaker": "Dr. Tonny J. Oyana",
                    },
                    {
                        "title": "Getting Started with MLOps",
                        "time": "11:00 - 11:40",
                        "category": "talk",
                        "speaker": "Rashid Kissejjere",
                    },
                    {
                        "title": "USSD and Python: Bridging the Digital Divide in Africa",
                        "time": "11:45 - 12:15",
                        "category": "talk",
                        "speaker": "Gilbert Chris",
                    },
                    {
                        "title": "Robots Think in Python: The Language Behind Intelligent Machines",
                        "time": "12:20 - 12:50",
                        "category": "talk",
                        "speaker": "Tirzah Atwiine, Diana Nansubuga",
                    },
                    {
                        "title": "Lunch and Group Photo",
                        "time": "12:50 - 13:55",
                        "category": "break",
                        "speaker": "PyCon Volunteers",
                    },
                    {
                        "title": "AI in Cyber Security",
                        "time": "14:00 - 14:45",
                        "category": "talk",
                        "speaker": "George Ssemaganda",
                    },
                    {
                        "title": "Automatic Repair of Security Vulnerabilities in Python Source Code",
                        "time": "14:50 - 15:20",
                        "category": "talk",
                        "speaker": "Steven Kakaire",
                    },
                    {
                        "title": "Voiceflow & Python for User Assistance and Data Collection",
                        "time": "15:30 - 16:00",
                        "category": "talk",
                        "speaker": "Bashir Kassujja",
                    },
                    {
                        "title": "PyChain: Building Decentralized Applications with Python",
                        "time": "16:05 - 16:35",
                        "category": "talk",
                        "speaker": "Oliseh Genesis",
                    },
                    {
                        "title": "Python + GenAI: Building Chatbots and Assistants with LangChain and OpenAI",
                        "time": "16:40 - 17:05",
                        "category": "talk",
                        "speaker": "Charles Moruri",
                    },
                    {
                        "title": "Open Source Panel",
                        "time": "17:05 - 18:05",
                        "category": "keynote",
                        "speaker": "Dorothy Kabarozi (Moderator)",
                    },
                    {
                        "title": "Lightning Talks and Close",
                        "time": "18:10 - 18:30",
                        "category": "lightning",
                    },
                ]
            },
        },
        {
            "id": "day3",
            "label": "Day 3 (9th August)",
            "rooms": {
                "MAIN HALL": [
                    {
                        "title": "Coffee/Tea and Registration",
                        "time": "8:00 - 10:00",
                        "category": "break",
                    },
                    {
                        "title": "Welcome to PyCon Uganda 2025",
                        "time": "10:15 - 10:30",
                        "category": "keynote",
                        "speaker": "Kirabo Atuhurira",
                    },
                    {
                        "title": "Opening Keynote",
                        "time": "10:30 - 11:00",
                        "category": "keynote",
                        "speaker": "Dan Carpenter",
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
                        "speaker": "Daniel Mwiine, Collins Mesue Asibong",
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
    ]

    template_name = f"{year}/schedule/schedule.html"
    context = {"tabs": tabs, "year": year}

    return render(request, template_name, context)
