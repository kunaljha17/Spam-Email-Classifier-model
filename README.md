# Email Spam Classifier

A Flask web application that uses a trained machine-learning model to classify email text as **Spam** or **Not Spam**.

## Live Demo

[Open the deployed application on Render](https://model-deployment-p6bd.onrender.com)

## Features

- Browser-based email classification form
- JSON API for programmatic predictions
- Input validation for empty and invalid requests
- Pre-trained text vectorizer and classifier loaded from the `models/` directory
- Deployable on Render with Gunicorn

## Tech Stack

- Python
- Flask
- scikit-learn
- Gunicorn
- HTML and CSS

 
## API Usage

Send a `POST` request to `/api/predict` with a JSON body containing the `email-content` field:

```bash
curl -X POST https://model-deployment-p6bd.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d "{\"email-content\":\"Congratulations! You have won a free prize.\"}"
```

Example response:

```json
{
  "email": "Congratulations! You have won a free prize.",
  "label": "Spam",
  "prediction": 1
}
```

The prediction values are:

- `1`: Spam
- `0`: Not Spam

## Render Deployment

The deployed service is available at [https://model-deployment-p6bd.onrender.com](https://model-deployment-p6bd.onrender.com).

## License

This project is distributed under the license in [LICENSE](LICENSE).
