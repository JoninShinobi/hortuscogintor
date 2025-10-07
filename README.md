# Hortus Cognitor

A Django website for courses about growing real change with the land.

## Setup Instructions

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Load sample data:**
   ```bash
   python manage.py load_sample_data
   ```

5. **Create superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   ./run_server.sh
   # Or manually:
   python manage.py runserver 8080
   ```

7. **Access the website:**
   - Main site: http://127.0.0.1:8080
   - Admin panel: http://127.0.0.1:8080/admin

## Project Structure

- **courses/**: Main Django app containing models, views, and templates for courses
- **templates/**: HTML templates for the website
- **static/**: Static files (CSS, JavaScript, images)
- **media/**: User-uploaded content (instructor photos, etc.)

## Features

- Course listing and detail pages
- Booking system for courses
- Instructor profiles
- Responsive design with custom styling
- Admin panel for content management

## Design

- **Primary Font**: Hey Eloise (Note: Font files need to be added to static/fonts/)
- **Primary Colors**: 
  - #ADA228 (Gold/Yellow)
  - #FFFFFF (White)
  
## Logo

The project uses the Hortus Cognitor logo (CARROTFIST) available in both black and white versions.