# Yatsiuk.University.Pinterest
## About
"Inspira" is a web application designed to inspire creativity, imagination, and discovery. Much like Pinterest, Inspira allows users to discover, save, and share images and ideas with your mutuals across various categories. Whether you're looking for design inspiration, recipes, travel destinations, or DIY projects, Inspira provides a platform to explore and curate content that resonates with you.

## Documentation 
### Introduction
Inspira is a visual discovery engine designed to help users explore and find inspiration on various topics such as fashion, recipes, home decor, and more. Users can discover new ideas through images and videos, save them to their own personalized boards, and share them with others.

### Features
• User Registration: Allow users to sign up for an account using their Google credentials.

• Create Boards: Users can create custom boards to organize and save their favorite images and videos.

• Search Functionality: Implement a search feature to allow users to discover content based on keywords and categories.

• Pinning Images/Videos: Enable users to pin images or videos from the web onto their boards for future reference.

• Explore Feed: Curate a personalized feed of content based on the user's interests and previous activity.

• Follow Other Users: Allow users to follow other users and subscribe to their boards for ongoing inspiration.

• Like and Comment: Enable users to engage with content by liking and commenting on pins.

• Share Pins: Provide options for users to share pins via email, social media, or direct messaging.

• Notifications: Implement notifications to alert users of new likes, comments, or follows on their pins or boards.

• Profile Management: Allow users to edit their profile information, including their bio, profile picture, and account settings.

• Report Content: Enable users to report inappropriate or offensive content for moderation.

• Welcome Email: Automatically send a welcome email to users upon successful registration or first sign-in with Google Account.

### Architecture
Technologies used:

• Language: Python

• Frontend: HTML, CSS

• Backend: Django

• Database: AzureDB

• Authentication: Google OAuth2

• Image Storage: none yet

• Deployment: Azure

• Design: Figma

## Getting started
  1. Clone the repository: 

```git clone https://github.com/yourusername/inspira.git```

  2. Navigate to the project directory:

```cd inspira```

  3. Create and activate a virtual environment (optional but recommended):

```python3 -m venv env          # Create a virtual environment```

```source env/bin/activate      # Activate the virtual environment```

  4. Install Django and other dependencies:

```pip install -r requirements.txt```

  5. Run database migrations:

```python manage.py migrate```

  6. Create a superuser (admin account) (optional):

```python manage.py createsuperuser```

  7. Start the development server:

```python manage.py runserver```

## Contacts
For any inquiries or feedback, feel free to contact the author (Victoria Yatsiuk) via:

• Telegram: https://t.me/kepskomeni

• E-mail: privateaccvictoria@gmail.com

## Contributing
Contributions are welcome! If you'd like to contribute to Inspira, please fork the repository and submit a pull request. Make sure to follow the existing code style and conventions.

## Project task decomposition

### Development Plan on a Weekly Basis:

Week 1:
- Implement feature: User Registration ✔️(?)
- Set up Azure cloud environment ✔️
- Create public GitHub repository ✔️
- Define project architecture and infrastructure ✔️(?)
- Draft Getting Started documentation ✔️

Week 2:
- Implement feature: Create Boards
- Configure Continuous Integration/Continuous Delivery pipeline
- Write unit tests for user registration functionality
- Document project tasks decomposition ✔️(?)
- Review and finalize architecture diagram

Week 3:
- Implement feature: Search Functionality
- Integrate SQL database with Entity Framework
- Develop infrastructure diagram
- Write unit tests for board creation
- Update project documentation with progress

Week 4:
- Implement feature: Pinning Images/Videos
- Integrate OAuth 2.0 authorization with Google account
- Set up Swagger UI for API documentation
- Create Postman collection for testing endpoints
- Write unit tests for pinning functionality

Week 5:
- Implement feature: Explore Feed
- Integrate open API for additional functionality
- Configure additional Azure service (e.g., Storage Account)
- Review and update README.md with getting started documentation
- Conduct initial round of user acceptance testing

Week 6:
- Implement feature: Follow Other Users
- Develop welcome email functionality
- Configure email service for sending notifications
- Write unit tests for user follow functionality
- Update project documentation with integration details

Week 7:
- Implement feature: Like and Comment
- Configure Service Bus for asynchronous messaging
- Develop notification system for likes and comments
- Write unit tests for liking and commenting
- Review and update documentation with notification setup

Week 8:
- Implement feature: Share Pins
- Test email notifications and sharing functionality
- Conduct performance testing on Azure environment
- Write unit tests for pin sharing
- Update README.md with deployment instructions

Week 9:
- Implement feature: Notifications
- Conduct security testing and vulnerability assessment
- Optimize database queries for improved performance
- Write unit tests for notification system
- Update project documentation with security measures

Week 10:
- Implement feature: Profile Management
- Conduct comprehensive end-to-end testing
- Address any outstanding bugs or issues
- Write unit tests for profile management functionality
- Review and finalize project documentation

Week 11:
- Implement feature: Report Content
- Perform final deployment to Azure
- Conduct user acceptance testing on live environment
- Document any post-deployment tasks or configurations
- Update README.md with final project status and acknowledgments

Week 12:
- Conduct project retrospective meeting
- Gather feedback from stakeholders and users
- Update documentation with lessons learned and future recommendations
- Finalize project closure tasks
- Celebrate successful project completion




