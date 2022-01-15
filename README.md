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

## Features

### Existing Features

1. Responsive to different screen sizes.
2. Supported by Chrome, Opera, and Firefox browsers.
3. Adapted for users with special accessibility requirements where possible.
4. There will be multiple pages: Landing page, all products page, product detail page, shopping bag, checkout page, successfull check out page, profile page, login page, sign up page, delete/edit product page, contact form page, favorites page, 404 error and 500 error page.

        - Each page will have a navigation header
        - Each page will have a footer
        - Each page will have a favicon on the browser tab

5. Each page will have a 'sticky' navbar

        - High contrast between text and background.
        - Text logo on the left, or removed on smaller screens
        - A central search bar
        - Menu options in the center or to the left on mobile
        - The logo will route back to the home page
        - Menu options will change to color on hover & envoke a pointer
        - On mobile devices, the menu items will switch to a toggle button and slide down the page when button is clicked
        - The mobile nav will not have 'on-hover' styling
        - Anon users will see my account(signup/register), search bar, shopping cart total, all products, contact page, equipment and classes page 
        - Registered users will see the above mentioned with an additional profile tab and log out option under the 'my account' nav item

 6. The home page will have:

        - A hero image.
        - Informative text.

7. The login/register page will have:

        - A form requesting user information (name, username & password) and a submission button
        - Toast messages displaying successfull/unsuccessfulsubmission of information

8. The profile page will have: 

        - An area displaying the users information
        - An area displaying orders the user has purchased
        - There will be an option to edit information
        - Toast messages displaying successfull/unsuccessful update of information

9. The all products page will have:

        - A sort by category bar
        - A section displaying existing products
        - Each product will have an image, label and a link to review its details
        - To an admin user there will be a link to edit/delete

10. The product detail page will have:

        - An image of the product
        - Descriptive text
        - Price
        - favorite icon
        - Quantity selector
        - Add to cart button
        - Go back button
        - Edit/Delete link for the admin user only
        - Toast messages displaying successfull/unsuccessful addition of products to the shopping bag

11. The shopping bag page will have:

        - Images and descriptions of products
        - Option to edit quantity or remove products
        - Grand total calculation
        - Keep shopping button
        - Continue to checkout button
        - Toast messages displaying successfull/unsuccessful removal of products

12. The check out page will have:

        - A form requesting/prepopulating order details
        - An order summary
        - A stripe payment option
        - A check box to save info to a profile
        - A grand total
        - Messages to convey successful or unsuccessful check out



13. The contact form page will have a form with fields for:

        - Name
        - Email
        - Drop down menu for the subject title
        - Text box
        - Submission button
        - Toast messages to convey successful or unsuccessful submission of the form.

14. All users interactions will either be confirmed or notified of an error either via on screen messages, orders, contact forms and profile set up will be also confirmed via email.

15. All products page and the cart page will have a scroll to top button.

## Information Architecture

### Data Storage

#### User Table

|   Title           | Key In Database                  | Form Validation   | Data Type  |
| ----------------- | -------------------------------- | ----------------- | ---------- |
| Account id        | _id                              | No Validation     | Primary Key|
| First Name        | first_name                       | max length 20     | CharField  |
| Last Name         | last_name                        | hashed min length | CharField  |
| Email             | email                            | Must have @ &.com | Email      |
| Street Address    | default_street_adress_1          | max length 120    | CharField  |
| Street Address  2 | default_street_adress_1          | max length 120    | CharField  |
| City or Town      | default_city_town                | max length 120    | CharField  |
| County/State      | default_county_state             | max length 72     | CharField  |
| Postal Code       | default_postcode_zip             | max length 120    | CharField  |
| Postal Code       | default_postcode_zip             | max length 120    | CharField  |
| Contact           |                                  |Number max         |            |
| Number            | default_phone_number         |length 20          | CharField  |
| Country           | country                          |pycountry select   | Option     |


### Products Table

|   Title           | Key In Database                  | Form Validation      | Data Type   |
| ----------------- | -------------------------------- | ----------------- | ----------  |
| Product Id        | _id                              | No Validation        | Primary Key |
| Product Name      | name                             | max length 254       | CharField   |
| Price             | price                            | max digits  6        | DecimalField|
| description       |description                       | No validation        | CharField   |
| sale_type         |sale_type                         | max length 20        | DecimalField|
| image             |image                             | Null True Blank True | ImageField  |



### Orders Table

|   Title           | Key In Database                  | Form Validation   | Data Type   |
| ----------------- | -------------------------------- | ----------------- | ----------  |
| Order Number      | order_number                     | No Validation     | Primary Key | 
| User Profile      | user_profile                     |     text          | Foreign Key |
| First Name        | first_name                       | max length 100    | CharField   |
| Last Name         | last_name                        | max length 100    | CharField   |      |
| email             | email                            | max length 120    | CharField   |
| Phone number      | phone_number                     | max length 20     | CharField   |
| Street Address  1 | default_street_adress_1          | max length 120    | CharField   |
| Street Address  2 | default_street_adress_1          | max length 120    | CharField   |
| City or Town      | default_city_town                | max length 120    | CharField   |
| County/State      | default_county_state             | max length 72     | CharField   |
| Postal Code       | default_postcode_zip             | max length 120    | CharField   |
| Country           | country                          |pycountry select   | Option      |
| Contact           |                                  |Number max         |             |
| Number            | default_telephone_number         |length 20          | CharField   |
| Order Date        | order_date                       |datetime.date.today| DateField   |
| Total Order       | total_order                      |max digits 10      | DecimalField|
| Delivery Charge   | delivery_charge                  |max digits 5       | DecimalField|
| Grand Total       | grand_total                      |max digits 10      | DecimaField |


## Technology Used

### Languages

- HTML
- CSS
- Javascript
- [Python](https://www.python.org/)

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Libraries

- [Jquery](https://jquery.com/)
- [Sweet Alert](https://sweetalert2.github.io/)
- [Stripe Payments](https://stripe.com/)
- [PopperJS](https://popper.js.org/)

### Tools

- [AWS](https://aws.amazon.com/s3/)
- [Heroku](https://www.heroku.com)
- [Git](https://git-scm.com/)
- [Postgres](https://www.postgresql.org/)



## BUGS

BUG #1

Trying to run a test function to render my webpage.

For some reason my files are upside down. I thought my Migrations folder 
along with settings and url files belonged in the top file.

I thought that my views/admin files were supposed to be under the __init__.py.(tells project manage.py is a
 directory we can import from)

I created the project directory first with the Django- admin wild_indigos command and then 

the startapp shop command.

Shouldn't the project directory be at the top?

Is that impacting my

I have tried to move the folders.

I have tried changing the name on the 


_____________

During the beginning of my testing stage, I tried to render a basic hello function. 
Initially I was getting a:

Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/
Using the URLconf defined in wild_indigos.urls, Django tried these URL patterns, in this order:

admin/
hello/ [name='hello']
The empty path didn’t match any of these.


This error was being returned because I did not have function mapped to the home url
in my root urls.py.

Django needs to define the url with an empty string. Once I removed hello from the string, the test function
properly rendered to the page

 Bug #2
On the first test run to check my index.html, an error kept returning:

'module' object is not callable.
It turns out that I had improperly imported os in the wrong file. By removing this, I was able to open my project. The project 


BUG 3
When landing page is throttled at 150% or 125% on mid-tier and low-end mobiles, the nav and footer get huge and cover the content on the hero image.


BUG 4
When wiring up my item-detail folder into urls.py, I was met whith an invalid syntax error. This error occurred because when I created the path, I forgot to add the commas at the end of both paths which led to the invalid syntax error.

This was solved by of course adding a ), to the end of the path.

Bug 5
When setting up the view for product details. I had 
Context = {
‘product’: products,
}
This returned a templating error and would not render the individual product once clicked.

This issue was solved by changing ‘products’ to ‘product’


Bug # 6

When wiring up the shopping bag app to the project, a templating error was returned that would not render the shopping cart page. This error 


Bug #7
When trying to implement the logic for adding the quantity times the price total, I receive a TypeError for an integer and a string 
Total +=

This bug was in the Product Models file. The bug was fixed by changing the price string to a DecimalField and running migrations. After the models were properly migrated, the cart was able to render the prices of the items. 

Bug # 8

Scott helped me with this one. I am using Bootstrap 5 and because of this, when I went to add the
Toasts to my project, it was not working. This was because Bootstrap 5 stopped using JQuery and are
instead using Vanilla JS. The initialization step is different.
In Bootstrap 4 the JavaScript Initialization is:
<script type=”text/javascript”>
      $(.toast).toast(‘show’);
</script>
In Bootstrap 5 it is quite different:

var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl, option)
})

Scott was able to make a loop that cycled through the toasts:
For (let x = 0; x < toastList.length;  x++) {
                               toastList[x].show();
               }
This solved the issue and my website started returning the Toast messages successfully.




## Testing

- Implementation: "I want to be able to quickly view the products sold on the site." In order to meet this user story, a button was placed directly on the landing page for an obvious link to the products. There is also a product link located on the navbar.

- TEST:







## MEDIA
Make to day amazing
https://unsplash.com/photos/DXmhzif5izc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink


3 bracelets image
https://unsplash.com/photos/md87xXz3le4?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink


Pain tincture

https://unsplash.com/photos/D6SQVDF7x_E?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

Tincture Guy
https://unsplash.com/photos/D6SQVDF7x_E?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

Bathbomb in tub
Photo by Anthony Shkraba from Pexels

Howlite
https://unsplash.com/photos/Gwhtv-14miU?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

https://unsplash.com/photos/D6SQVDF7x_E

https://unsplash.com/photos/LAOVX-PFNvI