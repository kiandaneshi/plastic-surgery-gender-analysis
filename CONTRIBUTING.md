# Contributing to PubMed Gender Analysis Tool

Thank you for your interest in contributing to this open-source research tool! This project aims to advance equity analysis in academic literature through transparent, reproducible methodology.

## How to Contribute

### 1. Reporting Issues
- **Bug Reports**: Use GitHub Issues with detailed reproduction steps
- **Feature Requests**: Describe the use case and potential implementation
- **Documentation**: Help improve clarity and completeness

### 2. Code Contributions
- **Fork** the repository
- **Create** a feature branch (`git checkout -b feature/your-feature`)
- **Make** your changes with clear commit messages
- **Test** your changes thoroughly
- **Submit** a pull request with detailed description

### 3. Areas for Enhancement

#### High Priority
- **Non-binary Gender Classification**: Develop methods beyond binary classification
- **International Name Coverage**: Improve accuracy for non-Western names
- **Real-time Monitoring**: Dashboard for ongoing literature surveillance
- **Additional Specialties**: Pre-configured setups for other medical fields

#### Medium Priority
- **Advanced NLP**: Sentiment analysis, research impact metrics
- **Journal Integration**: Direct API connections with publishers
- **Visualization Enhancements**: Interactive plots, customizable dashboards
- **Performance Optimization**: Faster processing, reduced memory usage

#### Documentation
- **Tutorial Videos**: Step-by-step usage guides
- **Case Studies**: Examples from different medical specialties
- **API Documentation**: Complete reference guide
- **Troubleshooting**: Common issues and solutions

### 4. Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/pubmed-gender-analysis.git
cd pubmed-gender-analysis

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest tests/

# Run example analysis
python examples/basic_usage.py
```

### 5. Code Standards

#### Python Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Include docstrings for all classes and methods
- Add type hints where appropriate

#### Documentation
- Update README.md for new features
- Include code examples in docstrings
- Document any new dependencies

#### Testing
- Write unit tests for new functionality
- Ensure existing tests still pass
- Include integration tests for API changes

### 6. Ethical Guidelines

#### Research Ethics
- Respect PubMed API rate limits and terms of service
- Consider bias implications in algorithmic classification
- Maintain transparency in methodology limitations
- Acknowledge data source constraints

#### Open Science
- Ensure reproducibility of all analyses
- Document methodology changes clearly
- Provide clear examples for replication
- Support accessibility for diverse users

### 7. Pull Request Process

1. **Ensure** your code follows the style guidelines
2. **Update** documentation for any new features
3. **Test** your changes with the examples provided
4. **Describe** your changes clearly in the PR description
5. **Link** any related issues or discussions

### 8. Community Guidelines

- **Be respectful** and inclusive in all interactions
- **Provide constructive** feedback in code reviews
- **Help others** learn and contribute effectively
- **Focus on the science** and methodology improvements

### 9. License Agreement

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

### 10. Recognition

Contributors will be acknowledged in:
- README.md contributor section
- Release notes for significant contributions
- Academic publications using enhanced methodology

## Questions?

- **General Questions**: Open a GitHub Discussion
- **Technical Issues**: Create a GitHub Issue
- **Research Collaboration**: Contact the maintainers directly

Thank you for helping advance open science and equity research in academic medicine!