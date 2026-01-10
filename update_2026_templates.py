#!/usr/bin/env python3
"""
Script to update 2026 templates:
- Change "PyCon Uganda" to "PyCon Africa"
- Change year references from 2025 to 2026
- Update routes and paths
"""

import os
import re
from pathlib import Path

def update_template_file(file_path):
    """Update a single template file with replacements."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Track changes
        changes = []
        
        # 1. Replace "PyCon Uganda" with "PyCon Africa" (case-insensitive)
        replacements = [
            (r'PyCon Uganda', 'PyCon Africa'),
            (r'Pycon Uganda', 'Pycon Africa'),
            (r'PYCON UGANDA', 'PYCON AFRICA'),
            (r'pycon uganda', 'pycon africa'),
            (r'PyConUganda', 'PyConAfrica'),
            (r'@pyconuganda', '@pyconafrica'),
            (r'@PyConUganda', '@PyConAfrica'),
        ]
        
        for old, new in replacements:
            if old in content:
                count = content.count(old)
                content = content.replace(old, new)
                changes.append(f"  - Replaced '{old}' with '{new}' ({count} times)")
        
        # 2. Replace year 2025 with 2026 in various contexts
        year_replacements = [
            # URL paths
            (r"'/2025/", "'/2026/"),
            (r'"/2025/', '"/2026/'),
            (r"href='/2025/", "href='/2026/"),
            (r'href="/2025/', 'href="/2026/'),
            (r"url='/2025/", "url='/2026/"),
            (r'url="/2025/', 'url="/2026/'),
            
            # Include statements
            (r"{% include '2025/", "{% include '2026/"),
            (r'{% include "2025/', '{% include "2026/'),
            
            # Static file references
            (r"{% static '2025/", "{% static '2026/"),
            (r'{% static "2025/', '{% static "2026/'),
            
            # URL template tags
            (r"year=2025", "year=2026"),
            (r"year='2025'", "year='2026'"),
            (r'year="2025"', 'year="2026"'),
            
            # Text references
            (r'PyCon Uganda 2025', 'PyCon Africa 2026'),
            (r'Pycon Uganda 2025', 'Pycon Africa 2026'),
            (r'PYCON UGANDA 2025', 'PYCON AFRICA 2026'),
            
            # Standalone year in text (be careful with this)
            (r'\b2025\b', '2026'),
        ]
        
        for old, new in year_replacements:
            if re.search(old, content):
                matches = len(re.findall(old, content))
                content = re.sub(old, new, content)
                changes.append(f"  - Replaced pattern '{old}' with '{new}' ({matches} times)")
        
        # 3. Special case: event year references
        # Handle dates like "7th - 9th August, 2025" -> needs manual review
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        
        return False, []
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main():
    """Main function to process all templates in 2026 folder."""
    templates_dir = Path('templates/2026')
    
    if not templates_dir.exists():
        print(f"Error: {templates_dir} does not exist!")
        return
    
    print("=" * 70)
    print("Starting template update for 2026 folder")
    print("=" * 70)
    print()
    
    total_files = 0
    updated_files = 0
    
    # Walk through all HTML files in templates/2026
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                relative_path = file_path.relative_to('templates/2026')
                total_files += 1
                
                updated, changes = update_template_file(file_path)
                
                if updated:
                    updated_files += 1
                    print(f"✓ Updated: {relative_path}")
                    for change in changes:
                        print(change)
                    print()
    
    print("=" * 70)
    print(f"Summary:")
    print(f"  Total files scanned: {total_files}")
    print(f"  Files updated: {updated_files}")
    print(f"  Files unchanged: {total_files - updated_files}")
    print("=" * 70)
    print()
    print("⚠️  IMPORTANT: Please review the changes before committing!")
    print("   Some replacements may need manual adjustment:")
    print("   - Event dates (7th - 9th August, 2025)")
    print("   - Specific venue details")
    print("   - Email addresses (team@pycon.ug vs team@pycon.africa)")
    print("   - Phone numbers")
    print("   - Any year-specific content")
    print()
    print("Recommended next steps:")
    print("  1. Review changes: git diff")
    print("  2. Test the website: uv run manage.py runserver")
    print("  3. Check key pages manually")
    print("  4. Commit if everything looks good")

if __name__ == '__main__':
    main()
