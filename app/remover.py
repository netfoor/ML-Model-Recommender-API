import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import uuid

# Initialize DynamoDB client (use resource to simplify put_item)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Change region if needed

# Sample data (add your actual data here or import from JSON file)
certifications = [
    {
        "id": str(uuid.uuid4()),  # Add an ID if your schema needs a PK
        "title": "AWS Certified Solutions Architect – Associate",
        "issuer": "Amazon Web Services",
        "credentialId": "ABC123DEF456",
        "credentialUrl": "https://aws.amazon.com/verify?cert=ABC123DEF456",
        "issueDate": "2023-05-15",
        "expirationDate": "2026-05-15",
        "photoKey": "certifications/aws-solutions-architect.png",
        "content": "Validated ability to design distributed systems on AWS.",
        "skills": ["AWS", "Cloud Architecture", "Scalability"],
        "category": "Technology",
        "slug": "aws-certified-solutions-architect"
    },
    # add the other 3 examples...
]

projects = [
    {
    "id": str(uuid.uuid4()),
    "title": "Real-Time Chat Application",
    "description": "A chat app built with React, Node.js, and Socket.IO supporting real-time messaging.",
    "place": "Hackathon",
    "projectUrl": "https://chatapp.example.com",
    "githubUrl": "https://github.com/user/chatapp",
    "demoUrl": "https://demo.chatapp.example.com",
    "skills": ["React", "Node.js", "WebSocket"],
    "categories": "Hackathon",
    "photoKey": "projects/chatapp/cover.png",
    "galleryKeys": ["projects/chatapp/1.png", "projects/chatapp/2.png"],
    "startDate": "2023-04-01",
    "endDate": "2023-04-15",
    "status": "Published",
    "featured": True,
    "slug": "real-time-chat-application",
    "metaDescription": "A real-time chat app built during a hackathon.",
    "tags": ["chat", "realtime", "web"]
  },
  {
    "id": str(uuid.uuid4()),
    "title": "E-commerce Dashboard",
    "description": "A data dashboard for tracking sales and customer behavior.",
    "place": "Professional",
    "projectUrl": None,
    "githubUrl": None,
    "demoUrl": None,
    "skills": ["Python", "Data Visualization", "Django"],
    "categories": "Professional",
    "photoKey": "projects/ecommerce-dashboard/cover.png",
    "galleryKeys": [],
    "startDate": "2022-01-10",
    "endDate": "2022-06-30",
    "status": "Published",
    "featured": False,
    "slug": "ecommerce-dashboard",
    "metaDescription": "Dashboard for analyzing e-commerce data trends.",
    "tags": ["data", "dashboard", "analytics"]
  },
  {
    "id": str(uuid.uuid4()),
    "title": "AI Research on NLP",
    "description": "Explored transformer models for sentiment analysis on large datasets.",
    "place": "Academic",
    "projectUrl": "https://university.example.edu/nlp-research",
    "githubUrl": "https://github.com/university/nlp-research",
    "demoUrl": None,
    "skills": ["NLP", "Machine Learning", "Transformers"],
    "categories": "Research",
    "photoKey": "projects/nlp-research/cover.png",
    "galleryKeys": [],
    "startDate": "2021-09-01",
    "endDate": "2022-05-31",
    "status": "Published",
    "featured": True,
    "slug": "ai-research-nlp",
    "metaDescription": "Academic research on applying transformers to sentiment analysis.",
    "tags": ["AI", "nlp", "research"]
  },
  {
    "id": str(uuid.uuid4()),
    "title": "Personal Portfolio Website",
    "description": "A responsive portfolio website showcasing projects and skills.",
    "place": "Personal",
    "projectUrl": "https://portfolio.example.com",
    "githubUrl": "https://github.com/user/portfolio",
    "demoUrl": "https://portfolio.example.com/demo",
    "skills": ["HTML", "CSS", "JavaScript"],
    "categories": "Personal",
    "photoKey": "projects/portfolio/cover.png",
    "galleryKeys": ["projects/portfolio/1.png"],
    "startDate": "2020-05-01",
    "endDate": None,
    "status": "Published",
    "featured": False,
    "slug": "personal-portfolio-website",
    "metaDescription": "A personal website built to highlight skills and projects.",
    "tags": ["portfolio", "frontend", "personal"]
  }
]

# Function to upload items to a table
def upload_items(table_name, items):
    table = dynamodb.Table(table_name)
    for item in items:
        try:
            table.put_item(Item=item)
            print(f"Uploaded item to {table_name}: {item.get('title') or item.get('id')}")
        except ClientError as e:
            print(f"Error uploading to {table_name}: {e.response['Error']['Message']}")

def main():
    # Upload data
    upload_items('Projects-qfrdapgnsbckbbphx5zhmz7hhe-NONE', projects)

if __name__ == "__main__":
    main()
