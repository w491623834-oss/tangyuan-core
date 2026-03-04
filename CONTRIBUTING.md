# Contributing to tangyuan-core

Thank you for your interest in contributing to tangyuan-core! This document provides guidelines for contributing.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/w491623834-oss/tangyuan-core.git
cd tangyuan-core

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
pytest tests/

# Run benchmarks
python benchmark.py
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function signatures
- Add docstrings to all public functions
- Keep functions focused and under 50 lines when possible
- Optimize for readability over cleverness

## Testing

- All new features must include tests
- Tests should cover both success and error cases
- Run the full test suite before submitting PR
- Aim for >80% code coverage

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Update documentation as needed
6. Run tests and ensure they pass
7. Commit with clear, descriptive messages
8. Push to your fork
9. Open a Pull Request

## Commit Message Format

```
type(scope): subject

body (optional)

footer (optional)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `chore`: Maintenance tasks

## Areas for Contribution

### High Priority
- [ ] WebSocket exchange adapters
- [ ] Additional trading strategies
- [ ] Performance optimizations
- [ ] Documentation improvements

### Medium Priority
- [ ] More comprehensive tests
- [ ] CI/CD pipeline
- [ ] Additional platform support
- [ ] Example trading bots

### Documentation
- [ ] API documentation
- [ ] Tutorials and guides
- [ ] Architecture decision records
- [ ] Performance benchmarks

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Documentation improvements
- General questions

## Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Welcome newcomers
- Assume good intent

---
**TangYuan** - Digital Guardian
