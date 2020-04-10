Enterprise Solution Development (ESD) project by G2T8

How to run The Farmers Lab Application:
1) Import all SQL Scripts in phpmyadmin (root account)

2) If you would like to set up customer microservice on docker, enter the docker folder:
	- set dbURL=mysql+mysqlconnector://root@localhost:3306/customer
	- pip install -r requirements.txt
	- docker build -t ycm98/customer:latest .
	- docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/customer ycm98/customer:latest

[Note: Our docker deployed on AWS EC2 instance has stopped working as our AWS account has ran out of credits, please refer to our presentation video for verification purposes]

2) Run the microservices in the following order:
	- (Run this if customer is not set up on docker) customer.py
	- products.py
	- order.py
	- orderdelivery.py
	- delivery.py
	- payment.py

3) Facebook API: As Facebook API only runs on HTTP, please run the application only on localhost WAMP server.

4) OneMap API would be working as per written script

5) Paypal API Testing accounts:
	- Email: cherylyong7@hotmail.com | Password: 12345678
	- Email: samquek@gmail.com | Password: 12345678
	- Email: yoongi@gmail.com | Password: cuteyoongi

6) TextMagic API: Only runs with credits left on the account, please contact Cheryl at @min2209 in Telegram for testing and verification purposes.

7) User Login: frontend/index.html
	User Accounts you can use to login:
	1) Email: samquek@gmail.com | Password: greenunicorn1!
	2) Email: sebastianng@gmail.com | Password: greenunicorn1!
	3) Email: jeffkua@gmail.com | Password: greenunicorn1!

8) Admin Login: frontend/admin/index.html
	Admin UI Login:
	Username: admin
	Password: greenunicorn1!

TextMagic API, Paypal API is linked to Cheryl's email account and Facebook API is linked to CheeYong's email account which couldn't be revealed for privacy purposes.

To know more about how to navigate through our application, please refer to our presentation video demo portion at the 4:30 mark.
Link: https://www.youtube.com/watch?v=6I0jZ6y6bOo