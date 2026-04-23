import streamlit as st

# --- 1. THE ENRICHED DATABASE (FIXED TEXT MATCHES) ---
# Updated 'use_case' lists to EXACTLY match the UI selection options
TOOLS = [
    {
        "name": "Pathogenwatch (Vibriowatch)", 
        "input": ["FASTA", "FASTQ"], 
        "Web browser": True, "Command line": False, 
        "infra": ["Cloud computing"], 
        "cost": "Free", 
        # FIXED: Changed "Transmission assessment" to "Transmission dynamics assessment"
        "use_case": ["Strain identification", "AMR assessment", "Transmission dynamics assessment"],
        "sharing": "Yes (can share collections)",
        "governance": "User-controlled sharing",
        "url": "https://pathogen.watch",
        "platform_type": "Platform",
        "developed_for": "Public health surveillance and genomic epidemiology",
        "interaction": "Integrated, fixed analysis pipeline (limited user control)",
        "capabilities": {
            "Quality control": "No", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "Yes", "Variant calling": "Yes",
            "Serotyping": "Yes", "Lineage classification": "Yes", "MLST": "Yes", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "Terra", 
        "input": ["FASTA", "FASTQ"], 
        "Web browser": True, "Command line": True, 
        "infra": ["Cloud computing"], 
        "cost": "Paid", 
        # FIXED: Changed "Transmission assessment" and "Other analysis" to match UI
        "use_case": ["Strain identification", "AMR assessment", "Transmission dynamics assessment", "Other analyses"],
        "sharing": "Yes (can share workspaces)",
        "governance": "Controlled-access cloud environment",
        "url": "https://terra.bio/",
        "platform_type": "Platform",
        "developed_for": "Scalable biomedical data analysis in the cloud",
        "interaction": "User selects and runs workflows/pipelines (high flexibility)",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "Yes", "Variant calling": "Yes",
            "Serotyping": "Yes", "Lineage classification": "Yes", "MLST": "Yes", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "Galaxy", 
        "input": ["FASTQ", "FASTA"], 
        "Web browser": True, "Command line": True, 
        "infra": ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing"], 
        "cost": "Free", 
        # FIXED: Changed "Transmission assessment" to "Transmission dynamics assessment"
        "use_case": ["Strain identification", "AMR assessment", "Transmission dynamics assessment"],
        "sharing": "Yes (can share histories/workflows)",
        "governance": "Instance-dependent",
        "url": "https://usegalaxy.org/",
        "platform_type": "Platform",
        "developed_for": "Making bioinformatics accessible without coding",
        "interaction": "User builds or selects workflows from modular tools (GUI-based)",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "Yes", "Variant calling": "Yes",
            "Serotyping": "Yes", "Lineage classification": "Yes", "MLST": "Yes", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "DNAnexus", 
        "input": ["FASTQ", "FASTA"], 
        "Web browser": True, "Command line": True, 
        "infra": ["Cloud computing"], 
        "cost": "Paid", 
        # FIXED: Changed "Transmission assessment" and "Other analysis" to match UI
        "use_case": ["Strain identification", "AMR assessment", "Transmission dynamics assessment", "Other analyses"],
        "sharing": "Yes (can bring in people to collaborate)",
        "governance": "Enterprise-grade governance",
        "url": "https://www.dnanexus.com/",
        "platform_type": "Platform",
        "developed_for": "Enterprise-scale, secure genomic data analysis",
        "interaction": "User selects and runs workflows/apps (cloud-executed pipelines)",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "Yes", "Variant calling": "Yes",
            "Serotyping": "Yes", "Lineage classification": "Yes", "MLST": "Yes", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "Cholgen (Bacpage)", 
        "input": ["FASTA"], 
        "Web browser": False, "Command line": True, 
        "infra": ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["AMR assessment", "Transmission dynamics assessment"],
        "sharing": "Not applicable/No",
        "governance": "Data uploaded to external servers",
        "url": "https://github.com/CholGen/bacpage",
        "platform_type": "Pipeline",
        "developed_for": "Cholera-specific genomic analysis and typing",
        "interaction": "Pipeline",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "No", 
            "AMR profiling": "Yes", "Virulence genes profiling": "No", "Variant calling": "Yes",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "Yes", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "Bagep", 
        "input": ["FASTQ"], 
        "Web browser": False, "Command line": True, 
        "infra": ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["AMR assessment", "Transmission dynamics assessment"],
        "sharing": "Not applicable/No",
        "governance": "Data handled entirely by user",
        "url": "https://github.com/idolawoye/BAGEP",
        "platform_type": "Pipeline",
        "developed_for": "Automated workflow for downstream analysis of bacterial genome sequences",
        "interaction": "Pipeline",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "No", "Variant calling": "Yes",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "No", "Phylogenetic tree construction": "Yes"
        }
    },
    {
        "name": "Bactopia", 
        "input": ["FASTQ"], 
        "Web browser": False, "Command line": True, 
        "infra": ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["AMR assessment"],
        "sharing": "Not applicable/No",
        "governance": "Data handled entirely by user",
        "url": "https://github.com/bactopia/bactopia",
        "platform_type": "Pipeline",
        "developed_for": "Standardised bacterial genome analysis workflows",
        "interaction": "Configurable pipeline",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "Yes", 
            "AMR profiling": "Yes", "Virulence genes profiling": "Yes", "Variant calling": "Yes",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "Yes", "Phylogenetic tree construction": "No"
        }
    },
    
    {
        "name": "IRIDA", 
        "input": ["FASTQ"], 
        "Web browser": True, "Command line": False, 
        "infra": ["Cloud computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["Strain identification", "AMR assessment"],
        "sharing": "Yes (can share between instance)",
        "governance": "Data ownership remains with institution",
        "url": "https://irida.ca/",
        "platform_type": "Platform",
        "developed_for": "Public health genomics data management and analysis",
        "interaction": "Platform with selectable, integrated pipelines (managed workflows)",
        "capabilities": {
            "Quality control": "No", "Assembly": "Yes", "Taxonomy assessment": "No", 
            "AMR profiling": "Yes", "Virulence genes profiling": "No", "Variant calling": "Yes",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "Yes", "Phylogenetic tree construction": "No"
        }
    },
    {
        "name": "Centre for Genomic Epidemiology", 
        "input": ["FASTA", "FASTQ"], 
        "Web browser": True, "Command line": False, 
        "infra": ["Cloud computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["Strain identification", "AMR assessment"],
        "sharing": "Not applicable/No",
        "governance": "Data uploaded to external servers",
        "url": "https://www.genomicepidemiology.org/",
        "platform_type": "Platform",
        "developed_for": "Easy access to typing and AMR prediction tools",
        "interaction": "Collection of specialised tools (not a single pipeline)",
        "capabilities": {
            "Quality control": "No", "Assembly": "No", "Taxonomy assessment": "No", 
            "AMR profiling": "Yes", "Virulence genes profiling": "No", "Variant calling": "No",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "Yes", "Phylogenetic tree construction": "No"
        }
    },
    {
        "name": "Choleraseq", 
        "input": ["FASTQ"], 
        "Web browser": False, "Command line": True, 
        "infra": ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing"], 
        "cost": "Free", 
        # Already correct
        "use_case": ["Transmission dynamics assessment"],
        "sharing": "Not applicable/No",
        "governance": "Data handled entirely by user",
        "url": "https://github.com/CERI-KRISP/CholeraSeq",
        "platform_type": "Pipeline",
        "developed_for": "Cholera-specific genomic analysis pipeline",
        "interaction": "Pipeline",
        "capabilities": {
            "Quality control": "Yes", "Assembly": "Yes", "Taxonomy assessment": "No", 
            "AMR profiling": "No", "Virulence genes profiling": "No", "Variant calling": "Yes",
            "Serotyping": "No", "Lineage classification": "No", "MLST": "No", "Phylogenetic tree construction": "Yes"
        }
    },
    
]

# --- 2. THE LOGIC FUNCTION ---
def analyze(file_type, expertise, infrastructure, funding, sharing_pref, required_goals):
    candidates = []
    
    # 1. Filter Input
    for t in TOOLS:
        if "All" in t["input"] or file_type in t["input"] or file_type == "Either":
            candidates.append(t)
    
    # 2. Filter Expertise
    if expertise == "Web browser":
        candidates = [t for t in candidates if t["Web browser"]]
    elif expertise == "Command line":
        candidates = [t for t in candidates if t["Command line"]]
    
    # 3. Filter Infrastructure
    if infrastructure != "Any":
        candidates = [t for t in candidates if infrastructure in t["infra"]]
    
    # 4. Filter Funding Access
    if funding == "No":
        candidates = [t for t in candidates if t["cost"] == "Free"]
    elif funding == "Yes":
        pass

    # 5. Filter Data Sharing Preference
    if sharing_pref != "Any":
        if sharing_pref == "Yes":
            candidates = [t for t in candidates if t["sharing"].lower().startswith("yes")]
        elif sharing_pref == "No":
            candidates = [t for t in candidates if "no" in t["sharing"].lower()]

    # 6. STRICT FILTER FOR GOALS (MATCH ALL)
    # Now that the text matches exactly, this will work correctly.
    if required_goals:
        candidates = [
            t for t in candidates 
            if all(goal in t["use_case"] for goal in required_goals)
        ]

    # 7. Scoring
    for t in candidates:
        t["score"] = 0
        if required_goals:
            matches = sum(1 for g in required_goals if g in t["use_case"])
            t["score"] += matches * 10
        
        # Bonus for Cholera specific
        if any("Cholera" in g for g in required_goals) and ("Chol" in t["name"] or "Vibrio" in t["name"]):
            t["score"] += 15
            
    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:3]

# --- 3. THE STREAMLIT UI ---
st.set_page_config(page_title="Bio Tool Selector", page_icon="🧬")
st.title("Simple decision support framework for cholera genomics analysis tool selection")
st.markdown("Select aspects available to you to help you select a suitable platform for data analysis.")

col1, col2 = st.columns(2)
with col1:
    file_type = st.selectbox("What input file do you have?", ["FASTA", "FASTQ", "Either"])
    expertise = st.selectbox("How do you prefer to carry out your analysis?", ["Web browser", "Command line", "Either"])
with col2:
    infrastructure = st.selectbox("What infrastructure is available to you?", ["Cloud computing", "Local computing (e.g laptops, desktops, or workstations using their own built-in compute resources)", "High-performance computing", "Any"])
    funding = st.selectbox("Do you have funding to support computing?", ["Yes", "No"])

# Data Sharing Filter
sharing_pref = st.selectbox("Data Sharing Requirement", ["Any", "Yes", "No"])

# UI Options (These MUST match the database exactly)
available_goals = ["Strain identification", "AMR assessment", "Transmission dynamics assessment", "Other analyses"]
selected_goals = st.multiselect("Use case", available_goals, default=[])

if st.button("Find Recommendations", type="primary"):
    with st.spinner("Analyzing tools..."):
        results = analyze(file_type, expertise, infrastructure, funding, sharing_pref, selected_goals)
    
    if not results:
        st.error("No matching tools found. Try relaxing your constraints (e.g., remove a goal or change infrastructure).")
    else:
        st.success(f"Found {len(results)} recommendations that meet ALL your selected criteria!")
        
        for i, tool in enumerate(results, 1):
            is_top = (i == 1)
            with st.expander(f"{'Top Pick' if is_top else 'Alternative'}: {tool['name']}", expanded=is_top):
                st.markdown(f"**Best for:** {', '.join(tool['use_case'])}")
                st.markdown(f"**Developed for:** {tool['developed_for']}")
                st.markdown(f"**Type:** {tool['platform_type']}")
                st.markdown(f"**How it works:** {tool['interaction']}")
                st.markdown(f"**Cost:** {tool['cost']}")
                
                has_web = tool.get("Web browser", False)
                has_cli = tool.get("Command line", False)
                
                if has_web and has_cli:
                    interface_text = "Web browser & Command line"
                elif has_web:
                    interface_text = "Web browser"
                elif has_cli:
                    interface_text = "Command line"
                else:
                    interface_text = "Unknown"
                    
                st.markdown(f"**Interface:** {interface_text}")
                
                st.markdown("---")
                st.markdown("**Data Governance & Sharing:**")
                st.markdown(f"- **Sharing:** {tool.get('sharing', 'Not specified')}")
                st.markdown(f"- **Governance:** {tool.get('governance', 'Not specified')}")
                
                st.markdown("---")
                st.markdown("**Capabilities (What it does/does not do):**")
                caps = tool.get("capabilities", {})
                cap_list = []
                for k, v in caps.items():
                    status = "✘" if v == "No" else "✔️"
                    cap_list.append(f"{k}: {status}&nbsp;&nbsp;&nbsp;")
                
                st.markdown("".join(cap_list))
                
                st.markdown("---")
                st.markdown("**Visit Platform:**")
                st.markdown(f"[Open {tool['name']}]({tool.get('url', '#')})")
