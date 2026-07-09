# Save this file as app.py
from flask import Flask, jsonify, request, render_template_string
import json

app = Flask(__name__)

# Master structures derived from your physical factory configurations
PRODUCTION_MATRIX = {
    "1200-20 NB-72 18PR": { "compound": "ILC-FM / KIP-FM" },
    "1100-20 HT-90 16/18PR": { "compound": "KIP-FM / LN-6647" },
    "8.25-16 HT-40 16PR": { "compound": "LN-6647 / 073-FM" },
    "750-16 16PR HT-90": { "compound": "KIP-FM / 073-FM" },
    "750-16 AT-20 14PR": { "compound": "ILC-FM / 073-FM" }
}

COMPOUND_RAW_MATERIALS = {
    "ILC-FM / KIP-FM": [
        { "material": "SMR-20 (SIR /SMR-20)", "dailyBase": 9083.55, "baseBeg": 236172, "baseWip": 45000 },
        { "material": "BEBEKA RUBBER (SMR-20)", "dailyBase": 13.11, "baseBeg": 340, "baseWip": 50 },
        { "material": "BR 1220 (SKD-2)", "dailyBase": 1174.57, "baseBeg": 30538, "baseWip": 5000 },
        { "material": "SBR 1500 (Kralex 1500)", "dailyBase": 461.47, "baseBeg": 11998, "baseWip": 2500 }
    ],
    "KIP-FM / LN-6647": [
        { "material": "SMR-20 (SIR /SMR-20)", "dailyBase": 9083.55, "baseBeg": 236172, "baseWip": 45000 },
        { "material": "SBR 1712 (Kralex 1712)", "dailyBase": 590.77, "baseBeg": 15359, "baseWip": 2200 },
        { "material": "EXXON CHLOROBUTYL 1066", "dailyBase": 64.44, "baseBeg": 1675, "baseWip": 300 }
    ]
}

@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify({"sizes": list(PRODUCTION_MATRIX.keys())})

@app.route('/api/calculate', methods=['POST'])
def calculate_mrp():
    data = request.json
    selected_size = data.get('size')
    daily_plan = float(data.get('daily_plan', 450))
    beg_mod = float(data.get('beg_modifier', 1.0))
    wip_mod = float(data.get('wip_modifier', 1.0))

    if selected_size not in PRODUCTION_MATRIX:
        return jsonify({"error": "Size missing from master mapping"}), 400

    compound_code = PRODUCTION_MATRIX[selected_size]["compound"]
    materials = COMPOUND_RAW_MATERIALS.get(compound_code, [])
    
    calculated_rows = []
    global_stock = 0
    active_alarms = 0

    for item in materials:
        total_stock = (item["baseBeg"] * beg_mod) + (item["baseWip"] * wip_mod)
        global_stock += total_stock
        daily_consumption = item["dailyBase"] * (daily_plan / 450.0)

        running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0

        # Run exact multi-horizon checking loops
        horizons = [15, 30, 60, 90, 150]
        alarm_status = {f"alarm_{h}": "ALARM" if running_days <= h else "OK" for h in horizons}
        
        for h in horizons:
            if running_days <= h:
                active_alarms += 1

        row_data = {
            "material": item["material"],
            "total_stock": round(total_stock),
            "daily_consumption": round(daily_consumption),
            "running_days": running_days,
            **alarm_status
        }
        calculated_rows.append(row_data)

    return jsonify({
        "compound": compound_code,
        "summary_daily": daily_plan,
        "summary_monthly": daily_plan * 30,
        "summary_stock": round(global_stock),
        "summary_alarms": active_alarms,
        "breakdown": calculated_rows
    })

if __name__ == '__main__':
    # Listen on port 5000 across local networks
    app.run(host='0.0.0.0', port=5000, debug=True)
