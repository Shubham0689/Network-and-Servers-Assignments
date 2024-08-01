# Login Page Project

This project demonstrates how to deploy a simple HTML login page on a local machine using the Nginx web server. The page is accessible via a custom DNS name `awesomeweb`.

## Project Structure

- **index.html**: The HTML file for the login page.
- **README.md**: Documentation and instructions for setting up the project.

## Prerequisites

Before starting, ensure you have the following:

- **Ubuntu**: This guide assumes you're running Ubuntu as your operating system.
- **Nginx**: Installed on your system. If not, follow the installation steps below.
- **Git**: Installed for version control and GitHub integration.

## Setup and Deployment

### Step 1: Install Nginx

1. Update the system packages:

   ```bash
    sudo apt update
2.  sudo systemctl status nginx
3. Copy index.html
    sudo cp ~/login_page_project/index.html /var/www/html/
4. Ensure the permissions are give:
    sudo chown www-data:www-data /var/www/html/index.html
    sudo chmod 644 /var/www/html/index.html
5. Modify the deatils in the below file: 
    sudo nano /etc/nginx/sites-available/default
6. Test nginx server 
    sudo nginx -t
7. Configure Local DNS:
    sudo nano /etc/hosts
8. Add awesomeweb To Local Host:
    127.0.0.1    awesomeweb
