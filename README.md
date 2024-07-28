# CarbonCart

A Eco-friendly support for your groceries\
Identifying the carbon footprints of grocery purchase

## 📃 Brief Overview

Welcome to CarbonCart, a Groceries Carbon Footprint Calculator! This web application helps users understand the
environmental impact of their grocery purchases by converting digital notes into text, analyzing the carbon footprint of
each item, and providing recommendations for more sustainable alternatives.

## 💡 Key Insights

- Screenshot to Text Conversion: Users upload a screenshot of their digital grocery list from their phone notes. The
  application uses Optical Character Recognition (OCR) to convert the image into a text file containing the names of the
  groceries.
- Carbon Footprint Analysis: The text file is compared with a dataset that includes the carbon emissions per kilogram
  for each item. This allows the application to calculate the total carbon footprint of the user's grocery purchases.
- Sustainable Alternatives: The recommendation engine suggests alternative products with lower carbon footprints,
  helping users make more environmentally conscious choices.

## 📈 Timeline

|→ This project was initiated with a blank repository on 27/07/2024.\
|→ In the evening of 27/04/2024, OCR implementation was done and integrated successfully in the website.\
|→ End of day 27/07/2024, the website UI was done and was made responsive enough for presentation.\
|→ User profiles and authentication was also implemented successfully by 28/07/2024 morning.\
|→ The auto correct and recommendation engine features were done and added in the morning of 28/07/2024.\
|→ A simple working web app was created by the afternoon of 28/07/2024 with the functionality of calculating the total
carbon footprint of the items in the groceries purchased.\
|→ By the end of 28/07/2024 we had small web app running and with the functionality to calculate carbon footprint of
groceries purchased by a person.

## 🥳 What worked

- The UI and backend logic of the website is fully functional with a smooth integration with OCR.
- The website takes in image of the grocery list and converts that into text for the total carbon footprint calculation.
- The recommendation engine for low carbon footprint alternatives for the purchases works well and is also integrated
  with the website.
- For the manual input, which is triggered when the ocr fails to recognize something or if the quantity is missing, the
  feature of auto-correction has been implemented successfully.

## 📌 What we plan to add further

- We plan to add a feature to manually input data into the website for carbon footprint calculation.
- We also intend to add an input method where the user can directly click a picture of the receipt and the data is
  directly taken from there.`

## 📽️ Demo Video

Please find out website demo: https://youtu.be/5LZdxYBY14E

## ⚒️ Setting up the project

Install pipenv, a python environment manager

```commandline
pip install pipenv
```

Next, install all packages

```commandline
pipenv install
```

To access the environment, run:

```commandline
pipenv shell
```

## 🫂 Contributors

Contributions make the open source community such an amazing place to learn, inspire, and create.
The contributors to this project are <br></br>
<a href="https://github.com/Annarhysa/CarbonCart/graphs/contributors">
<img src="https://contrib.rocks/image?repo=Annarhysa/CarbonCart" />
<img src="https://contrib.rocks/image?repo=Prithvi2310/Codes"/>
</a>

## 🛡️ Privacy Policy

Your privacy is important to us. This Privacy Policy outlines how we collect, use, and protect your information when you
use our services.

#### Data Collection and Usage

All data collected through our platform is used solely for the purpose of showing users their history. We use [Supabase](https://supabase.io),
an open-source backend as a service, to handle all authentication and data collection.

#### Data Protection

We are committed to ensuring that your data is secure. We do not sell, distribute, or lease your personal information to
third parties outside of our organization.

#### Access to Data

Only certain authorized officials within our organization have limited access to the database. This access is restricted
and used exclusively for development and maintenance purposes.

## 🪪 License

Please have a look at the [LICENSE](LICENCE.md) for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
