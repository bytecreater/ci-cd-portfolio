from flask import Flask, render_template_string
import base64

app = Flask(__name__)

# --- Image Data ---
# Your JPG image has been encoded into a Base64 string.
# This allows the image to be embedded directly in the HTML without needing a separate file.
image_path = 'Gemini_Generated_Image_bvj2mgbvj2mgbvj2.jpg'
try:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    IMAGE_DATA_URI = f"data:image/jpeg;base64,{encoded_string}"
except FileNotFoundError:
    # This is a fallback in case the image file is not found when you run the script.
    # It will show a placeholder instead of crashing.
    print(f"Warning: Image file '{image_path}' not found. Using a placeholder.")
    IMAGE_DATA_URI = "https://via.placeholder.com/150"


# --- Inline HTML Template ---
# The CSS and the image data are now included directly inside this string.
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nihal Ahemad Khan - Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    
    <style>
        /* --- Embedded CSS --- */
        /* --- General Styles --- */
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0f2027; /* fallback for old browsers */
            background: -webkit-linear-gradient(to right, #2c5364, #203a43, #0f2027); /* Chrome 10-25, Safari 5.1-6 */
            background: linear-gradient(to right, #2c5364, #203a43, #0f2027); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            color: #f1f1f1;
            margin: 0;
            padding: 0;
        }}

        .container {{
            width: 80%;
            max-width: 1000px;
            margin: auto;
            padding: 30px 0;
        }}

        h1, h2, h3 {{
            color: #00c6ff;
        }}

        h2 {{
            border-bottom: 2px solid #00c6ff;
            padding-bottom: 10px;
            margin-top: 40px;
            font-size: 1.8rem;
        }}
        
        h2 .fas, h2 .fa {{
            margin-right: 15px;
        }}

        a {{
            color: #00c6ff;
            text-decoration: none;
            transition: color 0.3s;
        }}

        a:hover {{
            color: #ffffff;
        }}

        ul {{
            list-style: none;
            padding-left: 0;
        }}

        li {{
            margin-bottom: 8px;
        }}

        /* --- Header Section --- */
        header {{
            background: rgba(0,0,0,0.3);
            padding: 40px 20px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            border-bottom: 3px solid #00c6ff;
        }}

        .profile-photo {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 4px solid #00c6ff;
            object-fit: cover;
            margin-bottom: 20px;
        }}

        .header-text h1 {{
            margin: 0;
            font-size: 3rem;
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: #ccc;
            margin: 5px 0 20px 0;
            font-style: italic;
        }}

        .contact-info a, .contact-info span {{
            margin: 0 10px;
            color: #ddd;
        }}
        .contact-info i {{
            margin-right: 5px;
        }}

        .social-links {{
            margin-top: 15px;
        }}

        .social-links a {{
            font-size: 1.2rem;
            margin: 0 15px;
        }}
        
        .social-links i {{
            margin-right: 8px;
        }}

        /* --- Card Styles --- */
        .card {{
            background: rgba(255,255,255,0.05);
            padding: 25px;
            border-radius: 12px;
            margin: 20px 0;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0px 8px 25px rgba(0, 198, 255, 0.3);
        }}

        .card h3 {{
            margin-top: 0;
        }}

        .link-button {{
            display: inline-block;
            background-color: #00c6ff;
            color: #111;
            padding: 8px 15px;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 10px;
            transition: background-color 0.3s;
        }}

        .link-button:hover {{
            background-color: #fff;
            color: #111;
        }}

        /* --- Skills Section --- */
        .skills-card p {{
            margin-bottom: 15px;
        }}

        .skill-tag {{
            display: inline-block;
            background: #2c5364;
            color: #e0e0e0;
            padding: 5px 12px;
            border-radius: 15px;
            margin: 3px;
            font-size: 0.9rem;
        }}

        /* --- Responsive Design --- */
        @media (min-width: 768px) {{
            header {{
                flex-direction: row;
                text-align: left;
                padding: 50px;
            }}
            .profile-photo {{
                margin-right: 40px;
                margin-bottom: 0;
            }}
        }}
    </style>
</head>
<body>

    <header>
        <img src="{IMAGE_DATA_URI}" alt="Nihal Ahemad Khan" class="profile-photo">
        <div class="header-text">
            <h1>Nihal Ahemad Khan</h1>
            <p class="subtitle">Cloud & DevOps Enthusiast</p>
            <div class="contact-info">
                <a href="mailto:nihalahemad2003@gmail.com"><i class="fas fa-envelope"></i> nihalahemad2003@gmail.com</a>
                <span>|</span>
                <a><i class="fas fa-phone"></i> +91-8999717928</a>
                <span>|</span>
                <a><i class="fas fa-map-marker-alt"></i> Pune, India</a>
            </div>
            <div class="social-links">
                <a href="https://linkedin.com/in/nihal-ahemad-khan" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
                <a href="https://github.com/bytecreater" target="_blank"><i class="fab fa-github"></i> GitHub</a>
            </div>
        </div>
    </header>

    <div class="container">
        
        <h2><i class="fas fa-cogs"></i> Skills</h2>
        <div class="card skills-card">
            <p><b>Programming:</b> <span class="skill-tag">Python</span> <span class="skill-tag">Java</span> <span class="skill-tag">C++</span> <span class="skill-tag">JavaScript</span> <span class="skill-tag">Shell Scripting</span></p>
            <p><b>Cloud:</b> <span class="skill-tag">AWS (EC2, S3, IAM, RDS, Lambda)</span> <span class="skill-tag">GCP (Compute Engine, Cloud Storage)</span></p>
            <p><b>DevOps Tools:</b> <span class="skill-tag">Docker</span> <span class="skill-tag">Kubernetes</span> <span class="skill-tag">Jenkins</span> <span class="skill-tag">Git/GitHub</span> <span class="skill-tag">GitHub Actions</span> <span class="skill-tag">Linux</span></p>
            <p><b>Databases:</b> <span class="skill-tag">MySQL</span> <span class="skill-tag">MongoDB</span></p>
            <p><b>Other:</b> <span class="skill-tag">Generative AI</span> <span class="skill-tag">UI/UX Design</span> <span class="skill-tag">System Design</span></p>
            <p><b>Soft Skills:</b> <span class="skill-tag">Problem-Solving</span> <span class="skill-tag">Agile</span> <span class="skill-tag">Leadership</span> <span class="skill-tag">Collaboration</span></p>
        </div>
        
        <h2><i class="fas fa-project-diagram"></i> Projects</h2>
        <div class="card">
            <h3>Dockerized Web Application Deployment</h3>
            <p>Built and containerized a sample web app using Docker and published on Docker Hub.</p>
            <a href="https://hub.docker.com/repository/docker/bytecreater/portfolio-webapp" class="link-button" target="_blank">View on Docker Hub</a>
        </div>
        <div class="card">
            <h3>Application Deployment on Kubernetes</h3>
            <p>Email Collector App (Node.js + MongoDB) Dockerized and deployed on Kubernetes.</p>
            <a href="https://github.com/bytecreater/K8s-demo-app.git" class="link-button" target="_blank">View on GitHub</a>
        </div>
        <div class="card">
            <h3>Cloud Deployment with AWS EC2 & Docker</h3>
            <p>Hosted various Dockerized applications on AWS EC2 instances, configuring security groups and networking.</p>
        </div>
        <div class="card">
            <h3>Static Website Hosting on AWS S3</h3>
            <p>Hosted a static website using an S3 bucket with public access configuration and permissions.</p>
        </div>
        
        <h2><i class="fas fa-graduation-cap"></i> Education</h2>
        <div class="card">
            <h3>B.Tech in Computer Science Engineering</h3>
            <p>AISSMS Institute of Information Technology, Pune (2023 - 2027)</p>
        </div>
        
        <h2><i class="fas fa-certificate"></i> Certifications</h2>
        <div class="card">
            <ul>
                <li>NPTEL: Joy of Computing Using Python – IIT Madras</li>
                <li>Introduction to Generative AI – Google</li>
                <li>Introduction to Responsible AI – Google</li>
                <li>Front End Development - CSS – Great Learning</li>
                <li>Python Essential Certificate – HackerRank</li>
                <li>Udemy Labs: Docker - SWARM - DevOps – KodeKloud</li>
            </ul>
        </div>
        
        <h2><i class="fas fa-trophy"></i> Awards & Competitions</h2>
        <div class="card">
            <ul>
                <li>Cyber Olympiad - City Rank 1</li>
                <li>Pulzion'24: Tech Across Ages – PICT</li>
                <li>NEET Score: 580 (2022)</li>
                <li>JEE Percentile: 95%ile (2022)</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    # Important: Make sure the image file ('Gemini_Generated_Image_bvj2mgbvj2mgbvj2.jpg')
    # is in the same directory as this script when you run it.
    app.run(host="0.0.0.0", port=5000, debug=True)