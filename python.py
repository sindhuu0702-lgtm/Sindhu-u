import re

def extract_comments(code):
    pattern = r"(#.?$|'''[\s\S]?'''|\"\"\"[\s\S]*?\"\"\")"
    comments = re.findall(pattern, code, re.MULTILINE)
    return comments

if _name_ == "_main_":
    sample_code = """
# ಇದೊಂದು ಉದಾಹರಣೆಯ comment
print("Hello World")
"""
    print("Extracted comments:", extract_comments(sample_code)
