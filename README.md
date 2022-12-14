# CBA_Solution

Full Stack business logistics application driven to help business owners analyze costs vs benefits. Website functionality was designed to help businesses 
understand how much work they have taken on, and based on that amount, where they stand financially. Created application to help my dad calculate how much 
business to take in given most of his business for the year comes in during a 2 month period.

Technologies used: Python, Flask, MySQL, CSS, Bootstrap, HTML, Git, GitHub, AWS EC2

Deployed website application using AWS EC2 Instance. http://54.161.193.73/

How to use the application:                                                                                                                                         
    -First, one will need to register their business in the database. Validations will make sure business name is a certain length, email is unique in the database,     and password has a capital letter, a special character, a number, and is a certain length. After registering a business, users will be able to log in and out. Once 
  logged in, the user will need to add all the services that the business offers. If a service needs to be updated later, user can edit any service along with deleted 
  them. Once business' services are added, orders can be added inputing custer name, choosing which service they want, the date ordered, and any notes regarding the 
  order. With each order added, edited, or deleted, the categories on the dashboard will update. By adding services with price and costs and then adding orders for 
  services, the application calculates gross income, net income, business costs, hours/days worked, and total amount of orders.

Functionality:                                                                                                                                                      
● Login and Registration with form validations for users.                                                                                                           
● Application allows users to create, read, update, and delete services and orders.                                                                                  
● Integrated access control by securing passwords with Bcrypt and using Session to secure user-based functionality on web pages.                                      
● Implemented a responsive and scalable application using Bootstrap and inline CSS to improve functionality across platforms.                                       
● Based on the accounts services data, business specific logistics for gross and net income, business' cost, work hours, and total orders are updated with            
  each new order. Also, all logistics update with each order deletion.                                                                                                
● Accessible anywhere given AWS deployment.

**Video Walk-Through:**
https://www.youtube.com/watch?v=QWEowwjevWk

![image](https://user-images.githubusercontent.com/98436247/193896081-01ac1998-bb2c-4bd6-90ea-8cb272f0dd1c.png)
![image](https://user-images.githubusercontent.com/98436247/193896836-e71c00af-12fe-4d23-a3be-c7566c257fdb.png)
![image](https://user-images.githubusercontent.com/98436247/193897700-60e3be16-f81b-4fac-a6b2-a56b23c0c218.png)
![image](https://user-images.githubusercontent.com/98436247/193897809-dd35e780-a844-4269-ad7a-af3fc7a51263.png)
![image](https://user-images.githubusercontent.com/98436247/193897887-1c443543-7f7f-4eba-87dd-5057290e9aec.png)
![image](https://user-images.githubusercontent.com/98436247/193897984-d31ab629-8cec-45a8-b6cc-7715a4997c6a.png)













