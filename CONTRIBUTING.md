# Contributing to ML Model Recommender API

Thank you for considering contributing to this project! Here's how you can help.

## How to Contribute

### 1. Fork the Repository
Click the "Fork" button in the top-right corner of this repository.

### 2. Clone Your Fork
```bash
git clone https://github.com/netfoor/ml-recomendations.git
cd ml-recomendations
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Follow the existing code style
- Write tests for new functionality
- Update documentation as needed

### 5. Test Your Changes
```bash
# Run tests
pytest

# Run locally
uvicorn app.main:app --reload
```

### 6. Submit a Pull Request
- Push your changes to your fork
- Create a pull request with a clear description

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions small and focused

### Example:
```python
def recommend_model(task: str) -> dict:
    """
    Recommend the best model for a given task.
    
    Args:
        task: The task type (e.g., 'summarization', 'chat')
        
    Returns:
        dict: Model recommendation with cost and performance info
    """
    # Implementation here
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest test/test_recommender.py
```

### Writing Tests
- Place tests in the `test/` directory
- Use descriptive test names
- Test both success and error cases
- Mock external dependencies

## Documentation

### README Updates
- Update the README.md if your changes affect:
  - API endpoints
  - Configuration options
  - Installation steps
  - Usage examples

### Code Documentation
- Add docstrings to new functions
- Update existing docstrings if behavior changes
- Include type hints

## Adding New Models

To add support for new AI models:

1. **Update `app/models.yml`**:
```yaml
models:
  - name: new-model-name
    provider: provider-name
    context_length: 8000
    cost_input: 0.002
    cost_output: 0.003
    speed: fast
    tasks: [task1, task2]
```

2. **Add tests** in `test/test_recommender.py`

3. **Update documentation** with new supported models

## Bug Reports

When reporting bugs, please include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)
- Error messages (if any)

## Feature Requests

For new features:
- Explain the use case
- Describe the proposed solution
- Consider backwards compatibility
- Discuss potential alternatives

## Questions

If you have questions:
- Check existing issues first
- Create a new issue with the "question" label
- Be specific about what you're trying to do

## Review Process

Pull requests will be reviewed for:
- Code quality and style
- Test coverage
- Documentation updates
- Backwards compatibility
- Security considerations

## Recognition

Contributors will be acknowledged in:
- GitHub contributors list
- Release notes (for significant contributions)
- README credits section

Thank you for contributing! 🚀
