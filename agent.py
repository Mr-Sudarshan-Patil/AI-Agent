from google.adk.agents.llm_agent import Agent



def get_about_me() -> dict:
    return {
        "status": "success",
        "about": {
            "name": "Sudarshan Patil",
            "role": "Frontend Web Developer",
            "summary": (
                "I'm a passionate web developer specializing in React, JavaScript, HTML, CSS, Tailwind, GSAP and Bootstrap "
                "I enjoy building modern, scalable web applications with clean architecture and performance in mind."
            ),
            "location": "Pune, India",
            "experience_years": 2,
        }
    }


def get_skills() -> dict:
    return {
        "status": "success",
        "skills": [
            "HTML", "CSS", "JavaScript","React.js", "Tailwind", "Git/GitHub", "REST APIs",
            "Linux", "Kali Linux", "Termux", "Survey Programming", "Decipher"
        ]
    }


def get_projects() -> dict:
    """Returns your portfolio projects."""
    return {
        "status": "success",
        "projects": [
            {
                "name": "SP WebDev Portfolio Site",
                "description": "A responsive portfolio website showcasing my skills and projects.",
                "tech_stack": ["HTML", "CSS", "JavaScript", "React", "TailwindCSS"],
                "url": "https://www.spwebdev.online/",
                "year": 2024
            },
            {
                "name": "Treding Application",
                "description": "Full-stack app with React for frontend and Node.JS for backend.",
                "tech_stack": ["React.js", "Node.Js", "Express.js", "Tailwind"],
                "year": 2024
            },
        ]
    }


def get_experience() -> dict:
    return {
        "status": "success",
        "experience": [
            {
                "role": "Survey Programmer",
                "company": "Course5 Intelligence.",
                "duration": "2022–2023",
                "responsibilities": [
                    "Programmed and deployed market research surveys.",
                    "Automated report generation using Python.",
                    "Ensured data accuracy and testing quality."
                ]
            },
            {
                "role": "Junior Java Developer (Freelance)",
                "company": "SP WebDev",
                "duration": "2024–Present",
                "responsibilities": [
                    "Developed and deployed Java-based web apps.",
                    "Integrated APIs and optimized performance.",
                    "Managed front-end interfaces with React."
                ]
            }
        ]
    }


def get_contact_info() -> dict:
    """Returns your contact details."""
    return {
        "status": "success",
        "contact": {
            "email": "mr.sudarsh@gmail.com",
            "linkedin": "https://linkedin.com/in/sudarshan-patil",
            "github": "https://github.com/sudarshan-patil",
            "website": "https://www.spwebdev.online/"
        }
    }


def get_academic_background() -> dict:
    return {
        "status": "success",
        "education": [
            {
                "degree": "Bachelor of Technology in Electronics and Telecommunication",
                "college": "R. C. Patel Institute of Technolgy, Shirpur",
                "duration": "2017 – 2021",
                "cgpa": "7.67",
                "percentage": "72%",
                "key_subjects": [
                    "Micro controllers",
                    "Internet of Things"
                    "Java Programming",
                    "Web Development"
                ],
                "achievements": [
                    "Graduated with Distinction",
                    "Built final-year project using IOT"
                ]
            },
            {
                "degree": "Higher Secondary Education (HSC)",
                "college": "GTP College, Nandurbar",
                "duration": "2016 – 2017",
                "percentage": "58%",
                "stream": "Science (Computer Science)"
            },
            {
                "degree": "Secondary School Certificate (SSC)",
                "school": "S.H.G.S. High School, Nandurbar",
                "year": "2014-2015",
                "percentage": "83%"
            }
        ]
    }


root_agent = Agent(
    model="gemini-2.5-flash",
    name="portfolio_agent",
    description="AI agent that provides detailed information about Sudarshan Patil — skills, experience, and projects.",
    instruction=(
        "You are a friendly and professional AI portfolio assistant. "
        "Answer questions about Sudarshan Patil’s skills, experience, and projects using the available tools. "
        "If the user asks something personal or unrelated, politely decline and redirect them to relevant information."
    ),
    tools=[
        get_about_me,
        get_skills,
        get_projects,
        get_experience,
        get_contact_info,
        get_academic_background
    ],
)
