# Destiny2APILibrary
This project is a python library designed to streamline access to Bungie's "Destiny 2" API

__Support for this project is currently limited to systems running Windows 10/11__

The user will need to register their own app through Bungie's Developer portal in order to generate an API Key

### How to register an App
1) Sign in to the website https://www.bungie.net/en/Application
2) Click "Create New App"
3) Fill out the form and agree to the Terms of Use

### How to set up the "Connection" object
In order for the "Connection" object to initialize properly, the "BungieAPIKey" environment variable needs to be set with the API Key generated for your Bungie app on the developer portal. Once you have access to the key for your app, run "KeyEnvVar.py" from an admin powershell.
