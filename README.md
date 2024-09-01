# Object Detection 

This project is a Django-based object detection that uses object detection to identify objects in uploaded images. The object detection system is powered by YOLO (You Only Look Once), enhancing user experience by providing detailed annotations of fashion items.

## Features

- User registration 
- Secure login functionality
- Image upload with token authentication
- YOLO-powered object detection for 0bjects
- Annotated images returned with detected objects highlighted
- RESTful API endpoints for image upload and retrieval of annotations

## Requirements

- Python 3.10
- Django 4.x
- Django REST Framework
- YOLO model for object detection
- Additional dependencies listed in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
Download the weights yolov5s.pt form ultralytics and change the downloaded weights path in detection/load_model.py
### 2. Create a Virtual Environment
```bash
python3.10 -m venv venv
```
- On macOS and Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
Run cmd as administrator
.\venv\Scripts\activate.bat
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt

```
### 4. Set Up the Django Project
```bash
python manage.py migrate
```
### 6. Run the Development Server
```bash
python manage.py runserver
```
### 7. TO register the user
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/register/`
- Body: `raw JSON`
```json
{
    "username": <<enter here name>>,
    "password": <<enter password>>,
    "email": <<enter email id>>
}
```
### 8. TO login 
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/login/`
- Body: `raw JSON`
```json
{
    "username": <<enter here name>>,
    "password": <<enter password>>
    
} 
```
In response you will get access token, copy it.

### 9. To detect the object
- Method: `POST`
- URL: `http://127.0.0.1:8000/detect/`
- Header: Key `Authorization` Value `Bearer <<paste here access token>>`
- Body: `form-data` Key `file` Value `<<upload image file>>`

You can use any image you like, but for the best results, choose images that contain people or vehicles. These types of images will help you see the object detection capabilities more clearly.





