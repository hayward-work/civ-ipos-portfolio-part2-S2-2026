from setuptools import setup, find_packages

setup(
    name="task_manager_cli",  # Updated project name
    version="0.2",  # Updated version to reflect the new project
    packages=find_packages(where='src'),  # Automatically locate packages under 'src'
    package_dir={'': 'src'},  # Packages are located in the 'src' directory

    # Dependencies required for the updated functionality
    install_requires=[
        "click>=8.0",          # For enhanced CLI functionality
        "python-dateutil>=2.8" # For robust date validation
    ],

    # Project metadata
    author="Your Name",
    author_email="your-email@example.com",
    description="A CLI-based Task Management App with reusable components",
    license="MIT",
    keywords="task management CLI reusable components",
    url="http://github.com/your_username/task-manager-cli",  # Replace with your repository URL
)
