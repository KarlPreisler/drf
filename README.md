# Food Lovers API (Django REST Framework)

This API is developed for the Food Lovers frontend social media web app and is powered by Django REST Framework. 
The Link to the frontend resository can be found here: https://github.com/KarlPreisler/foodlovers


Food Lovers offers a platform where users can create an account, post their own recipes or interract with other users by commenting or liking their recipes. 
Users can also follow each other on the platform, keeping them up to date with their favorite chef's latest recipes.

The website is fully responsive, providing users with the possibility of accessing the website on desktop, tablet or phone.

![Screenshot 2023-03-17 195122](https://user-images.githubusercontent.com/114813115/225993002-d2844e5b-5e32-4730-a0b2-842944de1226.png)

## Index - Table of Contents

* [Project Goals](#project-goals)
* [User Experience](#user-experience-(UX))
* [Wireframes](#wireframes)
* [Features](#features)
* [Languages](#languages)
* [Programs, libraries, frameworks, dependencies and media](#programs,libraries,frameworks,dependencies-and-media)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Acknowledgements](#acknowledgements)

Link to deployed project: https://foodlover.herokuapp.com/

The API for this frontend application was build with the Django REST Framework. 

The respository for the backend API can be found [here](https://github.com/KarlPreisler/drf)

Link to the deployed API can be found [here](https://food-lovers.herokuapp.com/)

## Project Goals

The objective of this project was to create a website application that provides a positive user experience while allowing users to share their recipes and interract with other users. The website includes the following features:

- Basic authentication and authorization functionality.
- Intuitive navigation system for positive UX.
- Full CRUD functionality that enables users to share their own recipes, read other users recipes, and update or delete their own recipes, comments, likes, and follow functionality.
- Filter options that allow users to sort through recipes by the ones that they have liked and recipes posted by followed users. Filter options to search for specific titles, authors or ingredients is also available.
- Capability to modify profile information such as bio text and images.


## User Experience (UX)

**User Stories**: 

User stories are being tracked using GitHub Projects. All User Stories have been divided into Acceptance Criteria and Tasks. 

### Wireframes
When designing the layout of the website I created Wireframes for the landing page and home page:



## Features

### Navigation bar
  - The navigation bar features a Logo the left, that acts as a link to the home page. The navigation bar has a consistent placement on each page making the website easy to navigate. The navigation bar is responsive, logo size, text and icons adapts to different screen sizes.
The navigation bar features links to the Home, Sign in and Sign up pages. If the user is logged in however, the navigation bar will include links to the following pages: Add recipe, Home, Feed, Liked, Followed and Profile.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.w3schools.com/js/js_es6.asp)
  - [JSX](https://reactjs.org/)

## Programs, libraries, frameworks, dependencies and media

- [Gitpod](https://gitpod.io)
  - Gitpod as the main IDE.
- [Git](https://git-scm.com/)
  - Git for version control.
- [GitHub](https://github.com/)
  - GitHub to store the project.
- [Code Institute's Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as the starting workspace template for this project.
- [Code Institute's README Template](https://github.com/Code-Institute-Solutions/readme-template) was used to structure this README.
- [React](https://reactjs.org/)
  - React as a JavaScript library for building the user interface.
- [Axios](https://axios-http.com/docs/intro)
  - Axios to make HTTP requests and handle the responses efficiently.
- [React Router](https://v5.reactrouter.com/web/guides/quick-start)
  - React Router for routing and navigation in this React application, allowing me to create declarative, dynamic routes with components for different pages and URLs.
- [JWT](https://jwt.io/)
  - JWT (JSON Web Tokens) was used for authentication and authorization of the web application.
- [React-Bootstrap](https://react-bootstrap.github.io/)
  - React-Bootstrap React-Bootstrap for styling and responsiveness.
- [Heroku](https://id.heroku.com/login)
  - Heroku to host both of the frontend and backend applications.
- [Google Fonts](https://fonts.google.com/)
  - Google fonts for importing Roboto font.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome for icons.
- [ui.dev](https://ui.dev/amiresponsive)
  -Ui.dev to test the responsiveness of the application.
- [Looka](https://looka.com/) was used to create a custom logo.
- [W3C Markup Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- An [ESLint](https://eslint.org/)

## Testing

Automatic tests for the navbar component: 


### Manual testing:
- I have tested that this website works appropriately in the following browsers: Chrome, Firefox and Safari.
- I have made sure that all authorization and authentication functionality is working as intended.
- I have created the website using the principles of UX and made sure that it functions the way it should on all standard devices using the devtools device toolbar.
- I have confirmed that all components are legible in terms of positioning and readability, and work as intended.
- No elements are distracted by background-colors, and no images are stretched when viewed on different devices.
- I have made sure that all functionality work properly and the website works as intended.
- I have made sure that all buttons functionality is working.
- I have made sure that the website is responsive to all devices, using react-bootstrap and CSS to make website adapt to different screen sizes.

### Lighthouse Testing 
I tested the landing page using DevTools Lighthouse test, this is the report I received.

![Screenshot 2023-03-17 185951](https://user-images.githubusercontent.com/114813115/225982862-962cdc06-7fa5-4dd0-a81d-590583f16fe2.png)


### HTML Validator 

- I validated the HTML of the landing page through the View Source functionality, since the code is using non HTML elements that won't be visible when at the source-view. I received errors because my img elements did not have any alt attribute, after adding that I received no errors. 

### CSS Validator 

- The CSS was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator), all code passed without warnings or errors.

## Bugs
- I ran into multiple bugs while creating this project. 

## Deployment

### Local Deployment

To preview the project in the development environment, run the following command in the terminal:
```npm start```. This will open port 3000. Click *Open Browser* when the popup window appears.


### Heroku deployment
This project is run using [Heroku](https://www.heroku.com), a cloud based platform that enables developers to build and run applications.
Here is the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-cli) for the most recent installation instructions. 

### Instructions for Heroku deployment:

- Clone [this repository]().
- Open your IDE and connect to your repository.
- Enter this command in the terminal:

        npm install

- Make sure your package.json dependencies look like this:

      "dependencies": {
        "@testing-library/jest-dom": "^5.16.4",
        "@testing-library/react": "^11.2.7",
        "@testing-library/user-event": "^13.5.0",
        "axios": "^0.27.2",
        "bootstrap": "^4.6.0",
        "jwt-decode": "^3.1.2",
        "react": "^17.0.2",
        "react-bootstrap": "^1.6.3",
        "react-dom": "^17.0.2",
        "react-infinite-scroll-component": "^6.1.0",
        "react-router-dom": "^5.3.0",
        "react-scripts": "5.0.1",
        "web-vitals": "^2.1.4"
      },

3.  Git add, commit and push all changes to your repository.
4.  Create or log in to an account on Heroku.
5.  Create a new app on Heroku.
6.  In the Deploy section on Heroku, go to Deployment method and connect to your GitHub repository.
7.  Go down to Manual deploy and select deploy branch.
8.  To run your app locally, you can enter this command in your terminal:

            npm run dev

## Acknowledgements
- Special thanks to my mentor Spencer for guidance throughout the project. With everything from styling and layout, to the functionality and logic of the project.
