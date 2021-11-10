# Wild Indigos E-commerce Store

![Live Project]()

[Live Site](https://herokuapp.com/)

## Milestone Project 4

# UX <a name="ux"></a>

## Strategy <a name="strategy"></a>

* I created this site as a way for my daughter to sell her bracelets online and for myself to begin the process of building a like-minded community through wellness. This site will be tailored to suit all of ur customer's needs.

* This project was built to showcase my abilites in designing and developing a full-stack web application using the django web framework, HTML, CSS, Javascript and Python.

* The website I have built is a full stack ecommerce web application for a company that my daughter and I created called Wild Indigos. I built a basic front-end website for Wild Indigos for my MS1 but with my skills advancing, I decided to remake the website and add all of the commerce features.

* The application I have developed uses E-commerce functionality, payments are made using Stripe, a blog section for customers to use to create SEO friendly blog posts to increase  organic traffic to the site and a comments section for users to add comments for interactivity with the store and leave comments on blog posts, Only registered users can leave comments and leave reviews, review section so that users can voice their own opinion on specific products, Confirmation emails, CRUD functionality for admin users to add, update and delete products reviews and blog posts, comments, CRUD functionality for users to create read update and delete their own reviews in the reviews section and the ability to delete comments they have left on blog posts, admin have authorisation to do anything on the site.

* For the assessor, the admin login details have been included in the comments section when submitting the project.

* Please note that this website is solely for educational purposes so Please don't attempt to enter real credit card details when using the stripe functionality. use the below details for testing purposes.

    * stripe card number: 4242 4242 4242 4242
    * Any card end date you wish
    * Anyy CVV number you wish


# Table of contents

1. [UX](#ux)

    * [strategy](#strategy)
        * [user stories](#user-stories)
        * [site goals](#site-goals)
    
    * [scope](#scope)
        * [features](#features)
    
    * [structure](#structure)

    * [skeleton](#skeleton)
        * [wireframes](#wireframes)
        * [Database](#database)
    
    * [surface](#surface)

2. [Technologies Used](#technologies-used)

3. [Testing](#testing)

4. [Deployment](#deployment)

5. [Credits](#credits)

### User Stories <a name="user-stories"></a>

* I want to be able to quickly view the products that the site is selling.

* I want to be able to easily navigate throughout the site.

* I want to be able to find out more information about the company and see if they have a social media presence.

* I want to be able to contact the company.

* I would like to be able to search for a specific item using the search bar.

* I want to be able to search the site based on the different categories.

* I want to be able to see all product details before I choose to buy the item

* I want to be able to sort the items based on their price.

* I want to be able to see products price and sizes if they have any.

* I want to be able to add items to my shopping bag

* I would like to be notified when I add items to bag or interact with the site functionality.

* I want to be able to edit my shopping bag.

* I want the checkout process to be quick and painless.

* I want to be able to leave a review of certain products.

* I want to receive confirmation of my order.

* I want to be able to see previous order details.

* I want my details tto be saved to my account for faster purchases in future.

### Site Goals <a name="site-goals"></a>

* I want to be able to add, edit and delete products, blog posts and the ability to delete comments from blog posts easily.

* I want to be able to increase organic visitors to the site using SEO friendly blog posts.

* I want an admin section of the site and to make administration tasks simpler.

* I want customers to have a relaxed and trouble free time on the site.

* I want the site to be fully mobile responsive.

## Scope <a name="scope></a>

## Design

### Scope and Structure

**Scope**

* Responsive Design 
* Informative Landing Page
* Sticky top Nav Bar & Mobile Nav Bar 
* Relational database to store all uploaded data/content
* CRUD functionality at varying levels for profiles and products
* Authentication functionality
* Profile page
* Search functionality
* Contact functionality
*  list functionality
* E-Commerce functionality

**Skeleton Structure**

This application will be made up of multiple pages derived or based around 6 data models, product, cart, checkout, user profile, contact form and favorites.

The landing page will consist of a large hero image with a text introduction of the site's offering or purpose.

Login, registration, add/edit products/profile and contact pages will all consist of forms with varying inputs dependant on the purpose of the form.

The profile page will display user information derived from the form and past orders .

The favorite products page will display favorited items with options to remove them or view the product in detail.

The products page will display all products and can be sorted or filtered.

The product detail page will display the image and details with an option to purchase, favorite or update/delete for the admin user.

**Interaction Design**

The nav bar items will highlight on hover.

The user will be able to interact with the data on the application via the search bar, products will display below the search bar if found or a line of text with '0 products found' if not found. They can also filter and sort categories using a sort selector drop down.

All forms will validate and change colour/display messages to notify the user of errors.

Delete features will trigger warning modals and require confirmation before the action runs.

Successful actions and unsuccessful actions will be flagged with django messages to the user.

Authentication processes, placed orders and contact form submission will trigger emails sent to the users email address provided.

### Wireframes
A mock-up of how the site will be laid out is available here via [Wire Frames]().

### Database Structure

![Database Structure]()

#### Data Models

###### Product & Categories

- The product model creates objects containing individual product information, such as name, description, price, image and sku. 
- The unique ID is auto generated. 
- The product objects will be used for the order model and favorites model.
- The product model is lonked to the categories model which divides the products into subsections.

##### User Profile & User

- The User model is created by django All Auth on registration, it stores the name, email and password of a user.
- The User Profile model creates and instance of the user information in the database, similar to above as an object. 
- The User Profile is linked to the User model. 
- The user Profile stores shipping and contact information.

##### Order Model & Order Line Item

- The order model is connected to the user profile, feeding in the shipping and contact information. 
- The order model creates an instance of an order on the data base with billing information, date and time of placement and by whom. 
- The order model is linked to the Order Line Item model which holds the product information for the order placed.
- The Order Line Item model is linked to products.

##### Favorites and favorited Items
- The favorites creates a 'container' for users to store favorited products. 
- The favorited items model creates instances of these favorite products in the container.
- This model is linked to the user and to the poduct model.

##### Contact
- The contact model stores users queries in the backend for the admin user to view.

### Security

Sensitive data such as SECRET_KEYS were stored on heroku using config variables to prevent unwanted connections to the database.

Django allauth was used to set up user authentication and built in decorators allowed restricted access to certain features on the website.

### Color Scheme

![Canva](canva.com)

The above color swatch shows a guideline for the color scheme of the site.

Colors are brand colors that have been adopted for their strong visual contrast in an attempt to make all content as easily consumable and suitable for visually impared users as possible.
* There are two main colors used throughout the project and they are listed below.
    * #61988E - this is the orchid color used in the header and footer as well as border colors fonts etc.
    * #211522- this is just your standard black that will be used as the 
    * #c197D2 - this is the off-white color used in the modal, forms, all auth etc. I wanted to have a nice easy to read white color and this was my preferred choice.
    

### Typography

[Google Fonts](https://fonts.google.com/quicksand) will be the main font for all content.  


### Imagery
