import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="Electricity_Demand_Solar_Forecasting_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Color Palette Definitions
    DARK_BG = RGBColor(15, 23, 42)       # Slate 900
    LIGHT_BG = RGBColor(248, 250, 252)   # Slate 50
    CARD_BG = RGBColor(255, 255, 255)    # White
    CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    
    TEXT_DARK = RGBColor(15, 23, 42)     # Slate 900
    TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    TEXT_LIGHT = RGBColor(255, 255, 255) # White
    
    ACCENT_TEAL = RGBColor(13, 148, 136) # Teal 600
    ACCENT_BLUE = RGBColor(2, 132, 199)  # Sky 600
    ACCENT_AMBER = RGBColor(217, 119, 6) # Amber 600
    ACCENT_GREEN = RGBColor(22, 163, 74) # Green 600
    ACCENT_PURPLE = RGBColor(147, 51, 234) # Purple 600
    
    def add_header(slide, title_text, category_tag, dark_theme=False):
        # Header banner shape
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.85))
        banner.fill.background()
        banner.line.color.rgb = CARD_BORDER if not dark_theme else RGBColor(30, 41, 59)
        banner.line.width = Pt(0)
        
        tf = banner.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_AMBER if dark_theme else ACCENT_BLUE
        
        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT if dark_theme else TEXT_DARK
        
        # Bottom dividing accent line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = ACCENT_TEAL if not dark_theme else ACCENT_AMBER
        line.line.width = Pt(0)

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    def add_card_text(card, title, bullets, title_color=TEXT_DARK, title_size=15, bullet_size=12.5):
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(title_size)
        p.font.bold = True
        p.font.color.rgb = title_color
        p.space_after = Pt(8)
        
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(bullet_size)
            pb.font.color.rgb = TEXT_DARK
            pb.space_after = Pt(5)

    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide (Dark Theme)
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_BG
    bg1.line.width = Pt(0)
    
    # Accent top stripe
    stripe = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.08))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = ACCENT_AMBER
    stripe.line.width = Pt(0)
    
    # Main Title Frame
    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "Short-Term Electricity Demand and Solar Generation Forecasting for Grid Stability"
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(14)
    
    p_sub = tf1.add_paragraph()
    p_sub.text = "Predictive Analytics, Duck Curve Dynamics, Feeder Simulation, and Forecast-Informed Storage Optimization"
    p_sub.font.size = Pt(16.5)
    p_sub.font.color.rgb = RGBColor(148, 163, 184) # Slate 400
    p_sub.space_after = Pt(28)
    
    p_desc = tf1.add_paragraph()
    p_desc.text = "SolarCast-Grid Framework | Real SCADA Telemetry (2021–2025) | IEEE 33-Bus Feeder | HiGHS 24h LP"
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = ACCENT_TEAL
    p_desc.space_after = Pt(24)
    
    # Bottom meta card
    meta_card = add_card(s1, 0.8, 5.4, 11.733, 1.3, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tf_meta = meta_card.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = Inches(0.3)
    tf_meta.margin_top = Inches(0.2)
    
    pm1 = tf_meta.paragraphs[0]
    pm1.text = "Presenter: Piyush Agrawal   |   Affiliation: Department of Electrical & Computing Sciences"
    pm1.font.size = Pt(13.5)
    pm1.font.bold = True
    pm1.font.color.rgb = TEXT_LIGHT
    pm1.space_after = Pt(6)
    
    pm2 = tf_meta.add_paragraph()
    pm2.text = "Scientific Provenance Tags: [OBSERVED] SCADA  •  [DERIVED] Analytics  •  [FORECAST] ML  •  [SIMULATED] AC Power Flow  •  [OPTIMISED] LP"
    pm2.font.size = Pt(11)
    pm2.font.color.rgb = RGBColor(203, 213, 225)

    s1.notes_slide.notes_text_frame.text = (
        "Welcome everyone. Today I am presenting our work on Short-Term Electricity Demand and Solar Generation "
        "Forecasting for Grid Stability, encapsulated in the SolarCast-Grid framework. "
        "We address one of the most critical challenges facing the clean energy transition: how to translate macro-scale "
        "national SCADA forecasts into physical, violation-free storage schedules that stabilize local distribution grids."
    )

    # -------------------------------------------------------------------------
    # SLIDE 2: Problem Statement & Motivation
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "The Challenge: Solar Intermittency & Grid Stability Bottlenecks", "Problem Statement & Motivation")
    
    c1 = add_card(s2, 0.8, 1.6, 3.65, 5.2)
    add_card_text(c1, "1. Macro Solar Influx", [
        "Rapid expansion of variable solar PV across the Indian power grid.",
        "Solar share of daily energy grew from 6.4% (2021) to 9.3% (2025).",
        "Zero-marginal-cost solar displaces baseload during midday hours.",
        "Extreme non-linearity and weather sensitivity induce steep grid ramp events."
    ], title_color=ACCENT_AMBER)
    
    c2 = add_card(s2, 4.84, 1.6, 3.65, 5.2)
    add_card_text(c2, "2. The Indian Duck Curve", [
        "Midday 'belly' has permanently displaced nighttime minimum since 2022.",
        "Evening 3-hour net-load ramp escalated from 20.7 GW to 33.2 GW mean in 2025.",
        "Historical peak 3-hour ramp reached 50.6 GW (March 5, 2025).",
        "Requires massive ramping flexibility from thermal and hydro fleets."
    ], title_color=ACCENT_BLUE)
    
    c3 = add_card(s2, 8.88, 1.6, 3.65, 5.2)
    add_card_text(c3, "3. Local Feeder Crisis", [
        "High rooftop & distributed PV causes reverse power flow back into substations.",
        "Leads to severe overvoltage (V > 1.05 p.u.) and thermal line overloading.",
        "Forces massive, wasteful solar curtailment when export headroom is capped.",
        "Research Goal: Can ML forecasts guide BESS dispatch to eliminate curtailment?"
    ], title_color=ACCENT_TEAL)

    s2.notes_slide.notes_text_frame.text = (
        "Slide 2 outlines the motivation. The problem has two connected dimensions: "
        "First, at the national transmission level, rapid solar adoption creates the classic Duck Curve with a brutal 33 GW "
        "evening ramp. Second, at the local distribution feeder level, excess solar causes reverse power flow and overvoltage, "
        "forcing utilities to curtail clean energy. Our research bridges this gap by testing whether accurate machine learning "
        "forecasts can drive physical battery storage to mitigate both challenges simultaneously."
    )

    # -------------------------------------------------------------------------
    # SLIDE 3: SCADA Dataset & Robust Cleaning Pipeline
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Grid-India SCADA Telemetry & Rigorous Ingestion Pipeline", "Data Engineering [OBSERVED / DERIVED]")
    
    c_data = add_card(s3, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_data, "Data Integrity & Pipeline Architecture", [
        "Source: Grid-India / NERLDC SCADA via Mendeley Data (Sep 2021 – Jun 2025).",
        "Scale: 4,075,224 raw telemetry samples resampled to 33,432 clean hourly records.",
        "Hampel Spike Filter: Rolling median ± 6·MAD at raw resolution removes sensor noise.",
        "Solar Night Offset: Zeroed 11,144 night hours and eliminated nocturnal transducer drift.",
        "Physical Bounds & Zero Checks: Fixed negative solar; flagged dropouts.",
        "Leak-Free Splits: Chronological split into Train (2021–2024), Val (2024 H2), and Test (2025 H1).",
        "Provenance: Every variable explicitly classified as OBSERVED or DERIVED."
    ], title_color=ACCENT_TEAL, bullet_size=12)
    
    img3 = r"results\eda\02_hourly_profiles_by_year.png"
    if os.path.exists(img3):
        s3.shapes.add_picture(img3, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s3.notes_slide.notes_text_frame.text = (
        "Slide 3 describes the dataset. We built our framework on 4.07 million raw SCADA records from Grid-India spanning "
        "nearly four years. We applied a multi-stage cleaning pipeline: Hampel outlier filtering, removal of nighttime sensor drift, "
        "and hourly energy-consistent resampling. Crucially, we enforced strict chronological train-validation-test splits "
        "to ensure absolute leak-safety with zero lookahead bias."
    )

    # -------------------------------------------------------------------------
    # SLIDE 4: Duck Curve Dynamics & Surplus-Solar Risk Proxy
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Empirical Duck Curve Dynamics & Surplus-Solar Risk Proxy", "Grid Dynamics [DERIVED / SCENARIOS]")
    
    c_duck = add_card(s4, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_duck, "Empirical Findings & Capacity Scenarios", [
        "Diurnal Net-Load Inversion: Since 2022, net-load minimum occurs at 13:00 IST instead of 03:00 night.",
        "Ramp Escalation: Mean 3-hour evening ramp grew from 20.7 GW (2023) to 33.2 GW (2025).",
        "Peak Event: 50.6 GW ramp on 2025-03-05 (requires massive dispatchable response).",
        "Surplus-Solar Risk Formulation: Modeled inflexible generation floor F_t (CEA technical min 55%/40% + nuclear + run-of-river hydro).",
        "Current Fleet (k=1): Zero surplus hours observed in the historical fleet.",
        "Future Buildout (k=2): Surplus emerges at 0.20% of solar generation.",
        "Future Buildout (k=3): Surplus surges to 9.15% (requiring widespread storage)."
    ], title_color=ACCENT_AMBER, bullet_size=12)
    
    img4 = r"results\eda\07_duck_curve_seasonal.png"
    if os.path.exists(img4):
        s4.shapes.add_picture(img4, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s4.notes_slide.notes_text_frame.text = (
        "On Slide 4, we quantify India's emerging Duck Curve. The chart shows net load by hour across seasons. "
        "Notice the deep depression during the middle of the day and the steep ramp starting at 16:00. "
        "Our surplus risk proxy proves that while today's fleet barely faces curtailment, scaling solar by 2x to 3x "
        "causes surplus risk to leap to over 9% of total solar energy, making proactive storage deployment mandatory."
    )

    # -------------------------------------------------------------------------
    # SLIDE 5: Machine Learning Forecasting Methodology
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Multi-Horizon Machine Learning Forecasting Framework", "Predictive Analytics [FORECAST]")
    
    c_f1 = add_card(s5, 0.8, 1.6, 3.65, 5.2)
    add_card_text(c_f1, "Targets & Horizons", [
        "8 Core Prediction Tasks:",
        "• Solar Generation (MW)",
        "• Electricity Demand (MW)",
        "• Wind Generation (MW)",
        "• Net Load (MW)",
        "Two Operational Horizons:",
        "• 1-Hour Ahead (h=1): real-time balancing & ramp regulation.",
        "• Day-Ahead (h=14–37): 24h schedule issued at 10:00 IST on Day D for D+1."
    ], title_color=ACCENT_BLUE)
    
    c_f2 = add_card(s5, 4.84, 1.6, 3.65, 5.2)
    add_card_text(c_f2, "Leak-Safe Features", [
        "Strict Issue-Time Filtering: Only data up to 10:00 IST available for Day-Ahead.",
        "Calendar Harmonics: Sin/cos encoding for hour, weekday, day-of-year.",
        "Autoregressive Lags: 24h, 48h, 168h lags reflecting diurnal and weekly cycles.",
        "Rolling Statistics: Moving averages and standard deviations across past windows.",
        "Capacity Growth Proxy: Rolling 30-day maximum solar to track capacity expansion."
    ], title_color=ACCENT_TEAL)
    
    c_f3 = add_card(s5, 8.88, 1.6, 3.65, 5.2)
    add_card_text(c_f3, "Model Suite Benchmarked", [
        "Standard Baselines: Persistence and Seasonal-Naive (24h and 168h).",
        "Linear Regularization: Ridge regression with level-ratio scaling.",
        "Tree Ensembles: Random Forest and HistGradientBoosting.",
        "Advanced Gradient Boosters: LightGBM and XGBoost with early stopping.",
        "Deep Sequence Network: Multi-layer PyTorch LSTM sequence model.",
        "Conformal Prediction: 80% split-conformal prediction intervals."
    ], title_color=ACCENT_PURPLE)

    s5.notes_slide.notes_text_frame.text = (
        "Slide 5 outlines our forecasting methodology. We established a rigorous 8-task benchmark comparing baselines, "
        "linear Ridge, tree ensembles, LightGBM, XGBoost, and deep LSTM networks. Crucially, Day-Ahead models operate under "
        "real-world market rules: they are issued at 10:00 AM on Day D for the entirety of Day D+1, meaning leads range from 14 to 37 hours "
        "with zero subsequent data leakage."
    )

    # -------------------------------------------------------------------------
    # SLIDE 6: Forecasting Benchmark Results
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Forecasting Benchmark: Tree Ensembles Dominate Sequences", "Benchmark Results [FORECAST vs OBSERVED]")
    
    c_res = add_card(s6, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_res, "Out-of-Sample Test Evaluation", [
        "Solar Day-Ahead: HistGB selected; Test MAE = 1,277 MW (R² = 0.988).",
        "Solar 1-Hour Ahead: LightGBM selected; Test MAE = 559 MW (R² = 0.998), beating baseline by +47.0%.",
        "Demand Day-Ahead: XGBoost selected; Test MAE = 4,631 MW (R² = 0.887), beating baseline by +33.9%.",
        "Demand 1-Hour Ahead: LightGBM selected; Test MAE = 1,427 MW (R² = 0.989), beating baseline by +67.6%.",
        "Net Load 1-Hour Ahead: LightGBM achieves 2,016 MW MAE (+67.7% gain).",
        "Tabular vs Deep Learning: Boosted decision trees consistently outperformed the LSTM across all tasks.",
        "Weather Impact: Numerical weather prediction reduced day-ahead solar MAE by 10.5%."
    ], title_color=ACCENT_GREEN, bullet_size=12)
    
    img6 = r"results\figures\fc_model_comparison.png"
    if os.path.exists(img6):
        s6.shapes.add_picture(img6, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 presents our forecasting results on the 6-month out-of-sample test period. "
        "LightGBM and XGBoost dominated across the board. For 1-hour demand and net load, LightGBM achieved a massive 67% error reduction "
        "over standard operational baselines. Interestingly, the deep LSTM was not selected for any task—the tabular feature engineering "
        "allowed tree ensembles to generalize far better on this hourly tabular dataset."
    )

    # -------------------------------------------------------------------------
    # SLIDE 7: Distribution Feeder Modeling & Graph Analysis
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Distribution Grid Simulation: IEEE 33-Bus Feeder", "Power Systems [SIMULATED]")
    
    c_grid = add_card(s7, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_grid, "Feeder Parameterization & Graph Topology", [
        "Benchmark Feeder: IEEE / Baran-Wu 33-bus 12.66 kV network implemented in pandapower.",
        "Feeder Loading: Base peak load of 3.715 MW and 2.300 MVAr across 32 load buses.",
        "Distributed PV Buildout: 4 solar generation sites (1.5 MW each = 6.0 MW total, representing 161% solar penetration).",
        "Graph Topology (NetworkX): 37 branches, 5 tie switches, giving 50,751 valid radial configurations.",
        "Optimal Battery Siting: Graph betweenness centrality & loss sensitivity identified bus 14 as the optimal battery location.",
        "Network Reconfiguration: Branch-exchange switching cuts peak losses by 31.1% compared to base topology."
    ], title_color=ACCENT_TEAL, bullet_size=12)
    
    img7 = r"results\figures\grid_graph.png"
    if os.path.exists(img7):
        s7.shapes.add_picture(img7, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s7.notes_slide.notes_text_frame.text = (
        "Moving to Slide 7, we test how these forecasts interact with a physical distribution network. "
        "We modeled the IEEE 33-bus benchmark feeder using pandapower and NetworkX. We integrated 4 solar plants totaling 6 MW "
        "on a 3.7 MW feeder to intentionally induce reverse power flows. Graph analysis identified the optimal battery bus, and "
        "feeder reconfiguration demonstrated that optimal tie-switch selection alone reduces peak losses by 31%."
    )

    # -------------------------------------------------------------------------
    # SLIDE 8: Surrogate Machine Learning for Power Flow
    # -------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Surrogate Machine Learning for Real-Time Power Flow", "Surrogate Modeling [SIMULATED LABELS]")
    
    c_surr = add_card(s8, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_surr, "Fast Physics-Informed ML Surrogates", [
        "Training Dataset: 12,000 converged AC Newton-Raphson power flows across diverse load, solar, and battery conditions.",
        "Leak-Safe Target Formulation: No line voltages or flows used as features; only dispatchable injections and network IDs.",
        "Technical Loss Prediction: LightGBM achieves Test MAE = 12.2 kW and R² = 0.974.",
        "Substation Receiving Power (Bus 0): HistGradientBoosting achieves Test MAE = 21.1 kW and R² = 0.9996.",
        "Held-Out Generalization: Evaluated on unseen scenario families and verified against 886 fresh AC power flow simulations.",
        "Computational Advantage: Delivers 1,000x faster loss estimates than running full AC power flow."
    ], title_color=ACCENT_BLUE, bullet_size=12)
    
    img8 = r"results\figures\grid_receiving_power_pred_vs_sim.png"
    if os.path.exists(img8):
        s8.shapes.add_picture(img8, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 presents our surrogate machine learning models. Full non-linear AC power flow is computationally expensive. "
        "We trained surrogate regressors on 12,000 simulated scenarios. LightGBM predicts feeder technical losses with an R-squared of 0.974, "
        "and HistGradientBoosting predicts receiving-end power with an R-squared of 0.9996. These surrogates provide millisecond-speed "
        "loss estimations for operational monitoring."
    )

    # -------------------------------------------------------------------------
    # SLIDE 9: Forecast-Informed 24h LP Optimization Formulation
    # -------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Forecast-Informed 24-Hour Battery & Demand Optimization", "Optimization Engine [OPTIMISED]")
    
    c_opt = add_card(s9, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_opt, "Formulation & Real-World Execution", [
        "Mathematical Program: 24-hour Linear Program (LP) solved via HiGHS.",
        "Decision Variables: Battery charge/discharge (1.5 MW / 6 MWh), flexible load shift (±10%), and solar curtailment.",
        "Objective: Minimize total solar curtailment + weighted technical losses + peak grid import costs + evening ramp stress.",
        "Physical Constraints: Battery SoC dynamics, C-rate bounds, LinDistFlow branch voltage limits, and 1.0 MW export limit at bus 0.",
        "Two-Stage Operational Reality:",
        "1. Plan Stage: Day-ahead schedule built strictly using forecasted load & solar.",
        "2. Realization Stage: Schedule dispatched on actual realized solar & demand.",
        "Slack Tracking: Slacks record if forecast errors force constraint violations."
    ], title_color=ACCENT_PURPLE, bullet_size=12)
    
    img9 = r"results\figures\optimization_example_days.png"
    if os.path.exists(img9):
        s9.shapes.add_picture(img9, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.2))

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 explains our optimization formulation. We formulated a 24-hour Linear Program solved via HiGHS. "
        "The optimizer controls a 1.5 MW / 6 MWh battery, flexible load shifting, and solar curtailment under LinDistFlow voltage constraints. "
        "Crucially, the schedule is planned using the Day-Ahead forecast and then executed on the actual conditions. Slack variables "
        "were added to measure whether forecast inaccuracy would ever violate physical grid limits."
    )

    # -------------------------------------------------------------------------
    # SLIDE 10: Optimization Results & AC Power Flow Validation
    # -------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Optimization Results: 90.5% Curtailment Cut & Zero Violations", "Validation & Impact [OPTIMISED / AC-VALIDATED]")
    
    # 4 metric highlight cards across top
    m1 = add_card(s10, 0.8, 1.6, 2.7, 1.5, bg_color=RGBColor(240, 253, 244), border_color=ACCENT_GREEN)
    tf = m1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "-90.5%"; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = ACCENT_GREEN
    p2 = tf.add_paragraph(); p2.text = "Solar Curtailment Reduction\n(967.9 → 91.7 MWh)"; p2.font.size = Pt(11); p2.font.color.rgb = TEXT_DARK
    
    m2 = add_card(s10, 3.81, 1.6, 2.7, 1.5, bg_color=RGBColor(239, 246, 255), border_color=ACCENT_BLUE)
    tf = m2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "98.7%"; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = ACCENT_BLUE
    p2 = tf.add_paragraph(); p2.text = "Solar Utilization Rate\n(Up from 86.4% baseline)"; p2.font.size = Pt(11); p2.font.color.rgb = TEXT_DARK

    m3 = add_card(s10, 6.82, 1.6, 2.7, 1.5, bg_color=RGBColor(254, 243, 199), border_color=ACCENT_AMBER)
    tf = m3.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "-17.0%"; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = ACCENT_AMBER
    p2 = tf.add_paragraph(); p2.text = "Technical Feeder Losses\n(403.3 → 334.9 MWh)"; p2.font.size = Pt(11); p2.font.color.rgb = TEXT_DARK

    m4 = add_card(s10, 9.83, 1.6, 2.7, 1.5, bg_color=RGBColor(245, 243, 255), border_color=ACCENT_PURPLE)
    tf = m4.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "0 Hours"; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = ACCENT_PURPLE
    p2 = tf.add_paragraph(); p2.text = "Grid Violations\n(Zero voltage or thermal breaches)"; p2.font.size = Pt(11); p2.font.color.rgb = TEXT_DARK

    # Bottom detailed summary card
    c_tab = add_card(s10, 0.8, 3.3, 11.733, 3.5)
    add_card_text(c_tab, "Comprehensive Benchmark Over 167 Test Days (AC Newton-Raphson Validated)", [
        "Unprecedented Curtailment Relief: Slashes wasted solar energy from 967.9 MWh down to 91.7 MWh.",
        "Captures Perfect Foresight: Achieves 93.6% of the theoretical upper-bound curtailment reduction (91.7 vs 41.6 MWh).",
        "Substation Peak Shaving: Decreases average daily peak substation import from 2.67 MW to 2.02 MW (-24.3%).",
        "Evening Ramp Alleviation: Cuts the 3-hour evening grid import ramp from 1.95 MW to 1.45 MW (-25.6%).",
        "100% Physical Safety: Validated by full AC power flow—exactly 0 voltage violations and 0 thermal overload hours across all 167 test days.",
        "Zero Slack Activation: Forecast inaccuracy never pushed the distribution feeder outside operational limits."
    ], title_color=TEXT_DARK, bullet_size=12)

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 delivers our key breakthrough finding. Over 167 out-of-sample test days, validated through full non-linear AC power flow, "
        "the forecast-informed battery dispatch cut solar curtailment by 90.5%, raising solar utilization to 98.7%. "
        "It captured over 93% of the benefit of theoretical perfect foresight, reduced feeder losses by 17%, and shaved evening ramps by 25%. "
        "Most importantly, there were exactly zero voltage or thermal violations across all 167 days."
    )

    # -------------------------------------------------------------------------
    # SLIDE 11: Interactive Dashboard & Software Architecture
    # -------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Interactive Dashboard & Robust Software Engineering", "Software & Architecture")
    
    c_arch1 = add_card(s11, 0.8, 1.6, 3.65, 5.2)
    add_card_text(c_arch1, "Streamlit Dashboard", [
        "6-Page Interactive Web App:",
        "• Overview: SCADA telemetry, distributions, and summary statistics.",
        "• Forecasting: Real-time inference and model comparison charts.",
        "• Duck Curve: Seasonal ramps and surplus risk proxy scenarios.",
        "• Grid & Power Delivery: Interactive 33-bus feeder graph with live pandapower simulation.",
        "• Model Evaluation: Permutation importance and residual analysis."
    ], title_color=ACCENT_BLUE)
    
    c_arch2 = add_card(s11, 4.84, 1.6, 3.65, 5.2)
    add_card_text(c_arch2, "Modular Codebase", [
        "Clean Separation of Concerns:",
        "• src/data: Robust raw loaders & Hampel cleaners.",
        "• src/features: Leak-safe chronological builders.",
        "• src/models: Standardized estimator registry.",
        "• src/grid: NetworkX topology & pandapower runner.",
        "• src/optimization: HiGHS LP dispatch engine.",
        "• scripts/: 10 single-command CLI reproduction scripts."
    ], title_color=ACCENT_TEAL)
    
    c_arch3 = add_card(s11, 8.88, 1.6, 3.65, 5.2)
    add_card_text(c_arch3, "Testing & Verification", [
        "Industrial Testing Standards:",
        "• 40 Automated Pytest Tests verifying all components.",
        "• Test coverage spans data loaders, feature leakage guards, model persistence, AC power flow convergence, and UI rendering.",
        "• Deterministic reproducibility: Clean random seeds and pinned dependencies in requirements.txt.",
        "• Open Source MIT License."
    ], title_color=ACCENT_GREEN)

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 reviews our software architecture. The project is structured into a clean, modular Python package "
        "complemented by a multi-page interactive Streamlit dashboard. Users can inspect historical telemetry, compare forecast models, "
        "and simulate the 33-bus feeder in real-time. The entire repository is covered by 40 unit and integration tests, "
        "ensuring strict data integrity and mathematical correctness."
    )

    # -------------------------------------------------------------------------
    # SLIDE 12: Conclusions & Future Directions (Web3 Integration)
    # -------------------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Conclusions, Strategic Impact & Web3 Roadmap", "Synthesis & Future Vision")
    
    c_conc = add_card(s12, 0.8, 1.6, 5.6, 5.2)
    add_card_text(c_conc, "Key Academic & Engineering Conclusions", [
        "1. Bridged Macro & Micro: Proved that all-India transmission SCADA forecasts can directly inform physical distribution feeder stability.",
        "2. Solved Curtailment: Slashed curtailment by 90.5% while reducing peak imports (-24.3%) and evening ramps (-25.6%).",
        "3. Guaranteed Grid Safety: 100% compliance with zero voltage or thermal violations across 167 held-out test days.",
        "4. ML Hierarchy: Gradient boosted decision trees consistently outperformed deep recurrent architectures on tabular SCADA telemetry.",
        "5. Surrogate Efficiency: Physics-informed surrogate models enabled 1,000x faster loss and power flow evaluations."
    ], title_color=ACCENT_TEAL, bullet_size=12)
    
    c_future = add_card(s12, 6.93, 1.6, 5.6, 5.2)
    add_card_text(c_future, "Decentralized Energy & Web3 Roadmap", [
        "Peer-to-Peer (P2P) Microgrid Settlements:",
        "• Future work connects the optimization engine to decentralized energy markets.",
        "• Smart contracts execute automated curtailment compensation and battery dispatch.",
        "Web3 Infrastructure via thirdweb.com:",
        "• Utilizing developer tools from thirdweb.com to deploy smart contracts for tokenized Energy Attribute Certificates (EACs).",
        "• Physical SCADA telemetry mints verifiable carbon credits directly on-chain.",
        "Dynamic Tariff Oracles:",
        "• Net-load forecasts broadcast to decentralized price oracles to incentivize flexible consumer load shifting during steep ramps."
    ], title_color=ACCENT_AMBER, bullet_size=12)

    s12.notes_slide.notes_text_frame.text = (
        "In conclusion on Slide 12: SolarCast-Grid proves that machine learning forecasts can safely eliminate over 90% of solar curtailment "
        "in physical distribution grids without violating physical constraints. Looking forward, we plan to extend this framework into decentralized "
        "energy markets, using web3 smart contract infrastructure like thirdweb.com to automate peer-to-peer renewable settlements "
        "and mint verifiable on-chain energy attribute certificates backed directly by SCADA telemetry. Thank you, and I welcome your questions."
    )

    prs.save(output_path)
    print(f"Presentation successfully created and saved to: {output_path}")

if __name__ == "__main__":
    create_deck()
