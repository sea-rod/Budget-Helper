# 👋Introduction
Welcome to our Django to-do application's README page! You've come to the right place if you're looking for a dependable and effective budget application. The Django Budget App is a web-based budgeting application that allows users to manage their finances by adding, categorizing, and tracking their expenses. With this application, users can create their own custom categories, use default categories, and calculate their budget categorical-wise.

## Features
User authentication and authorization
Add and edit custom categories
Default categories for common expenses
Add and edit expenses for each category
View and analyze expenses by category
Generate reports to view spending patterns and budget performance

## 🏃‍♂️Installation
1. Clone the repository

``` bash
git clone https://github.com/sea-rod/Budget-Helper.git
```
2. Change the working directory
```bash
cd Budget-Helper
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
or
```bash
python -m pip insatll -r requirements.txt 
```
4. Then run the `python manage.py migrate` to make create tables in the database
```bash
python manage.py migrate
```
5. Then run the `python manage.py collectstatic` command
```bash
python manage.py collectstatic
```
6. Start the development server
```bash
python manage.py runserver
```
>Note: Do not use the this server for production

7. Open your web browser and navigate to http://127.0.0.1:8000 to use the application.

8. Thats all your good to go. Enjoy the app 💖!!

> Change the .env file according to your needs.


## Usage
### Adding a new category
#### To add a new category, follow these steps:

1. Log in to your account.
2. Click on the user profile dropdown menu in the navigation menu.
3. Click on the "Add Category" button.
4. Enter the name and budget of the new category.
5. Click on the "Confirm" button.

### Editing a category
#### To edit a category, follow these steps:

1. Log in to your account.
2. Click on the "Analytics" link in the navigation menu.
3. Click on "Update" button besides the cateogory you want to edit.
4. Update the name and budget of the category.
5. Click on the "Confirm" button.

### Adding an expense
#### To add an expense, follow these steps

1. Log in to your account.
2. Click on "+ Add Expense" box in the body (if no expense is added)  
3. Click on "+ Add Expense" button (if atleast one expense is added)
4. Enter the Cateogry and the expense value.
5. Click on the "Confirm" button.


## 🔨Built with
- [Django](https://www.djangoproject.com/): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## Contributing
Contributions to the Django Budget App are welcome! Please submit a pull request with any changes or improvements you would like to make.

## License
This project is licensed under the MIT license - see [`License`](LICENSE) file for details.