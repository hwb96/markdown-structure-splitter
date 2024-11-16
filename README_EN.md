# markdown-hierarchy-splitter

A hierarchy-preserving Markdown document splitter for RAG (Retrieval-Augmented Generation) systems that maintains document structure and table integrity.

[![PyPI version](https://badge.fury.io/py/markdown-hierarchy-splitter.svg)](https://badge.fury.io/py/markdown-hierarchy-splitter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Key Features

- **Complete Hierarchy Preservation**: Every chunk maintains its full path in the document structure (H1 > H2 > H3...)
- **Smart Table Handling**: Preserves table integrity while respecting chunk size limits
- **Multi-format Export**: Supports export to Markdown, Word (.docx), and CSV formats
- **Configurable Chunking**: Adjustable chunk sizes with intelligent boundary detection
- **Minimal Dependencies**: Built with standard Python libraries and selective use of external packages

## 🎯 Problem Solved

Traditional RAG systems often face two critical issues when processing documents:

1. **Loss of Document Structure**: When documents are split into chunks, the hierarchical structure (chapters > sections > subsections) is typically lost
2. **Table Fragmentation**: Tables are frequently split mid-way, making the content incomprehensible

This library solves both issues by:
- Preserving the complete header path for each chunk
- Treating tables as atomic units while respecting size constraints

## 🚀 Installation

```bash
pip install markdown-hierarchy-splitter
```

## 📚 Usage

```python
from markdown_hierarchy_splitter import MarkdownProcessor

# Initialize processor
processor = MarkdownProcessor(chunk_size=300)

# Process a markdown file
with open('input.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()

# Get chunks with preserved hierarchy
chunks = list(processor.process_markdown(markdown_text))

# Export to multiple formats
processor.create_output_files(
    input_file="input.md",
    chunk_size=300
)
```

## Example Output

Input markdown:
```markdown
# Chapter 1
## Section 1.1
### Subsection 1.1.1
Some content here...

### Subsection 1.1.2
More content here...
```

Output chunks (with preserved hierarchy):
```markdown
# Chapter 1
## Section 1.1
### Subsection 1.1.1
Some content here...

# Chapter 1
## Section 1.1
### Subsection 1.1.2
More content here...
```

## 🏗️ Project Architecture

```
markdown-hierarchy-splitter/
├── src/
│   └── markdown_hierarchy_splitter/
│       ├── __init__.py
│       ├── processor.py          # Core processing logic
│       ├── exporters/
│       │   ├── __init__.py
│       │   ├── markdown.py       # Markdown export functionality
│       │   ├── docx.py          # Word document export
│       │   └── csv.py           # CSV export
│       └── utils/
│           ├── __init__.py
│           ├── hierarchy.py      # Header hierarchy management
│           └── table_handler.py  # Table processing utilities
├── tests/
│   ├── __init__.py
│   ├── test_processor.py
│   ├── test_exporters/
│   └── test_utils/
├── examples/
│   ├── basic_usage.py
│   └── sample_documents/
├── docs/
│   ├── API.md
│   └── advanced_usage.md
├── setup.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🛠️ Core Components

1. **MarkdownProcessor**
   - Manages the overall document processing flow
   - Coordinates between hierarchy tracking and table handling

2. **HierarchyTracker**
   - Maintains complete header paths
   - Ensures each chunk knows its exact position in document structure

3. **TableHandler**
   - Identifies and processes markdown tables
   - Implements smart table splitting logic

4. **Exporters**
   - Handles output generation in various formats
   - Maintains formatting consistency

## 📋 Requirements

- Python 3.8+
- python-docx
- langchain-text-splitters

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by challenges faced in RAG systems
- Built with best practices from the LangChain community