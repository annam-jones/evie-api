# Evie Project 

This was my final project on the course, the requirements were a full stack solo project with a 1 week deadline. 

## Brief 

- Build a full-stack application - by making your own backend and your own front-end.
- Use a Python Django API using Django REST Framework to serve your data from an SQL database.
- Consume your API with a separate front-end built with React.
- Create a MERN app & ensure there is CRUD functionality.
- Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut.
- Have a visually impressive design.
- Be deployed online so it's publicly accessible.

## Technologies 

### Frontend
- React
- JSX
- CSS
- Axios

### Backend 
- Python
- Django

### Dev Tools 
- Git
- GitHub

## Deployed Link 
https://evie-events.netlify.app/

## Process and Diagrams 

I used an ERD diagram to display the model relationships for my backend. 
![Screenshot_2025-02-26_at_11 20 09](https://github.com/user-attachments/assets/01ad3941-e1fc-4be4-843c-107c00d6944a)

I created wireframes to help me visualize how I wanted my app to look. 
![Untitled-2024-12-12-1611](https://github.com/user-attachments/assets/252cc87b-942c-447e-97f6-c2cb216d4e2b)

Routing Table 
![Screenshot_2025-02-26_at_11 18 43](https://github.com/user-attachments/assets/2144e9d4-52e7-4aff-87b4-e71f3bec6ff2)

## Code 

### Backend Snippets 
<img width="821" alt="Screenshot 2025-03-24 at 11 20 45" src="https://github.com/user-attachments/assets/4d70cc49-93f1-4060-895f-bb0cf250a013" />

This code defines a Django model called Event that represents events in an application. It inherits from Django's Model class and includes various fields such as title, description, date, location, and category. The model implements a category choice system with options like Technology, Outdoors, Music, etc. It also establishes relationships with the User model through ForeignKey and ManyToManyField to track who created the event and who's attending. The __str__ method returns the event title for string representation.

<img width="695" alt="Screenshot 2025-03-24 at 11 25 41" src="https://github.com/user-attachments/assets/7b714d79-76a5-4b74-bc82-755bb7ba566e" />

This code defines a Django REST Framework view called RegisterView that handles user registration. In the post method, it deserializes and validates incoming user data using UserSerializer. If valid, it saves the new user and generates a JWT token containing the user's ID, email, and an expiration date (set to 1 day from creation). The token is encoded using the HS256 algorithm with the application's secret key. The view returns a success response with user data and the token if registration succeeds, or an error response if validation fails. The User variable at the bottom references a custom user model.

### Frontend Snippets 

<img width="565" alt="Screenshot 2025-03-24 at 11 26 34" src="https://github.com/user-attachments/assets/4078060e-8588-4a0c-a810-81fce77205f0" />

This React component creates a navigation menu with authentication awareness. It accesses user context, manages menu state with useState, and provides a signOut function that clears credentials and redirects home. The rendered navbar shows a Home link to everyone, while conditionally displaying an Events link only to authenticated users. Navigation links automatically close the mobile menu when clicked.


<img width="541" alt="Screenshot 2025-03-24 at 11 28 56" src="https://github.com/user-attachments/assets/b4179345-5f68-4304-b19b-cff01c111e0e" />

This code exports three asynchronous functions for event management: eventCreate, eventUpdate, and eventDelete. Each function uses an apiClient to communicate with a backend service, implementing CRUD operations for events. The eventCreate function posts form data to create a new event, eventUpdate uses the PUT method to modify an existing event by ID, and eventDelete removes an event using the DELETE method. All functions include error handling through a common handleApiError utility, returning either the successful response data or processed error information.

## Screenshots of the App
<img width="1442" alt="Homepage_Evie" src="https://github.com/user-attachments/assets/f1d12cfc-714c-41e4-ba0b-ee858731a7ce" />
<img width="1442" alt="Index_Evie" src="https://github.com/user-attachments/assets/5e196d24-9ca7-42f9-8ba0-e3d706cedb3d" />
<img width="1384" alt="Create_Evie" src="https://github.com/user-attachments/assets/bd922709-909a-4198-a352-9daa2979541b" />
<img width="1426" alt="Modal_Evie" src="https://github.com/user-attachments/assets/610bf1e5-2aa3-4c89-889c-98dc8d341868" />

## Challenges 

- Implementing secure JWT authentication while maintaining a smooth user experience across protected and public routes
- Managing complex state between event creation, attendance tracking, and user profiles
- Building a responsive UI that works seamlessly across mobile, tablet, and desktop devices
- Handling image uploads and storage for event photos with proper validation and optimization
- Creating an intuitive date/time picker that handles time zones correctly for event scheduling
- Implementing efficient filtering and search capabilities to help users discover relevant events

## Future Improvements

- Implement real-time notifications for event updates, new attendees, and reminders using WebSockets
- Add interactive maps integration for easier location discovery and directions to events
- Develop a recommendation engine that suggests relevant events based on user preferences and past attendance

