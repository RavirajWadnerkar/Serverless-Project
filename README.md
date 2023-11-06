# Random Quote Serverless API

This project contains a serverless API that returns random quotes. It's built using Google Cloud Functions.

## Getting Started

These instructions will get you a copy of the project up and running on your Google Cloud Platform account.

### Prerequisites

- Google Cloud SDK
- Node.js (for Firebase CLI if used)

### Installing

1. Clone the repository:

git clone https://github.com/RavirajWadnerkar/Serverless-Project.git

2. Navigate to the project directory:

cd Serverless-Project 


### Deployment

To deploy this function, run the following command:

gcloud functions deploy random_quote --runtime python39 --trigger-http --allow-unauthenticated --entry-point=random_quote


### Usage

Once deployed, you can fetch a random quote by sending an HTTP request to the function's endpoint:

For anyone to use it and modify it, you need to replace the curl https://us-central1-serverless-application-404304.cloudfunctions.net/random_quote with your region and project id.

#### Some pictures

![image](https://github.com/RavirajWadnerkar/Serverless-Project/assets/47893967/5e03cf08-c02a-4cf0-9a54-6153f8861fee)

![image](https://github.com/RavirajWadnerkar/Serverless-Project/assets/47893967/ad38d442-1d34-4de8-83e6-d61338e23027)

![image](https://github.com/RavirajWadnerkar/Serverless-Project/assets/47893967/c4444ba8-8700-4d10-9443-6a8640c94ad0)
