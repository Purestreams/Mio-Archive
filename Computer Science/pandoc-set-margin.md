# Setting Margins for PDFs with Pandoc

When converting a Markdown file to a PDF using Pandoc, you can control the page margins by passing metadata to the underlying LaTeX engine. This is typically done through a YAML metadata block at the top of your Markdown file.

## Using the `geometry` option

Add a `geometry` field to your YAML front matter. This field passes options to LaTeX's `geometry` package.

To set all margins to the same value, you can do this:

```yaml
---
title: "Habits"
author: John Doe
date: March 22, 2005
geometry: margin=2cm
---
```

You can also specify each margin individually:

```yaml
---
title: "Advanced Document"
author: Jane Smith
geometry:
- top=2cm
- right=3cm
- bottom=2cm
- left=3cm
---
```

## Pandoc Command

To generate the PDF, you'll need to have a LaTeX distribution installed (like TeX Live, MiKTeX, or MacTeX). Then, use the following Pandoc command in your terminal:

```bash
pandoc your-file.md -o output.pdf
```

Pandoc will automatically use the `geometry` metadata when creating the PDF. You can adjust the values and units (e.g., `in` for inches, `mm` for millimeters) as needed.