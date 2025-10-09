# Hortus Cognitor

A Django website for courses about growing real change with the land.

## 🚀 Live Deployment

- **Live Website**: https://hortuscognitor.onrender.com/
- **Admin Panel**: https://hortuscognitor.onrender.com/admin/
- **GitHub Repository**: https://github.com/JoninShinobi/hortuscognitor

## 🛠️ Local Development Setup

### 1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### 3. **Run migrations:**
```bash
python manage.py migrate
```

### 4. **Load sample data:**
```bash
python manage.py load_sample_data
```

### 5. **Create superuser (for admin access):**
```bash
python manage.py createsuperuser
```

### 6. **Run the development server:**
```bash
source venv/bin/activate
python manage.py runserver
```

### 7. **Access the local website:**
- Main site: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

## 🔄 Deployment & Updates

### Making Changes and Deploying

1. **Make your changes locally**
2. **Test changes:**
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```
3. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
4. **Render automatically deploys** from the main branch

### Production Admin Access

To create an admin user on the live site:

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click on "hortuscognitor" service
3. Click the **"Shell"** tab
4. Run: `python manage.py create_admin`
5. Login at https://hortuscognitor.onrender.com/admin/ with:
   - **Username:** admin
   - **Password:** change_this_password_123
6. **⚠️ Change password immediately after first login!**

### Environment Configuration

**Production settings are configured via environment variables on Render:**
- `DEBUG=False`
- `ALLOWED_HOSTS=hortuscognitor.onrender.com`
- `DJANGO_SECRET_KEY=[secure-key]`

## 📁 Project Structure

```
hortus_cognitor/
├── courses/                    # Main Django app
│   ├── models.py              # Course, Instructor, Booking models
│   ├── views.py               # Page views and logic
│   ├── admin.py               # Django admin configuration
│   └── management/commands/   # Custom management commands
│       ├── load_sample_data.py
│       └── create_admin.py
├── templates/                 # HTML templates
│   ├── base.html             # Base template with navigation
│   ├── home.html             # Homepage
│   ├── courses/              # Course-related templates
│   └── admin/                # Custom admin templates
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── styles.css        # Main website styles
│   │   └── unfold_custom.css # Admin panel custom styles
│   └── images/               # Website images and logos
├── hortus_cognitor/          # Django project settings
│   ├── settings.py           # Main configuration
│   ├── urls.py               # URL routing
│   └── wsgi.py               # Production server config
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment config
└── vercel.json              # Vercel routing config
```

## ✨ Features

- **Course Management**: Create and manage land-based transformation courses
- **Instructor Profiles**: Detailed instructor biographies and photos
- **Responsive Design**: Mobile-optimized with burger menu navigation
- **Admin Interface**: Django Unfold admin theme with custom styling
- **Booking System**: Course registration and participant management
- **SEO Optimized**: Clean URLs and meta tags

## 🎨 Design System

### Fonts
- **Primary Font**: Hey Eloise (loaded via Adobe Fonts)
- **Fallback Fonts**: Kalam, Patrick Hand, Caveat, cursive
- **Body Text**: Georgia serif

### Colors
- **Primary Gold**: `#ADA228`
- **Hover Gold**: `#969020`
- **White**: `#FFFFFF`
- **Dark Background**: `#1a1a1a`
- **Text Dark**: `#333`

### Key Design Elements
- **Logo**: CARROTFIST (white version for dark backgrounds)
- **Hero Images**: Full-width background images with overlay text
- **Course Cards**: Clean white cards with subtle shadows
- **Mobile Menu**: Hamburger-style navigation for mobile devices

## 🔧 Key Management Commands

```bash
# Load sample course data
python manage.py load_sample_data

# Create admin user (production)
python manage.py create_admin

# Collect static files
python manage.py collectstatic

# Run database migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations
```

## 🌐 Architecture

**Frontend**: Django templates with custom CSS
**Backend**: Django with SQLite database
**Hosting**: Render (backend) + Vercel (routing)
**Static Files**: Served via WhiteNoise middleware
**Admin**: Django Unfold theme with custom styling

## 📝 Content Management

Use the admin panel to:
- **Add/Edit Courses**: Manage course details, dates, pricing
- **Manage Instructors**: Update instructor profiles and photos
- **View Bookings**: Monitor course registrations
- **Update Content**: Modify course descriptions and details

## 🚨 Important Notes

- All pushes to `main` branch automatically deploy to production
- Static files are automatically collected during deployment
- Database uses SQLite (suitable for small-scale applications)
- Admin styling fixes are in `static/css/unfold_custom.css`
- Course descriptions in sample data can be modified via admin panel

## 📞 Support

For technical issues or questions about the codebase, refer to the Django documentation or check the project's commit history for recent changes.