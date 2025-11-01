# Contributing to Data Science & AI Projects

We welcome contributions from the community! This document provides guidelines for contributing to this repository.

## 🤝 How to Contribute

### Types of Contributions

1. **New Projects**: Add beginner, intermediate, or advanced projects
2. **Bug Fixes**: Fix issues in existing code
3. **Documentation**: Improve README files, comments, or guides
4. **AI Agent Prompts**: Add new prompts for project enhancement
5. **Dataset Links**: Add new or alternative dataset sources
6. **Performance Improvements**: Optimize existing code

### Before Contributing

1. **Check existing issues** to see if your contribution is already being worked on
2. **Open an issue** to discuss major changes before implementing
3. **Follow the project structure** outlined in the main README

## 📋 Contribution Guidelines

### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Comments**: Write clear, concise comments
- **Documentation**: Include docstrings for functions and classes
- **Error Handling**: Implement appropriate error handling
- **Testing**: Include basic tests where applicable

### Project Structure Requirements

Each new project must include:

```
project-name/
├── README.md              # Project documentation
├── requirements.txt       # Project-specific dependencies
├── main.py               # Main implementation
├── data/                 # Local data files (if small)
├── notebooks/            # Jupyter notebooks
├── src/                  # Source code modules
├── tests/                # Test files
└── ai-prompts/           # AI agent prompts
    ├── enhancement.md
    ├── debugging.md
    └── optimization.md
```

## 🚀 Getting Started

### Setting Up Development Environment

1. **Fork the repository**
```bash
git clone https://github.com/YOUR_USERNAME/data-science-ai-projects.git
cd data-science-ai-projects
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

### Making Changes

1. **Write clean, documented code**
2. **Test your changes thoroughly**
3. **Update documentation as needed**
4. **Follow the existing code style**

### Submitting Changes

1. **Commit your changes**
```bash
git add .
git commit -m "Add: Brief description of changes"
```

2. **Push to your fork**
```bash
git push origin feature/your-feature-name
```

3. **Create a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Include screenshots if applicable

## 📝 Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe):

## Testing
- [ ] Code has been tested locally
- [ ] All existing tests pass
- [ ] New tests added (if applicable)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] AI prompts included (for new projects)
```

## 🎯 Project Categories

### Beginner Projects
- Focus on fundamental concepts
- Clear, step-by-step implementations
- Extensive comments and documentation
- Simple datasets and straightforward objectives

### Intermediate Projects
- More complex algorithms and techniques
- Real-world datasets and scenarios
- Performance considerations
- Multiple evaluation metrics

### Advanced Projects
- Cutting-edge techniques and methodologies
- Large-scale datasets
- Production-ready code
- Advanced optimization and deployment considerations

## ❓ Questions?

If you have questions about contributing:

1. **Check existing issues** for similar questions
2. **Open a new issue** with the "question" label
3. **Join discussions** in existing issues and pull requests

## 🙏 Recognition

All contributors will be acknowledged in the project README and commit history.

Thank you for contributing to the Data Science & AI Projects repository! 🚀