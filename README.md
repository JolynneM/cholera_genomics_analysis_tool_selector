# cholera_bioinformatics_tool_selector
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bioinformatics Tool Selector</title>
    <style>
        :root {
            --primary: #2563eb;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #1e293b;
            --border: #e2e8f0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        h1 { text-align: center; color: var(--primary); margin-bottom: 30px; }
        
        .form-group { margin-bottom: 20px; }
        label { display: block; font-weight: 600; margin-bottom: 8px; }
        
        select, input {
            width: 100%;
            padding: 10px;
            border: 1px solid var(--border);
            border-radius: 6px;
            font-size: 16px;
        }

        button {
            width: 100%;
            background-color: var(--primary);
            color: white;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.2s;
            font-weight: bold;
        }

        button:hover { background-color: #1d4ed8; }

        #results { margin-top: 30px; display: none; }
        
        .result-card {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            background: #fff;
            border-left: 5px solid var(--primary);
        }

        .result-card.top { border-left-color: #10b981; background: #f0fdf4; }
        
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 5px;
            color: white;
        }
        .badge-cost { background: #64748b; }
        .badge-type { background: #3b82f6; }

        .error-msg {
            color: #ef4444;
            background: #fef2f2;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #fecaca;
            display: none;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🧬 Bioinformatics Tool Selector</h1>
    <p style="text-align:center; color:#64748b;">Select your constraints to find the best platform.</p>

    <div class="form-group">
        <label for="inputFile">Input File Type</label>
        <select id="inputFile">
            <option value="FASTA">FASTA (Sequence only)</option>
            <option value="FASTQ">FASTQ (Raw Reads)</option>
            <option value="BAM">BAM (Aligned Reads)</option>
            <option value="VCF">VCF (Variants)</option>
            <option value="Mixed">Mixed / Multiple Formats</option>
        </select>
    </div>

    <div class="form-group">
        <label for="expertise">User Expertise</label>
        <select id="expertise">
            <option value="GUI">Graphical Interface (No Coding)</option>
            <option value="CLI">Command Line (Scripting/Python/Bash)</option>
            <option value="Mixed">Mixed (Comfortable with both)</option>
        </select>
    </div>

    <div class="form-group">
        <label for="infrastructure">Infrastructure</label>
        <select id="infrastructure">
            <option value="Cloud">Cloud (Web Browser)</option>
            <option value="Local">Local Machine / Laptop</option>
            <option value="HPC">HPC / Cluster</option>
            <option value="Any">Any / Flexible</option>
        </select>
    </div>

    <div class="form-group">
        <label for="funding">Funding Status</label>
        <select id="funding">
            <option value="None">No Budget (Must be Free/Open Source)</option>
            <option value="Institutional">Institutional Grant (Can pay for hosting)</option>
            <option value="Commercial">Commercial Budget (Subscription OK)</option>
        </select>
    </div>

    <div class="form-group">
        <label for="useCase">Primary Goal (Optional)</label>
        <select id="useCase">
            <option value="">-- Select if applicable --</option>
            <option value="Public Health">Public Health Surveillance</option>
            <option value="Cholera">Cholera / Specific Pathogen</option>
            <option value="Clinical">Clinical / Compliance</option>
            <option value="Education">Education / Learning</option>
            <option value="Reproducibility">Reproducibility / Standardization</option>
            <option value="Enterprise">Enterprise Security</option>
        </select>
    </div>

    <button onclick="analyzeTools()">Find Recommendations</button>

    <div id="errorMsg" class="error-msg"></div>
    <div id="results"></div>
</div>

<script>
    // Database derived from your CSV
    const tools = [
        { 
            name: "Pathogenwatch", 
            input: ["FASTA"], 
            gui: true, cli: false, 
            infra: ["Cloud"], 
            cost: "Free", 
            useCase: ["Public Health", "Surveillance", "Cholera"] 
        },
        { 
            name: "Terra", 
            input: ["FASTQ", "BAM", "VCF"], 
            gui: true, cli: true, 
            infra: ["Cloud"], 
            cost: "Paid", 
            useCase: ["Biomedical", "Large Scale", "Clinical"] 
        },
        { 
            name: "Galaxy", 
            input: ["FASTQ"], 
            gui: true, cli: true, 
            infra: ["Cloud", "Local"], 
            cost: "Free", 
            useCase: ["Education", "Accessible", "Reproducibility"] 
        },
        { 
            name: "DNAnexus", 
            input: ["FASTQ", "BAM"], 
            gui: true, cli: true, 
            infra: ["Cloud"], 
            cost: "Paid", 
            useCase: ["Clinical", "Enterprise", "Security"] 
        },
        { 
            name: "Climb", 
            input: ["All"], 
            gui: false, cli: true, 
            infra: ["Cloud", "Institutional"], 
            cost: "Institutional", 
            useCase: ["Microbiology", "Research"] 
        },
        { 
            name: "Cholgen (Bacpage)", 
            input: ["FASTA"], 
            gui: true, cli: false, 
            infra: ["Cloud"], 
            cost: "Free", 
            useCase: ["Cholera", "Typing"] 
        },
        { 
            name: "Bactopia", 
            input: ["FASTQ"], 
            gui: false, cli: true, 
            infra: ["Local", "HPC", "Cloud"], 
            cost: "Free", 
            useCase: ["Standardization", "Reproducibility", "Bacterial"] 
        },
        { 
            name: "Nfcore (Pathogen)", 
            input: ["FASTQ"], 
            gui: false, cli: true, 
            infra: ["Local", "Cloud"], 
            cost: "Free", 
            useCase: ["Reproducibility", "Standardization", "Public Health"] 
        },
        { 
            name: "IRIDA", 
            input: ["FASTQ"], 
            gui: true, cli: false, 
            infra: ["Local", "Institutional"], 
            cost: "Hosting Required", 
            useCase: ["Public Health", "Data Management"] 
        },
        { 
            name: "Centre for Genomic Epidemiology", 
            input: ["FASTA", "FASTQ"], 
            gui: true, cli: false, 
            infra: ["Cloud"], 
            cost: "Free", 
            useCase: ["Typing", "AMR Prediction"] 
        },
        { 
            name: "Choleraseq", 
            input: ["FASTQ"], 
            gui: false, cli: true, 
            infra: ["Local", "HPC"], 
            cost: "Free", 
            useCase: ["Cholera", "Pipeline"] 
        },
        { 
            name: "BaseSpace / Illumina", 
            input: ["FASTQ"], 
            gui: true, cli: false, 
            infra: ["Cloud"], 
            cost: "Paid", 
            useCase: ["Illumina Ecosystem", "Management"] 
        }
    ];

    function analyzeTools() {
        const userInput = {
            file: document.getElementById('inputFile').value,
            exp: document.getElementById('expertise').value,
            infra: document.getElementById('infrastructure').value,
            fund: document.getElementById('funding').value,
            useCase: document.getElementById('useCase').value
        };

        let candidates = [...tools];
        let errorMsg = "";

        // 1. Filter by Input File
        candidates = candidates.filter(t => {
            if (t.input.includes("All")) return true;
            if (userInput.file === "Mixed") return true; // Assume mixed accepts most
            return t.input.includes(userInput.file);
        });

        // 2. Filter by Expertise
        if (userInput.exp === "GUI") {
            candidates = candidates.filter(t => t.gui);
        } else if (userInput.exp === "CLI") {
            candidates = candidates.filter(t => t.cli);
        }

        // 3. Filter by Infrastructure
        if (userInput.infra !== "Any") {
            candidates = candidates.filter(t => t.infra.includes(userInput.infra));
        }

        // 4. Filter by Funding
        if (userInput.fund === "None") {
            candidates = candidates.filter(t => t.cost === "Free");
        } else if (userInput.fund === "Institutional") {
            // Keep Free, Institutional, and Paid (assuming grant covers it)
            // But exclude pure commercial subscriptions if they are very expensive? 
            // For now, keep everything except "Free" only if they specifically want free.
            // Actually, let's just keep Free + Institutional + Paid
            // If they said "None", we already filtered.
        }
        // If Commercial, keep all.

        // 5. Scoring
        candidates.forEach(t => {
            t.score = 0;
            // Bonus for specific use case match
            if (userInput.useCase && t.useCase.includes(userInput.useCase)) {
                t.score += 10;
            }
            // Bonus for Cholera specific if selected
            if (userInput.useCase === "Cholera" && (t.name.includes("Chol") || t.name === "Pathogenwatch")) {
                t.score += 15;
            }
            // Bonus for Public Health
            if (userInput.useCase === "Public Health" && t.useCase.includes("Public Health")) {
                t.score += 12;
            }
        });

        // Sort
        candidates.sort((a, b) => b.score - a.score);

        // Display
        const resultDiv = document.getElementById('results');
        const errorDiv = document.getElementById('errorMsg');
        resultDiv.innerHTML = "";
        errorDiv.style.display = "none";
        resultDiv.style.display = "block";

        if (candidates.length === 0) {
            errorDiv.style.display = "block";
            errorDiv.innerHTML = "<strong>No exact matches found.</strong><br>Try relaxing your constraints (e.g., allow 'Mixed' input or 'Cloud' infrastructure).";
            resultDiv.style.display = "none";
            return;
        }

        // Render Top 3
        candidates.slice(0, 3).forEach((tool, index) => {
            const isTop = index === 0;
            const cardClass = isTop ? "result-card top" : "result-card";
            
            let desc = "";
            if (tool.useCase.length > 0) desc = `Best for: ${tool.useCase.join(", ")}`;
            else desc = "General purpose analysis";

            const html = `
                <div class="${cardClass}">
                    <h3>${isTop ? "🏆 Top Recommendation:" : "Alternative:"} ${tool.name}</h3>
                    <p><strong>${desc}</strong></p>
                    <p><span class="badge badge-type">Input: ${tool.input.join(", ")}</span>
                       <span class="badge badge-cost">Cost: ${tool.cost}</span>
                       <span class="badge badge-type">${tool.gui ? "GUI" : ""} ${tool.cli ? "CLI" : ""}</span>
                    </p>
                    <p style="font-size: 0.9em; color: #555;">
                        Infrastructure: ${tool.infra.join(", ")}
                    </p>
                </div>
            `;
            resultDiv.innerHTML += html;
        });
    }
</script>

</body>
</html>
