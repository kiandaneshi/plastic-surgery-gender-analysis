# GitHub Upload Guide

## Quick Upload Instructions

### 1. Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click "New repository" (green button)
3. Repository name: `pubmed-gender-analysis`
4. Description: `Large-scale gender analysis tool for academic literature using PubMed data`
5. Make it **Public** (for open source)
6. ✅ Add README file (we have our own)
7. ✅ Add .gitignore (choose Python)
8. ✅ Choose MIT License
9. Click "Create repository"

### 2. Upload Files
**Option A: Web Interface (Easiest)**
1. Click "uploading an existing file"
2. Drag and drop the entire `open_source_release` folder contents
3. Commit message: "Initial release: Complete PubMed gender analysis methodology"
4. Click "Commit changes"

**Option B: Command Line**
```bash
# Navigate to open_source_release folder
cd open_source_release

# Initialize git
git init
git add .
git commit -m "Initial release: Complete PubMed gender analysis methodology"

# Connect to your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/pubmed-gender-analysis.git
git branch -M main
git push -u origin main
```

### 3. Repository Structure (What You're Uploading)

```
pubmed-gender-analysis/
├── README.md                    # Main documentation
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── setup.py                     # Package installation
├── CONTRIBUTING.md              # Contribution guidelines
├── src/                         # Core methodology code
│   ├── main.py                  # Main analysis orchestrator
│   ├── pubmed_api.py           # PubMed API interface
│   ├── gender_analyzer.py      # Gender classification
│   ├── topic_classifier.py     # Subspecialty classification
│   ├── data_processor.py       # Title/power words analysis
│   └── statistical_analyzer.py # Statistical validation
├── examples/                    # Usage examples
│   ├── basic_usage.py          # Simple analysis example
│   └── specialty_adaptation.py # Customize for other fields
└── docs/                        # Documentation
    └── methodology.md           # Detailed methodology
```

### 4. Post-Upload Setup

#### Add Repository Topics
1. Go to your repository main page
2. Click the gear icon next to "About"
3. Add topics: `academic-research`, `pubmed`, `gender-analysis`, `bibliometrics`, `python`, `open-science`

#### Enable GitHub Pages (Optional)
1. Go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: main, folder: / (root)
4. This creates a website for your documentation

#### Create Release
1. Go to "Releases" → "Create a new release"
2. Tag: `v1.0.0`
3. Title: `Initial Release - Complete Methodology`
4. Description:
```
## PubMed Gender Analysis Tool v1.0.0

Complete methodology for large-scale gender analysis of academic literature.

### Features
- ✅ PubMed API integration with systematic sampling
- ✅ International gender classification (61.5% accuracy)
- ✅ Automated subspecialty classification via MeSH terms
- ✅ Statistical validation with chi-squared testing
- ✅ Publication-ready table and figure generation

### Validated Results
- Analyzed 108,377 plastic surgery articles (2015-2025)
- 33.6% female first authorship with significant improvement over time
- Subspecialty variation from 19-42 percentage point gender gaps

### Usage
See examples/ folder for basic usage and specialty adaptation guides.
```

### 5. Repository Description

**About Section:**
```
Large-scale gender analysis tool for academic literature using PubMed data. Validated on 108K+ plastic surgery articles. Adaptable for any medical specialty.
```

**Website:** Leave blank or add your institution URL

### 6. README Badge Updates

After upload, update these placeholder URLs in README.md:
- Replace `your-username` with your actual GitHub username
- Add your contact email
- Update any institutional affiliations

### 7. Make Repository Discoverable

#### README Keywords
Your README already includes these searchable terms:
- PubMed, Entrez API
- Gender analysis, bibliometrics
- Medical specialties, plastic surgery
- Open science, reproducible research

#### GitHub Search Optimization
Your repository will be findable by:
- "PubMed gender analysis"
- "Academic literature bias"
- "Medical research equity"
- "Bibliometric analysis tools"

### 8. Community Features

#### Enable Discussions
1. Settings → Features
2. ✅ Enable Discussions
3. Categories: General, Ideas, Q&A, Show and Tell

#### Issue Templates
GitHub will suggest creating issue templates for bug reports and feature requests.

### 9. Citation Information

Add to README after upload:
```
## Citation

```bibtex
@software{pubmed_gender_analysis_2025,
  title={PubMed Gender Analysis Tool for Academic Literature},
  author={Your Name and Collaborators},
  year={2025},
  url={https://github.com/your-username/pubmed-gender-analysis},
  version={1.0.0}
}
```

### 10. Promotion Strategy

#### Academic Sharing
- Share on academic Twitter with #OpenScience #PubMed hashtags
- Post in relevant research communities (Reddit: r/AcademicPsychology, r/medicine)
- Email relevant research groups and methodologists

#### Documentation Sites
- Submit to lists of open-source research tools
- Add to awesome lists on GitHub (awesome-python, awesome-research-tools)

## Files Ready for Upload

All files in the `open_source_release/` folder are clean, documented, and ready for public release. They contain only the essential methodology code without any analysis results or personal data.

**Total Repository Size:** ~50KB (lightweight and fast to clone)
**Dependencies:** 8 standard Python packages
**Documentation:** Complete with examples and methodology details

Your repository will provide other researchers with everything needed to:
1. Replicate your exact methodology
2. Adapt the tool for their specialty
3. Contribute improvements and enhancements
4. Build upon your work for new research questions

Upload when ready - everything is prepared for immediate public release!