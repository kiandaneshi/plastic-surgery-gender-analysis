# PubMed Gender Analysis Tool for Plastic Surgery Literature

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

This repository contains the complete methodology and code for conducting large-scale gender analysis of academic literature using the PubMed Entrez API. Originally developed for analyzing gender patterns in plastic surgery literature (2015-2025), this tool is designed to be adaptable for any medical specialty or research field.

**Key Features:**
- **Scalable Data Collection**: Systematic sampling methodology to handle large datasets efficiently
- **Robust Gender Classification**: International name database with 61.5% identification accuracy
- **Subspecialty Analysis**: Automated MeSH term-based topic classification
- **Statistical Validation**: Chi-squared testing with p-values for all findings
- **Publication-Ready Outputs**: Automated table and figure generation

## Research Impact

This methodology was used to analyze **108,377 plastic surgery articles**, producing the largest bibliometric gender analysis in surgical literature to date. Key findings:
- 33.6% female first authorship (significant improvement from 27.2% in 2015 to 39.6% in 2025)
- Subspecialty variation ranging from 19-42 percentage point gender gaps
- No significant gender bias in assertive language usage

## Quick Start

### Prerequisites
```bash
pip install requests pandas gender-guesser lxml scipy matplotlib seaborn
```

### Basic Usage
```python
from src.main import main

# Run complete analysis
main()
```

### Custom Analysis
```python
from src.pubmed_api import PubMedAPI
from src.gender_analyzer import GenderAnalyzer
from src.topic_classifier import TopicClassifier

# Initialize components
pubmed_api = PubMedAPI()
gender_analyzer = GenderAnalyzer()
topic_classifier = TopicClassifier()

# Search for articles
search_term = 'your specialty here'
date_range = '2020/01/01:2023/12/31'
article_ids = pubmed_api.search_articles(search_term, date_range)

# Fetch and analyze
articles = pubmed_api.fetch_article_details(article_ids)
# Continue with analysis...
```

## Methodology

### Data Collection Strategy
1. **Year-by-Year Search**: Bypasses PubMed's 10,000 record limit per query
2. **Systematic Sampling**: Every 5th article for computational efficiency (~20% sample)
3. **Rate Limiting**: Respectful API usage with built-in delays
4. **Batch Processing**: 200-article batches for optimal performance

### Gender Classification
- **Library**: `gender-guesser` with international name database
- **Preprocessing**: Removes titles, suffixes, handles initials
- **Categories**: Male, Female, Unknown, Ambiguous
- **Accuracy**: 61.5% successful gender identification

### Topic Classification
- **Method**: MeSH term keyword matching
- **Categories**: Customizable subspecialty definitions
- **Algorithm**: Rule-based with exact and partial term matching
- **Extensible**: Easy to adapt for different medical specialties

### Statistical Analysis
- **Primary Tests**: Chi-squared tests for categorical comparisons
- **Effect Sizes**: Cramér's V for practical significance
- **Multiple Comparisons**: Conservative α = 0.001 threshold
- **Power Analysis**: >99% power for detecting medium effects

## File Structure

```
src/
├── main.py                 # Main orchestration script
├── pubmed_api.py          # PubMed Entrez API interface
├── gender_analyzer.py     # Gender inference from names
├── topic_classifier.py    # MeSH term-based subspecialty classification
├── data_processor.py      # Title analysis and data cleaning
└── statistical_analyzer.py # Statistical testing and validation

examples/
├── basic_usage.py         # Simple analysis example
├── custom_search.py       # Custom search parameters
└── specialty_adaptation.py # Adapting for other medical fields

docs/
├── methodology.md         # Detailed methodology
├── api_reference.md       # Complete API documentation
└── troubleshooting.md     # Common issues and solutions
```

## Customization for Other Specialties

### 1. Search Terms
Modify the search term in `main.py`:
```python
search_term = 'your specialty[MeSH Major Topic]'
```

### 2. Subspecialty Categories
Edit `topic_classifier.py` to define your specialty's subspecialties:
```python
self.topic_keywords = {
    'your_subspecialty_1': ['keyword1', 'keyword2'],
    'your_subspecialty_2': ['keyword3', 'keyword4'],
    # Add more categories...
}
```

### 3. Power Words Analysis
Customize assertive language terms in `data_processor.py`:
```python
self.power_words = ['novel', 'breakthrough', 'first', 'superior', 'your_terms']
```

## Output Data Format

The tool generates several output files:
- **CSV**: Raw analysis results with all metadata
- **Summary TXT**: Statistical findings and key metrics
- **Excel**: Publication-ready tables
- **Figures**: PNG/PDF visualizations

### Example Output Structure
```csv
pmid,title,first_author,gender,topic,year,journal,power_words_count
12345678,"Novel Approach to...",Smith J,female,aesthetics,2023,Plastic Surgery,1
```

## Ethical Considerations

- **Gender Binary Limitation**: Current classification is binary (male/female) due to name database constraints
- **Cultural Bias**: Name databases may have reduced accuracy for non-Western names
- **Privacy**: Only analyzes publicly available metadata, no patient data
- **Transparency**: All code and methodology openly available for scrutiny

## Performance

- **Processing Speed**: ~200 articles per batch, ~1 hour for 20,000 articles
- **Memory Usage**: <1GB RAM for typical analyses
- **API Limits**: Respects PubMed rate limiting (3 requests/second)
- **Scalability**: Tested up to 100,000+ articles

## Citation

If you use this tool in your research, please cite:

```
https://doi.org/10.5281/zenodo.15849698

A paper is in the works that can/will need to be cited too!

## Contributing

We welcome contributions! See `CONTRIBUTING.md` for guidelines.

### Areas for Enhancement
- Non-binary gender classification methods
- Additional language analysis features
- International journal integration
- Real-time monitoring dashboards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: GitHub Issues for bug reports and feature requests
- **Documentation**: See `docs/` folder for detailed guides
- **Email**: [Your Contact Email]

## Acknowledgments

- **PubMed/NCBI**: For providing open access to biomedical literature
- **Gender-Guesser**: International name classification library
- **Research Community**: For advancing open science practices

---

**Note**: This tool is designed for academic research purposes. Always verify results independently and consider the limitations of algorithmic gender classification.
