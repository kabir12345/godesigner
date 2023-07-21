Sure, here's the detailed and technical README.md for your project:
# GoDesigner

## Table of Contents
1. [Overview](#overview)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [Known Issues](#known-issues)
7. [Future Improvements](#future-improvements)
8. [Contact Information](#contact-information)
9. [License](#license)

## Overview
GoDesigner is a B2B tool designed for interior designers. It allows users to upload photos of homes and reimagine the house using generative AI. The web app also provides product recommendations that are present in the generated photo using the Segment Anything model and Google Shopping API.

## Technologies Used
The project uses a fine-tuned Stable Diffusion model, which is specifically tailored towards images and prompts related to the images. The model is trained on a custom dataset with a population size of 10798. The project is primarily written in Python and uses Docker for containerization.

## Installation
To install and run the project, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/kabir12345/godesigner.git
```
2. Navigate to the project directory:
```bash
cd godesigner
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Build the Docker image:
```bash
docker build -t godesigner .
```
5. Run the Docker container:
```bash
docker run -p 5000:5000 godesigner
```

## Usage
Once the application is running, navigate to `localhost:5000` in your web browser. From there, you can upload a photo of a home and the application will generate a reimagined version of the home using generative AI.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
