# news-recommender-system

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">news-recommender-system</h3>

  <p align="center">
    Python script for scraping news from G1 and Google Notícias.
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About The Project 

Python script for scraping news from [G1](https://g1.globo.com/) and [Google Notícias](https://news.google.com.br) and saving in a MySQL Database.

### Built With


* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/documentation/webdriver/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

The rules for user-agents was respected according to the robots.txt files of both websites.
* [G1 - robots.txt](https://g1.globo.com/robots.txt)
* [Google Notícias - robots.txt](https://news.google.com.br/robots.txt)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install these following modules utilizing pip install

* pip
  ```sh
  requests==2.26.0
  beautifulsoup4==4.9.3
  selenium==3.141.0
  mysql-connector-python==8.0.26
  python-dotenv==0.19.0
  ```

The following files are requisites from the [Heroku](https://www.heroku.com/) plataform for deploy
```sh
  requirements.txt
  runtime.txt
  Procfile
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/andre-albuquerque/web-scraping.git
   ```
3. In the project's directory, create a .env file with the database connection information

   ```sh
   DB_HOST = 'mydbhost'
   DB_USERNAME = 'mydbusername'
   DB_PASSWORD = 'mydbpassword'
   DB_DATABASE =  'mydbname'
   DB_PORT = 'mydbport'
   ```


<!-- USAGE EXAMPLES -->
## Usage

Open your terminal in the directory's project and run the following command

   ```sh
   python news_scraping.py
   ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

André de Albuquerque - [Linkedin](https://www.linkedin.com/in/andr%C3%A9-albuquerque-/) - andrealbuquerqueleo@gmail.com

Project Link: [https://github.com/andre-albuquerque/web-scraping](https://github.com/andre-albuquerque/web-scraping)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://i.imgur.com/ZQFaHk9.gif 
