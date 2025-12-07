# Django Blog Project

## Overview

This Django project is a simple blog application that allows users to **create, read, update, and delete (CRUD) blog posts**. Authenticated users can manage their own posts, while all visitors can browse blog posts.

All CRUD operations are implemented using **Django Class-Based Views (CBVs)**, with proper permission handling using `LoginRequiredMixin` and `UserPassesTestMixin`.

---

## Features

- **User Authentication**
  - Register, Login, Logout
  - Profile update for authenticated users
- **Blog Post Management (CRUD)**
  - Create new posts (authenticated users only)
  - Read/list all posts (public)
  - View post details (public)
  - Update posts (only by the author)
  - Delete posts (only by the author)
- **Slug-based URLs** for SEO-friendly links
- **Flash messages** for success/failure notifications

---

## URL Patterns

| URL | View | Permissions |
|-----|------|-------------|
| `/` | Home | Public |
| `/posts/` | PostListView | Public |
| `/posts/new/` | PostCreateView | Authenticated users |
| `/posts/<slug>/` | PostDetailView | Public |
| `/posts/<slug>/edit/` | PostUpdateView | Author only |
| `/posts/<slug>/delete/` | PostDeleteView | Author only |
| `/register/` | Register | Public |
| `/login/` | Login | Public |
| `/logout/` | Logout | Authenticated users |
| `/profile/` | Profile update | Authenticated users |

---

## Setup

1. Clone the repository:
   git clone <https://github.com/fnkorley-stack/Alx_DjangoLearnLab/tree/main/django_blog>
   cd django_blog
2. Install dependencies:

pip install -r requirements.txt


3. Apply migrations:

python manage.py makemigrations
python manage.py migrate


4. Run the development server:

python manage.py runserver


5. Open your browser at http://127.0.0.1:8000/ to access the blog.

Usage Notes

Only authenticated users can create posts.

Only the author can edit or delete their posts.

All users (authenticated or not) can view the post list and details.

Post URLs use automatically generated slugs from the post title.

CRUD operations are implemented with CBVs:

PostListView → list all posts

PostDetailView → view single post

PostCreateView → create new post (LoginRequiredMixin)

PostUpdateView → edit post (LoginRequiredMixin + UserPassesTestMixin)

PostDeleteView → delete post (LoginRequiredMixin + UserPassesTestMixin)


---

### ✅ Instructions:

1. Create `README.md` at the **project root** (same level as `manage.py`).  
2. Paste this content and save.  
3. Commit and push:

git add README.md
git commit -m "Add README for CBV CRUD blog with permissions"
git push origin main
