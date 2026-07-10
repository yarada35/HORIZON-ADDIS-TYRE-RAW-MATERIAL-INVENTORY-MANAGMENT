# ----------------------------------------------------
# 🧮 LOGIC ENGINE: ROBUST NORMALIZED COLUMN MATCHING
# ----------------------------------------------------
def normalize_string(s):
    """Removes all spaces, hyphens, slashes, and forces lowercase for resilient matching"""
    if not isinstance(s, str):
        return ""
    return "".join(c for c in s.lower() if c.isalnum())

mrp_rows = []
total_batch_kg_day = 0
critical_alarms = 0
warning_alarms = 0

scale_ratio = production_plan_pcs / 450.0

# Find the recipe column using normalized fuzzy matching
target_col = None
if selected_size:
    norm_selected = normalize_string(selected_size)
    for col in df_cpd_tyre.columns:
        if normalize_string(col) == norm_selected:
            target_col = col
            break

# Process each material configuration row
for idx, row in df_planning.iterrows():
    mat_name = str(row["Material Name"]).strip()
    beg_stock = row["Beg Stock"]
    wip_stock = row["WIP Stock"]
    base_add = row["Base ADD"]
    
    # Extract formulation weight using the normalized column reference
    raw_weight_value = 0.0
    if target_col:
        # Cross-reference the raw materials/compounds rows
        matching_rows = df_cpd_tyre[df_cpd_tyre["Compound Type"].astype(str).str.strip().str.lower() == mat_name.lower()]
        if not matching_rows.empty:
            val = pd.to_numeric(matching_rows.iloc[0][target_col], errors='coerce')
            if not pd.isna(val):
                raw_weight_value = val

    # Calculate operational requirements
    calculated_add = base_add * scale_ratio * raw_weight_value
    total_current_stock = beg_stock + wip_stock
    total_batch_kg_day += calculated_add
    
    if calculated_add > 0:
        running_days_coverage = round(total_current_stock / calculated_add)
    else:
        running_days_coverage = 999

    if calculated_add == 0:
        status_badge = "<span class='badge-safe'>- NO DEMAND</span>"
    elif running_days_coverage <= 15:
        critical_alarms += 1
        status_badge = "<span class='badge-crit'>❌ CRITICAL</span>"
    elif running_days_coverage <= 30:
        warning_alarms += 1
        status_badge = "<span class='badge-warn'>⚠️ WARNING</span>"
    elif running_days_coverage <= lookahead_days:
        status_badge = "<span class='badge-awake'>💡 AWAKENING</span>"
    else:
        status_badge = "<span class='badge-safe'>✓ SAFE</span>"

    mrp_rows.append({
        "Material Component": mat_name,
        "Current Stock Balance (Kg)": f"{round(total_current_stock):,}",
        "Daily Demand ADD (Kg)": f"{round(calculated_add):,}",
        "Runway Coverage": f"<b>{running_days_coverage if calculated_add > 0 else '—'} Days</b>",
        "Alarm Status": status_badge,
        "30-Day Demand (Kg)": f"{round(calculated_add * 30):,}",
        "60-Day Demand (Kg)": f"{round(calculated_add * 60):,}",
        "90-Day Demand (Kg)": f"{round(calculated_add * 90):,}",
        "150-Day Demand (Kg)": f"{round(calculated_add * 150):,}"
    })

df_mrp_display = pd.DataFrame(mrp_rows)

# ... [Keep your existing KPI Cards layout section here] ...
