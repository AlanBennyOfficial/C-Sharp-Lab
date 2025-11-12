import os
import subprocess
import json
from datetime import datetime

REPO_PATH = "./"  # Path to your local repo clone
OUTFILE = "index.html"
GITHUB_REPO = "AlanBennyOfficial/C-Sharp-Lab"
GITHUB_BRANCH = "main"

def get_git_timestamp(filepath):
    """Get the last commit date for a file using git log."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ci", "--", filepath],
            cwd=REPO_PATH,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and result.stdout.strip():
            # Parse ISO 8601 format: "2024-11-12 10:30:45 +0000"
            timestamp_str = result.stdout.strip()
            # Extract just the date and time part
            dt_part = " ".join(timestamp_str.split()[:2])
            return dt_part
        return "N/A"
    except Exception:
        return "N/A"

def scan_program_files(root_path):
    """Recursively find all Program.cs files with their metadata."""
    programs = []
    
    for root, dirs, files in os.walk(root_path):
        # Skip hidden and build directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['bin', 'obj']]
        
        if "Program.cs" in files:
            full_path = os.path.join(root, "Program.cs")
            rel_path = os.path.relpath(full_path, root_path)
            
            # Get folder name (project name)
            folder_name = os.path.basename(os.path.dirname(full_path))
            
            # Get timestamp
            timestamp = get_git_timestamp(rel_path)
            
            # Read code content
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    code = f.read()
            except:
                code = "[Error: Could not read file]"
            
            # Normalize path separators for URLs
            normalized_path = rel_path.replace("\\", "/")
            
            # Build GitHub link
            github_link = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{normalized_path}"
            
            programs.append({
                "name": folder_name,
                "path": normalized_path,
                "date": timestamp,
                "code": code,
                "github_link": github_link
            })
    
    # Sort by name
    programs.sort(key=lambda x: x["name"].lower())
    return programs

def main():
    print("🔍 Scanning repository...")
    programs = scan_program_files(REPO_PATH)
    
    if not programs:
        print("❌ No Program.cs files found!")
        return
    
    print(f"✅ Found {len(programs)} Program.cs files")
    
    # Prepare data for JavaScript
    codes_json = json.dumps([p["code"] for p in programs])
    names_json = json.dumps([p["name"] for p in programs])
    paths_json = json.dumps([p["path"] for p in programs])
    dates_json = json.dumps([p["date"] for p in programs])
    links_json = json.dumps([p["github_link"] for p in programs])
    
    # Generate table rows
    table_rows = ""
    for idx, prog in enumerate(programs):
        name_escaped = prog["name"].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        path_escaped = prog["path"].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        date_escaped = prog["date"].replace('"', '&quot;')
        
        table_rows += f'''    <tr data-index="{idx}">
        <td>{name_escaped}</td>
        <td>{path_escaped}</td>
        <td>{date_escaped}</td>
        <td>
            <button class="view-btn" onclick="viewCode({idx})">⚡ Quick View</button>
            <br><br>
            <button class="link-btn" onclick="openGitHub({idx})">🔗 Link</button>
        </td>
    </tr>
'''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C# Program.cs Browser - {len(programs)} Projects</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html, body {{
            height: 100%;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .header {{
            background: rgba(255, 255, 255, 0.95);
            padding: 2em;
            border-radius: 10px;
            margin-bottom: 2em;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }}
        
        .header h1 {{
            color: #333;
            margin-bottom: 0.5em;
            font-size: 2.5em;
        }}
        
        .header p {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 10px;
            padding: 2em;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }}
        
        .controls {{
            display: flex;
            gap: 1em;
            margin-bottom: 2em;
            flex-wrap: wrap;
            align-items: center;
        }}
        
        .controls button {{
            padding: 0.7em 1.5em;
            font-size: 1em;
            border: none;
            border-radius: 5px;
            background: #667eea;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }}
        
        .controls button:hover {{
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}
        
        .search-box {{
            flex-grow: 1;
            min-width: 200px;
        }}
        
        .search-box input {{
            width: 100%;
            padding: 0.7em;
            font-size: 1em;
            border: 2px solid #667eea;
            border-radius: 5px;
            transition: all 0.3s;
        }}
        
        .search-box input:focus {{
            outline: none;
            border-color: #764ba2;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }}
        
        .stats {{
            color: #666;
            font-size: 0.95em;
            padding: 0.5em 1em;
            background: #f5f5f5;
            border-radius: 5px;
        }}
        
        .table-wrapper {{
            overflow-x: auto;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 2em;
        }}
        
        thead {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        
        th {{
            padding: 1.2em;
            text-align: left;
            font-weight: 600;
            -webkit-user-select: none;
            cursor: pointer;
            user-select: none;
            transition: background 0.3s;
            position: relative;
        }}
        
        th:hover {{
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }}
        
        th.sortable::after {{
            content: ' ⇅';
            opacity: 0.5;
            margin-left: 0.5em;
        }}
        
        th.sort-asc::after {{
            content: ' ↑';
            opacity: 1;
            color: #ffff00;
        }}
        
        th.sort-desc::after {{
            content: ' ↓';
            opacity: 1;
            color: #ffff00;
        }}
        
        td {{
            padding: 1em 1.2em;
            border-bottom: 1px solid #e5e5e5;
            color: #333;
        }}
        
        tbody tr {{
            transition: all 0.2s;
        }}
        
        tbody tr:hover {{
            background: #f9f9f9;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }}
        
        tbody tr.hidden {{
            display: none;
        }}
        
        .view-btn, .link-btn {{
            padding: 0.5em 1em;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 600;
            font-size: 0.85em;
            margin-right: 0.5em;
        }}
        
        .view-btn {{
            background: #667eea;
            color: white;
        }}
        
        .view-btn:hover {{
            background: #764ba2;
            transform: scale(1.05);
        }}
        
        .link-btn {{
            background: #1f6feb;
            color: white;
        }}
        
        .link-btn:hover {{
            background: #388bfd;
            transform: scale(1.05);
        }}
        
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            overflow-y: auto;
        }}
        
        .modal.show {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .modal-content {{
            background: white;
            padding: 2em;
            border-radius: 10px;
            max-width: 90vw;
            max-height: 90vh;
            overflow: auto;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            animation: slideIn 0.3s ease;
        }}
        
        @keyframes slideIn {{
            from {{
                transform: translateY(-50px);
                opacity: 0;
            }}
            to {{
                transform: translateY(0);
                opacity: 1;
            }}
        }}
        
        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5em;
            padding-bottom: 1em;
            border-bottom: 2px solid #667eea;
        }}
        
        .modal-header h2 {{
            color: #333;
            margin: 0;
            font-size: 1.5em;
        }}
        
        .modal-actions {{
            display: flex;
            gap: 0.5em;
            align-items: center;
        }}
        
        .copy-btn {{
            padding: 0.6em 1.2em;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9em;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 0.5em;
        }}
        
        .copy-btn:hover {{
            background: #218838;
            transform: scale(1.05);
        }}
        
        .copy-btn.copied {{
            background: #6c757d;
        }}
        
        .copy-feedback {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #28a745;
            color: white;
            padding: 1em 1.5em;
            border-radius: 5px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            animation: slideInRight 0.3s ease;
            z-index: 2000;
        }}
        
        @keyframes slideInRight {{
            from {{
                transform: translateX(400px);
                opacity: 0;
            }}
            to {{
                transform: translateX(0);
                opacity: 1;
            }}
        }}
        
        .close-btn {{
            font-size: 1.8em;
            font-weight: bold;
            color: #999;
            cursor: pointer;
            background: none;
            border: none;
            padding: 0;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.2s;
        }}
        
        .close-btn:hover {{
            background: #f0f0f0;
            color: #333;
        }}
        
        /* Syntax highlighting styles */
        pre {{
            background: #1e1e1e;
            padding: 1.5em;
            border-radius: 5px;
            overflow: auto;
            font-family: 'Courier New', 'Courier', monospace;
            font-size: 0.95em;
            line-height: 1.6;
            max-height: 65vh;
            margin: 0;
        }}
        
        code {{
            color: #d4d4d4;
        }}
        
        .hljs {{
            background: #1e1e1e !important;
            color: #d4d4d4 !important;
        }}
        
        .hljs-string {{
            color: #ce9178 !important;
        }}
        
        .hljs-number {{
            color: #b5cea8 !important;
        }}
        
        .hljs-literal {{
            color: #569cd6 !important;
        }}
        
        .hljs-attr {{
            color: #9cdcfe !important;
        }}
        
        .hljs-title {{
            color: #4ec9b0 !important;
        }}
        
        .hljs-params {{
            color: #9cdcfe !important;
        }}
        
        .hljs-keyword {{
            color: #569cd6 !important;
        }}
        
        .hljs-built_in {{
            color: #4ec9b0 !important;
        }}
        
        .hljs-type {{
            color: #4ec9b0 !important;
        }}
        
        .hljs-class {{
            color: #4ec9b0 !important;
        }}
        
        .hljs-comment {{
            color: #6a9955 !important;
        }}
        
        .info-message {{
            background: #e8f4f8;
            border-left: 4px solid #0084d4;
            padding: 1em;
            margin-bottom: 1.5em;
            border-radius: 4px;
            color: #0056b3;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .controls {{
                flex-direction: column;
            }}
            
            .search-box {{
                width: 100%;
            }}
            
            .container {{
                padding: 1em;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            th, td {{
                padding: 0.7em;
            }}
            
            .view-btn, .link-btn {{
                padding: 0.4em 0.8em;
                font-size: 0.75em;
                margin-right: 0.3em;
            }}
            
            .modal-actions {{
                flex-direction: column;
                width: 100%;
            }}
            
            .copy-btn {{
                width: 100%;
                justify-content: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📚 C# Program.cs Browser</h1>
        <p>AlanBennyOfficial/C-Sharp-Lab Repository</p>
    </div>
    
    <div class="container">
        <div class="info-message">
            📊 Displaying all Program.cs files from your repository (including Lab Record subfolder)
        </div>
        
        <div class="controls">
            <button onclick="sortByName()">📁 Sort by Name</button>
            <button onclick="sortByDate()">📅 Sort by Date</button>
            <button onclick="resetSort()">🔄 Reset</button>
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="🔍 Search projects..." onkeyup="filterTable()">
            </div>
            <div class="stats">
                Total: <strong id="totalCount">{len(programs)}</strong> | 
                Showing: <strong id="visibleCount">{len(programs)}</strong>
            </div>
        </div>
        
        <div class="table-wrapper">
            <table id="progTable">
                <thead>
                    <tr>
                        <th class="sortable" onclick="sortTable(0)">Project/Folder</th>
                        <th class="sortable" onclick="sortTable(1)">File Path</th>
                        <th class="sortable" onclick="sortTable(2)">Last Commit Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
{table_rows}                </tbody>
            </table>
        </div>
    </div>

    <!-- Modal for viewing code -->
    <div id="codeModal" class="modal" onclick="closeModal(event)">
        <div class="modal-content" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h2 id="modalTitle">Program.cs</h2>
                <div class="modal-actions">
                    <button class="copy-btn" id="copyBtn" onclick="copyCodeToClipboard()">
                        <span id="copyBtnText">📋 Copy Code</span>
                    </button>
                    <button class="close-btn" onclick="closeModal()">&times;</button>
                </div>
            </div>
            <pre id="codeViewer"><code id="codeContent" class="language-csharp"></code></pre>
        </div>
    </div>

    <script>
        // Data storage
        const codes = {codes_json};
        const names = {names_json};
        const paths = {paths_json};
        const dates = {dates_json};
        const links = {links_json};
        
        let currentSort = {{column: -1, ascending: true}};
        let searchTerm = '';
        let currentCodeIndex = -1;
        
        function viewCode(idx) {{
            if (idx >= 0 && idx < codes.length) {{
                currentCodeIndex = idx;
                document.getElementById('modalTitle').textContent = names[idx] + ' - Program.cs';
                const codeElement = document.getElementById('codeContent');
                codeElement.textContent = codes[idx];
                codeElement.className = 'language-csharp';
                
                // Reset copy button state
                const copyBtn = document.getElementById('copyBtn');
                copyBtn.classList.remove('copied');
                document.getElementById('copyBtnText').textContent = '📋 Copy Code';
                
                // Show modal first
                document.getElementById('codeModal').classList.add('show');
                
                // Highlight the code after a small delay to ensure DOM is updated
                setTimeout(() => {{
                    hljs.highlightElement(codeElement);
                }}, 10);
            }}
        }}
        
        function copyCodeToClipboard() {{
            if (currentCodeIndex >= 0 && currentCodeIndex < codes.length) {{
                const code = codes[currentCodeIndex];
                navigator.clipboard.writeText(code).then(() => {{
                    const copyBtn = document.getElementById('copyBtn');
                    const copyBtnText = document.getElementById('copyBtnText');
                    
                    // Show feedback
                    copyBtn.classList.add('copied');
                    copyBtnText.textContent = '✅ Copied!';
                    
                    // Show notification
                    showCopyFeedback();
                    
                    // Reset button after 2 seconds
                    setTimeout(() => {{
                        copyBtn.classList.remove('copied');
                        copyBtnText.textContent = '📋 Copy Code';
                    }}, 2000);
                }}).catch(err => {{
                    console.error('Failed to copy:', err);
                    alert('Failed to copy code. Please try again.');
                }});
            }}
        }}
        
        function showCopyFeedback() {{
            const feedback = document.createElement('div');
            feedback.className = 'copy-feedback';
            feedback.textContent = '✅ Code copied to clipboard!';
            document.body.appendChild(feedback);
            
            setTimeout(() => {{
                feedback.remove();
            }}, 3000);
        }}
        
        function openGitHub(idx) {{
            if (idx >= 0 && idx < links.length) {{
                window.open(links[idx], '_blank');
            }}
        }}
        
        function closeModal(event) {{
            if (!event || event.target.id === 'codeModal' || event.target.classList.contains('close-btn')) {{
                document.getElementById('codeModal').classList.remove('show');
                currentCodeIndex = -1;
            }}
        }}
        
        // Close modal with Escape key
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') closeModal();
        }});
        
        function filterTable() {{
            searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const rows = document.querySelectorAll('#tableBody tr');
            let visibleCount = 0;
            
            rows.forEach(row => {{
                const text = row.textContent.toLowerCase();
                if (text.includes(searchTerm)) {{
                    row.classList.remove('hidden');
                    visibleCount++;
                }} else {{
                    row.classList.add('hidden');
                }}
            }});
            
            document.getElementById('visibleCount').textContent = visibleCount;
        }}
        
        function sortTable(columnIndex) {{
            const tbody = document.getElementById('tableBody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const headers = document.querySelectorAll('th.sortable');
            
            // Check if same column clicked
            const ascending = currentSort.column !== columnIndex || !currentSort.ascending;
            
            rows.sort((a, b) => {{
                let aText = a.cells[columnIndex].textContent.trim();
                let bText = b.cells[columnIndex].textContent.trim();
                
                // Date column special handling
                if (columnIndex === 2) {{
                    const aDate = new Date(aText);
                    const bDate = new Date(bText);
                    if (!isNaN(aDate) && !isNaN(bDate)) {{
                        return ascending ? aDate - bDate : bDate - aDate;
                    }}
                }}
                
                // String comparison
                const comp = aText.localeCompare(bText);
                return ascending ? comp : -comp;
            }});
            
            // Re-append rows
            rows.forEach(row => tbody.appendChild(row));
            
            // Update header indicators
            headers.forEach((header, idx) => {{
                header.classList.remove('sort-asc', 'sort-desc');
            }});
            
            if (headers[columnIndex]) {{
                headers[columnIndex].classList.add(ascending ? 'sort-asc' : 'sort-desc');
            }}
            
            currentSort = {{column: columnIndex, ascending: ascending}};
        }}
        
        function sortByName() {{
            sortTable(0);
        }}
        
        function sortByDate() {{
            sortTable(2);
        }}
        
        function resetSort() {{
            location.reload();
        }}
    </script>
</body>
</html>
'''
    
    try:
        with open(OUTFILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ Website generated: {OUTFILE}")
        print(f"🎉 Open {OUTFILE} in your browser!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()