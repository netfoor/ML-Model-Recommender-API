# ML Model Recommender API

A FastAPI service that recommends the most cost-effective OpenAI model for a given task, considering cost, performance, and task fit.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 📊 **Smart Recommendations** - Algorithm-based model selection
- 💰 **Cost Optimization** - Recommends most cost-effective models
- ⚡ **High Performance** - Optimized for speed and efficiency
- 🐳 **Docker Support** - Containerized deployment
- ☁️ **AWS Lambda Ready** - Serverless deployment with Serverless Framework

## API Contract

### Request
```json
{
  "prompt": "Summarize this text: ...",
  "task": "summarization"
}
```

### Response
```json
{
  "provider": "openai",
  "model": "gpt-3.5-turbo",
  "reason": "Best trade-off between cost and task accuracy for summarization",
  "approx_cost_per_1k_tokens": 0.001,
  "max_context_length": 16000,
  "speed": "fast"
}
```

## Supported Tasks

- `summarization` - Text summarization
- `chat` - Conversational AI
- `classification` - Text classification
- `creative` - Creative writing
- `complex_reasoning` - Complex problem solving

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js (for Serverless Framework)
- AWS CLI configured (for deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ml-recomendations.git
   cd ml-recomendations
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Test the API**
   ```bash
   curl -X POST "http://localhost:8000/recommend-model" \
        -H "Content-Type: application/json" \
        -d '{"task": "summarization"}'
   ```

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t model-recommender .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 model-recommender
   ```

### AWS Lambda Deployment

1. **Install Serverless Framework**
   ```bash
   npm install -g serverless
   npm install
   ```

2. **Deploy to AWS**
   ```bash
   serverless deploy
   ```

## Configuration

The model configurations are stored in `app/models.yml`. You can modify this file to add new models or update existing ones:

```yaml
models:
  - name: gpt-3.5-turbo
    provider: openai
    context_length: 16000
    cost_input: 0.001
    cost_output: 0.002
    speed: fast
    tasks: [summarization, chat, classification]
```

## Testing

Run the test suite:

```bash
pytest
```

## Project Structure

```
ml-recomendations/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app and Lambda handler
│   ├── recommender.py       # Recommendation logic
│   ├── config.py           # Configuration loader
│   └── models.yml          # Model definitions
├── test/
│   ├── __init__.py
│   ├── test_api.py         # API tests
│   └── test_recommender.py # Recommender tests
├── requirements.txt         # Python dependencies
├── serverless.yml          # Serverless Framework config
├── Dockerfile              # Docker configuration
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need help, please open an issue on GitHub.
