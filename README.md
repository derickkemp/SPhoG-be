# SPhoG Back-End

The back end-server for the SPhoG image gallery application.

The main purpose of the back end-sesrver is to serve as a caching layer due to very aggressive rate limiting on the Unsplash API. The back-end server also serves as a method of protecting the project's access key, which the Unsplash documentation states should be kept secret.

## Requirements

- [Python 3.10.8 or later](https://www.python.org/)
- [MongoDB 6.0.3 or later](https://www.mongodb.com/docs/manual/administration/install-community/)

## Installation

To get a local copy of Sextant working on your machine, follow these steps

- Ensure you have installed all the packages specified in the [Requirements](#requirements) section.

- Clone this repository.

  `git clone https://github.com/derickkemp/SPhoG-be.git`

- Navigate to project directory.

  `cd SPhoG-be`

- Create a virtual environment for your application.

  `python -m venv venv`

- Install the required packages.

  `pip install -r requirements.txt`

- Create a file named `.env.secret` in the project root and add your MongoDB database name and Unsplash access key.

  ```
  MONGODB_DB=<REPLACE THIS WITH YOUR MONGODB DATABASE NAME>
  UNSPLASH_ACCESS_KEY=<REPLACE THIS WITH YOUR UNSPLASH ACCESS KEY>
  ```

- Navigate to to the src directory

  `cd src/`

- Hydrate the cache with initial data

  `python -m sphog_be.db.utils.hydrate_db`

- Start the development server.

  `python -m flask --app sphog_be.app run`
