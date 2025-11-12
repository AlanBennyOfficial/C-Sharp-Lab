import os
import subprocess
from datetime import datetime
import html

REPO_PATH = "C-Sharp-Lab"  # Path to your local repo
OUTFILE = "index.html"

def get_git_timestamp(filepath):
    """Get the last commit date for a file in YYYY-MM-DD HH:MM:SS format."""
    try:
        out = subprocess.check_output([
            "git", "log", "-1", "--format=%cI", "--", filepath
        ], cwd=REPO_PATH, encoding="utf-8").strip()
        return out if out else ""
    except Exception:
        return ""

programs = []
for root, dirs, files in os.walk(REPO_PATH):
    for file in files:
        if file == "Program.cs":
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, REPO_PATH)
            timestamp = get_git_timestamp(rel_path)
            name = os.path.basename(os.path.dirname(full_path))
            with open(full_path, encoding="utf-8") as f:
                code = f.read()
            programs.append({
                "name": name,
                "path": rel_path,
                "date": timestamp,
                "code": code
            })

# Prepare HTML table rows
def row(prog, idx):
    # Make HTML-safe and add ID for modal/view
    return f'''
    <tr>
        <td>{html.escape(prog["name"])}</td>
        <td>{html.escape(prog["path"])}</td>
        <td>{html.escape(prog["date"])}</td>
        <td>
            <button onclick="viewCode({idx})">View</button>
        </td>
    </tr>
    '''

rows_html = "\n".join(row(prog, idx) for idx, prog in enumerate(programs))

# For modal source viewing
codes_js_array = "[" + ",".join(
    '"' + html.escape(prog["code"]).replace("\n", "\\n").replace('"', '\\"') + '"' for prog in programs
) + "]"

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>C# Program.cs Browser</title>
    <style>
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f7f7f7; }}
    h1 {{ padding: 1em; margin: 0; background:#333; color:#fff; }}
    table {{ border-collapse: collapse; width: 90%; margin: 2em auto; background: #fff; }}
    th, td {{ border: 1px solid #ccc; padding: .5em 1em; }}
    th {{ cursor: pointer; background-color: #eee; }}
    tr:hover td {{ background: #f0f8ff; }}
    button {{ font-size: 1em; padding: 0.3em 0.8em; }}
    .modal {{
        display: none; position: fixed; z-index: 1001; left: 0; top: 0; width: 100%; height: 100%;
        background: rgba(0,0,0,.7); align-items: center; justify-content: center;
    }}
    .modal-content {{
        background: #fff; padding: 2em; max-width: 80vw; max-height: 80vh; overflow: auto; border-radius: 10px;
    }}
    pre {{ white-space: pre-wrap; word-break: break-all; background: #eee; padding:1em; max-height: 60vh; overflow:auto; }}
    .close-btn {{ float:right; font-size:1.5em; margin:-1em -1em 0 0; cursor:pointer; }}
    </style>
</head>
<body>
    <h1>C# Program.cs Files (Sortable Table)</h1>
    <table id="progTable">
        <thead>
            <tr>
                <th onclick="sortTable(0)">Project/Folder &#8597;</th>
                <th onclick="sortTable(1)">Relative Path &#8597;</th>
                <th onclick="sortTable(2)">Last Commit Date &#8597;</th>
                <th>View Source</th>
            </tr>
        </thead>
        <tbody>
            {rows_html}
        </tbody>
    </table>
    <div id="codeModal" class="modal" onclick="closeModal(event)">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal(event)">&times;</span>
            <pre id="codeViewer"></pre>
        </div>
    </div>
<script>
let codes = {codes_js_array};
// Table sort
function sortTable(n) {{
    let table = document.getElementById("progTable");
    let rows = Array.from(table.rows).slice(1); // skip header
    let asc = !table.dataset['sort'+n] || table.dataset['sort'+n]=='desc';
    rows.sort(function(a, b) {{
        let x = a.cells[n].innerText.toLowerCase();
        let y = b.cells[n].innerText.toLowerCase();
        // For date column: compare ISO string
        if(n==2) return asc ? x.localeCompare(y) : y.localeCompare(x);
        return asc ? (x>y?1:x<y?-1:0) : (y>x?1:y<x?-1:0);
    }});
    table.tBodies[0].innerHTML = '';
    for(let r of rows) table.tBodies[0].appendChild(r);
    table.dataset['sort'+n] = asc?'asc':'desc';
}}
// Code viewer modal
function viewCode(idx) {{
    document.getElementById('codeViewer').innerText = codes[idx];
    document.getElementById('codeModal').style.display = 'flex';
}}
function closeModal(e) {{
    if(e.target.id == "codeModal" || e.target.classList.contains('close-btn')) {{
        document.getElementById('codeModal').style.display = 'none';
    }}
}}
</script>
</body>
</html>
"""

with open(OUTFILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Website created: {OUTFILE}. Open it in your browser!")