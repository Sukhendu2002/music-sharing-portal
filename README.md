# Django Music Sharing Web App

This is a Django-based web application for sharing and discovering music. This application allows users to upload and share their favorite songs, create playlists, and explore music shared by others. It's a platform that brings music enthusiasts together to connect, discover new tracks, and enjoy their favorite tunes.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
    - [User Registration](#user-registration)
    - [Uploading Music](#uploading-music)
    - [Creating Playlists](#creating-playlists)
    - [Exploring Music](#exploring-music)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Music Upload**: Upload and share your favorite songs with the community.
- **Create Playlists**: Organize songs into playlists and customize the playlist cover.
- **Explore Music**: Discover and listen to music uploaded by other users.
- **Search Functionality**: Search for specific songs, artists, or genres.
- **Like and Comment**: Engage with other users' music through likes and comments.
- **User Profiles**: View and follow other users' profiles.

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- Python (3.6 or higher)
- Django
- Virtualenv (optional but recommended)
- Dependencies listed in `requirements.txt`

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/django-music-sharing-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-music-sharing-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account for admin access:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

Your Django Music Sharing Web App should now be running locally at `http://127.0.0.1:8000/`.

## Usage

### User Registration

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Click on "Register" to create a new account.
3. Fill in the required details and click "Register."
4. You can now log in with your new account credentials.

### Uploading Music

1. Log in to your account.
2. Click on "Upload Music" in the navigation menu.
3. Fill in the song details, upload the song file, and submit the form.
4. Your song will be added to the library for others to discover.

### Creating Playlists

1. Log in to your account.
2. Click on "Create Playlist" in the navigation menu.
3. Provide a name for your playlist, optionally add a description and a cover image.
4. Search for songs to add to your playlist and save it.

### Exploring Music

1. Explore music by clicking on "Music Library" in the navigation menu.
2. Use the search bar to find specific songs, artists, or genres.
3. Click on a song to listen, like, and comment.
