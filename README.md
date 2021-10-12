<h1 align="center">The Backlog site</h1>

[View the live project here.](http://backlog-gamesite.herokuapp.com/)

On this site you will be able to keep track on your gaming, add the games you haven't played yet, or start reviewing the games you have played, share your thoughts about the games. Register an account and start adding to your own backlog. 

<h2 align="center"><img src="static/img/img-readme/amIResponsive.png"></h2>

---

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. I would like to get a clear instructions on what the site is about, what I can do. 
        2. I would like to easily navigate my way through the site.  
        3. I want the registration process to be smooth and availible. 

    -   #### Frequent User Goals
        1. I would like the login process to be a button click away. 
        2. I want to add new games to my backlog easily, maybe add multiple games at once. 
        3. I want to review my finshed game, and let others see my reviews. 
        4. I would like to search for a specific game review, to see other users thought on that game.
        5. I would want to add pictures to my review.  
        6. I want to see other users backlog. 
        7. I would like to know where I could purchase a copy of a game.

---

- ### Strategy
    - This site focuses on the gamers, one of the larges growing community in the world. During this recent pandemic, lots of gaming companies has delayed there games. So there hasn't been to many new games released. So by shortage of something to play, I started my backlog. With just pen and paper. I looked at the games I missed or didn't have time to finish and started to write them down. So the reason for this website is for you to keep better track on your own perosnal backlog. Just add your games to your list. And when you are done, you can leave a short review of your experience, for other users to see.

---

- ### Scope
    
    - So the users of this site should be able to create an account, add to there own backlog, review there finished games & look on other users reviews and backlogs. More features will be to add a link to where you can buy the games. 

---

- ### Structure
- Navbar
    - At the top of the page I will have a navbar so you can easily navigate around the site. 
    - On smaller devices the navbar links will collapse into a toggler menu. With a button to reveal the links in a good looking [sidenav](static/img/img-readme/mobileSidenav.png).
- Home
    - At first you will see the page header, A short description on what the site is about, and then you can choose to Register an account or Log in. 
- Review Page
    - At the review page you will see other users reviews as well as our own, displaying from newest to oldest post. 
    - 
- My page
    - At this page you will store your backlog in a list. 
    - Also displayed in a list would be yor finished games.
    - Underneath those lists you can see your own reviews, in an order from newest to oldest.
    - When you are done with a game, review the game and it will be for everybody to see at this page. Viewing the newest to oldest reviews.
    - The reviews will be stored in mongoDB.
- Register
    - A easily understanable register page, centered in the middle of the page. Come up with a nickname, enter a password, and you are ready to start your backlog. 
- Log In
    - Will have the same estetics as the register page. 
    - Just enter your nickname and password and your are good to go. Will have simular styling as the register page. 
- Add to Backlog
    - Will have the same estetics as the register page.
    - At this page you will add games to your backlog.
    - You type in the name of your game, and it will be stores in your backlog.
    - The backlog will be stored in mongoDB.

---

- ### Skeleton
    *   ### Wireframes
    - Desktop
        - [Home Page](static/img/img-readme/home.png)
        - [My Page](static/img/img-readme/myPage.png)
        - [Reviews](static/img/img-readme/reviews.png)
        - [Register](static/img/img-readme/signUp.png)
    - Mobile
        - [Home](static/img/img-readme/mobileHome.png)
        - [Sidenav](static/img/img-readme/mobileSidenav.png)
        - [Register](static/img/img-readme/mobileSign.png)
        - [Review](static/img/img-readme/mobileReview.png)
        - [My page](static/img/img-readme/mobileMy.png)
        - [Log in](static/img/img-readme/mobileLog.png)
        - [Add](static/img/img-readme/mobileAdd.png)

---

- ### Surface

-   ### Design
    -   #### Colour Scheme
    -   #### Typography
    -   #### Imagery

---

## Features

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

- [jQuery](https://jquery.com/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [PyMongo](https://pypi.org/project/pymongo/)

- [Materialize](https://materializecss.com/)

- [BSON](https://bsonspec.org/)

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

- [Heroku]()

- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

- [FontAwesome](https://fontawesome.com/) - provides icons across the site

- [GoogleFonts](https://fonts.google.com/) - Fonts

- [Git](https://git-scm.com/) - Git was used for version control.

- [GitHub](https://github.com/) - GitHub was used to store the project.

- [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create the wireframes.

- [Am I Responsive](http://ami.responsivedesign.is/#) - Tested responsivness & the images at the top of the readMe.

- [Color Hex](https://www.color-hex.com/) - The color images wich are displayed at the [**Design**](#design) section of this readMe.

- [Amp What](https://www.amp-what.com/) - At the footer, and sidenav.  

## Testing

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

-   [Pep8online](static/img/img-readme/pep8onlinevalid.png) - Validation for Python code. 

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

-   #### Returning Visitor Goals

-   #### Frequent User Goals



### Further Testing


### Known Bugs

- So the first bug i've encounterd was when opening the sidenav on mobile view, at the users profile page. The pacman image looked like [this](static/img/img-readme/bug01.png). Only the alt text is showing. Now in late develepment I also used the pacman images as the navbrand and encountered the same problem, the navbrand image and the sidenav images dosen't show at the profile page, fullreview page, when you edit your backlog or when your about to write a review or edit your review. The difference between these pages are that these pages has an argument passed through the URL. The profile page has username, edit-backlog has backlog_id, fullreview has review_id and edit-review also has review_id pas through as an argumenet. Solved it by changing the src to the images address instead of the img folder in my static files. 

- Another bug I've encountered is at the edit-review page, I've preloaded the image field with it's current [value](static/img/img-readme/bug03.png), but if I don't load the same or a new images I get an error. ["Missing required parameter - file"](static/img/img-readme/bug02.png).



## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

### Content



### Media

### Acknowledgements
