import json

# Generate 20 realistic project entries
projects = [
    {
        "db_ib": str(i + 1),
        "img": "https://via.placeholder.com/150",
        "title": title,
        "description": description,
        "status": status,
        "uni": uni,
        "likes": likes,
        "saves": saves,
        "dislikes": dislikes,
        "class1": class1,
        "class2": class2,
        "class3": class3
    }
    for i, (title, description, status, uni, likes, saves, dislikes, class1, class2, class3) in enumerate([
        ("AI-Powered Disease Detection", "Using deep learning to identify diseases from medical imaging scans.", "Active", "Harvard", 120, 85, 14, "AI", "Medical", ""),
        ("Autonomous Drone Swarm", "Developing a swarm of autonomous drones for search and rescue operations.", "In Development", "Stanford", 98, 65, 22, "Robotics", "AI", "Aerospace"),
        ("Next-Gen Battery Technology", "Enhancing lithium-ion battery efficiency with solid-state materials.", "Prototype", "MIT", 150, 100, 10, "Energy", "Materials Science", ""),
        ("Smart Traffic Management System", "An AI-driven traffic control system that reduces congestion and emissions.", "Active", "UC Berkeley", 89, 75, 18, "Transportation", "AI", "Civil Engineering"),
        ("3D Bioprinting of Human Organs", "Developing bioengineered tissues for organ transplant applications.", "Research", "Johns Hopkins", 200, 150, 5, "Medical", "Biotechnology", ""),
        ("Quantum Cryptography Network", "Building a secure communication network based on quantum key distribution.", "In Development", "Oxford", 175, 120, 8, "Computing", "Cryptography", "Quantum"),
        ("Carbon Capture and Storage System", "Designing an industrial-scale CO2 capture system to reduce emissions.", "Prototype", "ETH Zurich", 110, 90, 12, "Environmental", "Chemical Engineering", ""),
        ("Exoskeleton for Paraplegics", "Creating a lightweight, AI-powered exoskeleton for mobility assistance.", "Active", "University of Tokyo", 95, 70, 15, "Medical", "Robotics", ""),
        ("Hyperloop Transportation System", "Developing a high-speed vacuum tube-based transportation solution.", "Prototype", "Caltech", 220, 190, 9, "Transportation", "Mechanical", ""),
        ("AI-Powered Legal Assistant", "An NLP-based legal assistant that helps lawyers analyze case law.", "Active", "Yale", 130, 110, 6, "AI", "Legal", ""),
        ("Smart Agriculture IoT Platform", "A data-driven platform that optimizes crop growth and yield.", "Research", "Cornell", 145, 115, 10, "Agriculture", "IoT", ""),
        ("Personalized Cancer Treatment", "Leveraging genomics to create tailored cancer treatment plans.", "In Development", "UCSF", 180, 140, 7, "Medical", "Genetics", ""),
        ("Underwater Data Centers", "Deploying submerged data centers for efficient cooling and sustainability.", "Prototype", "Microsoft Research", 155, 130, 4, "Computing", "Environmental", ""),
        ("AI-Powered Music Composition", "A deep learning model that generates unique music compositions.", "Active", "Berklee College of Music", 75, 50, 20, "AI", "Music", ""),
        ("Wearable Health Monitoring System", "A non-invasive health tracker with real-time analytics.", "Active", "Imperial College London", 140, 120, 6, "Medical", "Wearable Tech", ""),
        ("Space-Based Solar Power System", "Collecting solar energy in space and beaming it to Earth.", "Research", "NASA", 160, 140, 5, "Energy", "Aerospace", ""),
        ("AI-Driven Financial Forecasting", "A machine learning model for accurate financial market predictions.", "Active", "Wharton", 125, 100, 9, "AI", "Finance", ""),
        ("Neural Interface for Brain-Computer Interaction", "Developing a direct brain-to-computer communication system.", "Prototype", "MIT", 185, 160, 3, "Neuroscience", "AI", ""),
        ("Self-Healing Concrete", "A concrete material that autonomously repairs cracks to extend lifespan.", "In Development", "Delft University", 105, 85, 12, "Civil Engineering", "Materials Science", ""),
        ("AI-Powered Cybersecurity Threat Detection", "A real-time AI-driven system to detect and prevent cyber threats.", "Active", "Carnegie Mellon", 170, 140, 6, "AI", "Cybersecurity", "")
    ])
]

# Save as a JSON file
json_path = "mockdatamarketplace.json"
with open(json_path, "w") as f:
    json.dump(projects, f, indent=4)

print(json_path)
