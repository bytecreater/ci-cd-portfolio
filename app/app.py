from flask import Flask, render_template_string

app = Flask(__name__)

# Inline HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nihal Ahemad Khan - Portfolio</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: #f1f1f1;
            margin: 0;
            padding: 0;
        }
        header {
            background: #111;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            margin: 5px 0;
            font-size: 2.5rem;
            color: #00c6ff;
        }
        header p {
            margin: 2px 0;
            font-size: 1rem;
        }
        a {
            color: #00c6ff;
            text-decoration: none;
        }
        .container {
            width: 85%;
            margin: auto;
            padding: 30px 0;
        }
        h2 {
            border-bottom: 2px solid #00c6ff;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        ul {
            list-style: square;
            margin-left: 20px;
        }
        .card {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 12px;
            margin: 15px 0;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.4);
        }
    </style>
</head>
<body>
    <header>
        <h1>Nihal Ahemad Khan</h1>
        <p>Email: <a href="mailto:nihalahemad2003@gmail.com">nihalahemad2003@gmail.com</a> |
           Phone: +91-8999717928 | Location: Pune, India</p>
        <p>
           <a href="https://linkedin.com/in/nihal-ahemad-khan" target="_blank">LinkedIn</a> | 
           <a href="https://github.com/bytecreater" target="_blank">GitHub</a>
        </p>
    </header>
    <div class="container">
        
        <h2>Skills</h2>
        <div class="card">
            <ul>
                <li><b>Programming:</b> Python, Java, C++, JavaScript, Shell Scripting</li>
                <li><b>Cloud:</b> AWS (EC2, S3, IAM, RDS, Lambda), GCP (Compute Engine, Cloud Storage)</li>
                <li><b>DevOps Tools:</b> Docker, Kubernetes, Jenkins, Git/GitHub, GitHub Actions, Linux</li>
                <li><b>CI/CD & Monitoring:</b> Pipelines</li>
                <li><b>Databases:</b> MySQL, MongoDB</li>
                <li><b>Other:</b> Generative AI, UI/UX Design, System Design</li>
                <li><b>Soft Skills:</b> Problem-Solving, Agile, Leadership, Collaboration</li>
            </ul>
        </div>
        
        <h2>Projects</h2>
        <div class="card">
            <p><b>Dockerized Web Application Deployment</b><br>
            Built and containerized a sample web app using Docker and published on Docker Hub.<br>
            <a href="https://hub.docker.com/repository/docker/bytecreater/portfolio-webapp" target="_blank">Docker Hub Link</a></p>
        </div>
        <div class="card">
            <p><b>Application Deployment on Kubernetes</b><br>
            Email Collector App (Node.js + MongoDB) Dockerized and deployed on Kubernetes.<br>
            <a href="https://github.com/bytecreater/K8s-demo-app.git" target="_blank">GitHub Repo</a></p>
        </div>
        <div class="card">
            <p><b>Cloud Deployment with AWS EC2 & Docker</b><br>
            Hosted Dockerized applications on AWS EC2 instances.</p>
        </div>
        <div class="card">
            <p><b>Static Website Hosting on AWS S3</b><br>
            Hosted static website using S3 bucket with configuration & permissions.</p>
        </div>
        
        <h2>Education</h2>
        <div class="card">
            <p><b>B.Tech in Computer Science Engineering</b><br>
            AISSMS Institute of Information Technology, Pune (2023 - 2027)
            <br>
            Assalamualikum Zubair Bhai.
            </p>
        </div>
        
        <h2>Certifications</h2>
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
        
        <h2>Awards & Competitions</h2>
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
    app.run(host="0.0.0.0", port=5000, debug=True)

