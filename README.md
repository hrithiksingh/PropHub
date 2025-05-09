# Prop Image Tagging Service

A simple FastAPI app to manage image tags: list all images, auto-generate tags for uploads, and edit existing tags.

## Prerequisites

- Python 3.10+
- pip

## Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
python -m venv .venv
source .venv/bin/activate       # on Windows: .venv\Scripts\activate
pip install fastapi uvicorn
```

> If you already have a `requirements.txt`, run:
> ```bash
> pip install -r requirements.txt
> ```

## Project Structure

```
src/
├── app.py                   # FastAPI app entrypoint
├── controllers/
│   └── prop_API_controller.py
├── models/
│   └── prop_images.py
└── services/
    ├── get_all_images.py
    ├── save_new_image.py
    └── edit_tags.py
```

## Running the App

```bash
uvicorn src.app:app --reload
```

By default it will be available at `http://127.0.0.1:8000`.

## Available Endpoints

| Method | Path                         | Description                          |
|:------:|------------------------------|--------------------------------------|
| GET    | `/`                          | Health check – returns `{"message":"ALL is well!"}` |
| GET    | `/images`                    | List all images and their tags       |
| POST   | `/images/analyze`            | Upload an image, generate & save tags|
| PUT    | `/images/{image_id}/tags`    | Update tags for a specific image     |

## Usage Examples

- **Health check**
  ```bash
  curl http://127.0.0.1:8000/
  ```

- **List images**
  ```bash
  curl http://127.0.0.1:8000/images
  ```

- **Analyze image**
  ```bash
  curl -X POST "http://127.0.0.1:8000/images/analyze" \
       -F "file=@/path/to/photo.jpg"
  ```

- **Edit tags**
  ```bash
  curl -X PUT "http://127.0.0.1:8000/images/<IMAGE_ID>/tags" \
       -H "Content-Type: application/json" \
       -d '{"tags":["wedding","floral"]}'
  ```

Feel free to extend with a real database backend, authentication, or cloud storage for images.
