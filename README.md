1. **Project Setup Guide**
   - This guide will walk you through setting up and running the Flask project. Ensure you follow each step carefully to get the project running smoothly.

2. **Before you begin, make sure you have the following installed:**
   - Python (with pip)
   - MySQL Server
   - Flask
   - A text editor or IDE that supports Python development (e.g., VS Code, PyCharm).

3. **Setup Instructions**
   - Clone this repository to your local machine:
     ```
     git clone https://github.com/Ochan-LOKIDORMOI/Junub_website
     ```
   - Navigate to the project directory in your terminal:
     ```
     cd Jununb_website
     ```
   - Install Dependencies:
     ```
     pip install Flask mysql-connector-python
     ```

4. **Database Configuration:**
   - Install MySQL server on your computer if you haven't already done so.
   - Ensure your MySQL server is up and running.
   - Create a database and name it according to your choice.
   - Modify the `app.py` file to match your MySQL database configuration:
     ```python
     db = mysql.connector.connect(
         host="localhost",
         user="your_mysql_username",
         password="your_mysql_password",
         database="Your_database_name"
     )
     ```
     **NB:** Replace `your_mysql_username` and `your_mysql_password` with your MySQL username and password.

5. **Run the Application**
   - Run `./app.py` to start the application.
   - Open your web browser and navigate to http://localhost:5500/ to access the application.

6. **Usage**
   - Register/login to the application and explore the various functionalities available.
   - Ensure to test each feature thoroughly to ensure proper functionality.

7. **Important Notes**
   - Make sure your MySQL server is running before running the application.
   - Avoid using sensitive information like passwords directly in code for production applications. Consider using environment variables or secure storage mechanisms.

8. **Support**
   - For any issues or inquiries, please contact:
     - Email: o.lokidormo@alustudent.com
     - Contact: +211929333208

9. **Contributor**
   - Ochan-LOKIDORMOI
