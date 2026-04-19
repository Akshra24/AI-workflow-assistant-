import pdfplumber

# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -------- AI WORKFLOW PROCESSING --------
def process_text(text):
    text = text.strip()
    text = text[:800]

    if len(text) < 30:
        return "Please provide more detailed input text."

    # Split into sentences
    sentences = [s.strip() for s in text.split('.') if s.strip()]

    # -------- SUMMARY --------
    summary = ". ".join(sentences[:2]) + "."

    # -------- KEY POINTS --------
    key_points = sentences[:4]

    # -------- ACTION ITEMS --------
    action_items = [
        s for s in sentences
        if any(word in s.lower() for word in ["will", "should", "need", "must"])
    ]

    # -------- FORMAT OUTPUT --------
    output = f"""
### 📝 Summary:
{summary}

### 📌 Key Points:
{"".join([f"- {point}\n" for point in key_points])}

### ✅ Action Items:
{"".join([f"- {item}\n" for item in action_items]) if action_items else "- No clear action items found."}
"""

    return output