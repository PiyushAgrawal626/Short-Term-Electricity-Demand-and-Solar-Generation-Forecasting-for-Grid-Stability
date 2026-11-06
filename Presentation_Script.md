# Presentation Script & Speaker Notes

**Project Title:** Short-Term Electricity Demand and Solar Generation Forecasting for Grid Stability  
**Presenter:** Piyush Agrawal  
**Framework:** SolarCast-Grid  
**Total Slides:** 12 Slides (Widescreen 16:9)  
**Estimated Time:** 12 – 15 Minutes (plus Q&A)

---

## ⏱️ Presentation Timing & Slide Breakdown

| Slide # | Slide Title | Category | Target Time | Key Takeaway |
|:---:|---|---|:---:|---|
| **1** | Title Slide | Title | 1:00 min | Project vision and scope |
| **2** | The Challenge: Solar Intermittency & Grid Bottlenecks | Motivation | 1:15 min | Duck curve & feeder reverse flow |
| **3** | Grid-India SCADA Telemetry & Ingestion Pipeline | Data Engineering | 1:15 min | 4.07M samples, leak-safe cleaning |
| **4** | Empirical Duck Curve Dynamics & Surplus-Solar Risk Proxy | Grid Dynamics | 1:15 min | Midday dip to 13:00, 33 GW ramp |
| **5** | Multi-Horizon Machine Learning Forecasting Framework | Methodology | 1:15 min | 8 tasks, issue-time aware features |
| **6** | Forecasting Benchmark: Tree Ensembles Dominate Sequences | Results | 1:15 min | LightGBM/XGBoost beat baselines |
| **7** | Distribution Grid Simulation: IEEE 33-Bus Feeder | Power Systems | 1:15 min | pandapower, graph topology, 31% loss cut |
| **8** | Surrogate Machine Learning for Real-Time Power Flow | Surrogate ML | 1:00 min | 1,000x faster loss predictions ($R^2=0.974$) |
| **9** | Forecast-Informed 24-Hour Battery & Demand Optimization | Optimization | 1:15 min | HiGHS LP + LinDistFlow constraints |
| **10** | Optimization Results: 90.5% Curtailment Cut & Zero Violations | Validation | 1:30 min | 90.5% curtailment cut, 0 violations |
| **11** | Interactive Dashboard & Robust Software Engineering | Architecture | 1:00 min | Streamlit web app, 40 passed tests |
| **12** | Conclusions, Strategic Impact & Web3 Roadmap | Vision | 1:15 min | Key takeaways, thirdweb.com P2P settlement |

---

## 🎙️ Slide-by-Slide Narration Script

### Slide 1: Title Slide
* **Visual:** Dark navy background with solar amber accent bar, project title, and scientific provenance tags (`[OBSERVED]`, `[DERIVED]`, `[FORECAST]`, `[SIMULATED]`, `[OPTIMISED]`).
* **Speaker Script:**  
  > *"Good morning respected professors, evaluators, and colleagues. Today I am presenting my project titled **'Short-Term Electricity Demand and Solar Generation Forecasting for Grid Stability'**, built upon the SolarCast-Grid framework.*  
  >  
  > *As our power grid shifts rapidly toward clean energy, the central engineering challenge is no longer just generating green power—it is managing renewable intermittency and preserving physical grid stability. In this project, we bridge macro-scale transmission telemetry from Grid-India with micro-scale physical distribution feeder stability, demonstrating that machine learning forecasts can reliably drive physical battery storage to eliminate solar curtailment without violating a single grid constraint."*
* **Transition:** *"To understand why this is so critical, let's examine the emerging challenges facing both national transmission and local distribution systems."*

---

### Slide 2: The Challenge: Solar Intermittency & Grid Bottlenecks
* **Visual:** Three structured analytical cards: Macro Solar Influx, The Indian Duck Curve, and Local Feeder Crisis.
* **Speaker Script:**  
  > *"Slide 2 illustrates the two interconnected sides of the clean energy transition.  
  > At the macro transmission level, solar energy's share of India's daily electricity demand grew from 6.4% in 2021 to 9.3% in recent years. This influx creates the famous 'Duck Curve': midday net demand plunges when the sun is shining, followed by a punishing evening ramp when solar generation drops off just as residential demand peaks. In 2025, India's mean evening 3-hour ramp reached 33.2 GW, with a record single-day peak of 50.6 GW.  
  > Simultaneously, at the local distribution level, high concentrations of distributed solar create reverse power flows back toward substations. This leads to severe over-voltages and line congestion, forcing utilities to curtail clean energy. Our central research question is: **Can macro SCADA forecasts reliably guide local battery dispatch to solve curtailment while maintaining 100% physical grid compliance?**"*
* **Transition:** *"To answer this with scientific rigor, we turned to real-world SCADA telemetry from Grid-India."*

---

### Slide 3: Grid-India SCADA Telemetry & Ingestion Pipeline
* **Visual:** Data engineering breakdown card on the left, paired with the hourly multi-year profile plot on the right.
* **Speaker Script:**  
  > *"On Slide 3, we present our data engineering foundation. We obtained 4,075,224 raw SCADA telemetry points from Grid-India via Mendeley Data, spanning September 2021 through June 2025.  
  > Rather than relying on simple averages or synthetic data, we designed a leak-safe preprocessing pipeline:  
  > 1. We applied a Hampel outlier filter using rolling medians and median absolute deviation (MAD) at raw resolution to suppress sensor spikes.  
  > 2. We eliminated nocturnal transducer drift by zeroing 11,144 nighttime solar hours.  
  > 3. We resampled the data to hourly mean MW, which preserves exact energy consistency where 1 MW for 1 hour equals 1 MWh.  
  > 4. Finally, we enforced strict chronological train, validation, and test splits with zero future lookahead bias."*
* **Transition:** *"With this clean dataset, our first objective was to quantify the evolution of the Indian Duck Curve."*

---

### Slide 4: Empirical Duck Curve Dynamics & Surplus-Solar Risk Proxy
* **Visual:** Analytical summary of net-load shifts paired with the seasonal duck curve graph.
* **Speaker Script:**  
  > *"Slide 4 shows the empirical duck curve dynamics derived from the SCADA data.  
  > Notice the diurnal inversion: in 2021, the daily net-load minimum occurred at 3:00 AM. By 2022 and onward, the minimum permanently shifted to 1:00 PM in the middle of the day. The evening ramp starting at 4:00 PM now demands unprecedented ramping speed from conventional generators.  
  > To evaluate future risks, we formulated a Surplus-Solar Risk Proxy incorporating CEA technical minimum operating floors for thermal and nuclear power. We found that while today's fleet (k=1) has virtually zero surplus, scaling solar capacity by 2x produces surplus energy, and at 3x solar buildout, surplus surges to 9.15% of total solar energy. This mathematically proves that storage and active demand management are indispensable."*
* **Transition:** *"To manage this variability, we built a comprehensive multi-horizon machine learning forecasting suite."*

---

### Slide 5: Multi-Horizon Machine Learning Forecasting Framework
* **Visual:** Three-column architecture highlighting Targets & Horizons, Leak-Safe Features, and Model Benchmarks.
* **Speaker Script:**  
  > *"Slide 5 outlines our forecasting architecture. We benchmarked 8 core tasks: Solar Generation, Electricity Demand, Wind Generation, and Net Load across two operational horizons:  
  > - **1-Hour Ahead (h=1)** for real-time dispatch and frequency regulation.  
  > - **Day-Ahead (leads of 14 to 37 hours)**, mirroring actual power exchange operations where the 24-hour schedule for Day D+1 must be finalized by 10:00 AM on Day D.  
  > All features are strictly issue-time aware—including trigonometric calendar harmonics, multi-day autoregressive lags (24h, 48h, 168h), rolling statistical windows, and a rolling 30-day maximum capacity growth proxy. We evaluated baseline persistence, linear Ridge regression, Random Forest, HistGradientBoosting, LightGBM, XGBoost, and deep PyTorch LSTM sequence networks."*
* **Transition:** *"Let's look at how these models performed on out-of-sample test data."*

---

### Slide 6: Forecasting Benchmark Results & Key Insights
* **Visual:** Key metrics and findings on the left, paired with the model comparison benchmark chart on the right.
* **Speaker Script:**  
  > *"Slide 6 summarizes our forecasting results on the unseen test period (January to June 2025).  
  > Two major insights emerged:  
  > First, **gradient-boosted decision trees dominated the benchmark**. LightGBM achieved the best performance across all 1-hour ahead tasks, beating persistence baselines by 47% on solar, 67.6% on demand, and 67.7% on net load, with a 1-hour solar test MAE of just 559 MW. For day-ahead forecasting, HistGradientBoosting and XGBoost were selected, achieving an R² of 0.988 for solar and 0.887 for demand.  
  > Second, **tree ensembles consistently outperformed the deep LSTM network**. In tabular hourly power systems where lagged and harmonic features can be explicitly engineered, tree-based gradient boosting models generalize better and train in minutes rather than hours. Furthermore, incorporating numerical weather forecasts improved day-ahead solar MAE by 10.5%."*
* **Transition:** *"Having established accurate forecasts, we next simulated how power flows across a physical distribution network."*

---

### Slide 7: Distribution Feeder Simulation: IEEE 33-Bus Feeder
* **Visual:** Power systems parameterization card paired with the IEEE 33-bus NetworkX topological diagram.
* **Speaker Script:**  
  > *"On Slide 7, we introduce our distribution grid environment. We parameterized the standard IEEE/Baran-Wu 33-bus 12.66 kV radial distribution feeder in pandapower and NetworkX.  
  > The feeder serves a base peak load of 3.715 MW. To simulate heavy renewable stress, we integrated 4 distributed solar generation plants totaling 6.0 MW—representing a 161% solar penetration that causes substantial reverse power flow.  
  > Using NetworkX graph analysis, we mapped 50,751 valid radial configurations. We performed graph betweenness and electrical distance sensitivity to determine bus 14 as the optimal battery location, and showed that optimal branch-exchange tie-switch reconfiguration cuts peak feeder losses by 31.1%."*
* **Transition:** *"Because running 100,000 AC power flows in real-time is computationally demanding, we developed surrogate machine learning models."*

---

### Slide 8: Surrogate Machine Learning for Real-Time Power Flow
* **Visual:** Surrogate ML methodology card paired with the predicted vs simulated power scatter plot.
* **Speaker Script:**  
  > *"Slide 8 highlights our physics-informed surrogate machine learning models. We generated 12,000 non-linear AC Newton-Raphson power flow scenarios across varying solar injections, load scales, and battery states.  
  > We trained fast surrogate regressors to predict technical feeder losses and substation receiving power at bus 0. We enforced strict data hygiene: no voltages or internal line flows were used as inputs, preventing target leakage.  
  > LightGBM predicted technical losses with a test MAE of just 12.2 kW and an R² of 0.974. HistGradientBoosting predicted receiving-end power with an R² of 0.9996. These surrogates evaluate feeder conditions over 1,000 times faster than full AC Newton-Raphson solvers, making them ideal for high-speed digital twin monitoring."*
* **Transition:** *"Now, we combine our day-ahead forecasts with our feeder model in our 24-hour optimization engine."*

---

### Slide 9: Forecast-Informed 24-Hour Battery & Demand Optimization
* **Visual:** Optimization formulation card paired with the 24-hour battery schedule and load dispatch plot.
* **Speaker Script:**  
  > *"Slide 9 presents our core optimization engine. We formulated a 24-hour Linear Program (LP) solved with HiGHS.  
  > The decision variables control a 1.5 MW / 6 MWh battery storage system, flexible load shifting within a ±10% band, and solar curtailment. The objective function minimizes solar curtailment while penalizing feeder losses, peak substation imports, and evening ramps.  
  > Crucially, the model incorporates LinDistFlow linearised branch power and voltage constraints, plus a 1.0 MW export limit at the substation.  
  > In practice, the schedule is planned at 10:00 AM using the Day-Ahead forecast, and then dispatched during the real day under actual weather conditions. We introduced slack variables to honestly detect if forecast errors would cause voltage or thermal violations."*
* **Transition:** *"The critical question is: how did this forecast-informed dispatch perform across the entire test period?"*

---

### Slide 10: Optimization Results: 90.5% Curtailment Cut & Zero Violations
* **Visual:** Four high-impact metric cards (-90.5% Curtailment, 98.7% Solar Utilization, -17.0% Losses, 0 Hours Violations) and comprehensive benchmark table.
* **Speaker Script:**  
  > *"Slide 10 delivers our most significant experimental finding. We evaluated every single day across 167 out-of-sample test days and validated every single hour with full non-linear AC Newton-Raphson power flow.  
  > The results are definitive:  
  > 1. **Solar Curtailment dropped by 90.5%**, from 967.9 MWh in the unmanaged baseline down to just 91.7 MWh. This captured **93.6%** of the curtailment reduction attainable under theoretical perfect foresight!  
  > 2. **Solar Utilization rose to 98.7%**, up from 86.4%.  
  > 3. **Technical Feeder Losses decreased by 17.0%**, from 403.3 MWh to 334.9 MWh.  
  > 4. **Peak Grid Import dropped by 24.3%**, and the evening import ramp was reduced by **25.6%**.  
  > 5. Most importantly: **Zero voltage violations and zero thermal overload hours** were recorded across all 167 days. The forecast-informed schedule maintained 100% physical grid compliance without once activating penalty slack variables."*
* **Transition:** *"To make these models accessible and verifiable, we built a comprehensive software platform."*

---

### Slide 11: Interactive Dashboard & Robust Software Engineering
* **Visual:** Three architecture pillars: Streamlit Dashboard, Modular Codebase, and Pytest Verification Suite.
* **Speaker Script:**  
  > *"Slide 11 details our software engineering and interactive application. We engineered a modular, decoupled Python codebase structured into distinct modules for data cleaning, feature engineering, model inference, grid simulation, and LP optimization.  
  > We built a multi-page interactive Streamlit dashboard that allows grid operators to explore SCADA telemetry, inspect forecasting residuals, analyze duck curve ramps, and simulate the 33-bus feeder in real time.  
  > The entire codebase is verified through an automated test suite of 40 unit and integration tests covering everything from feature leak guards to AC power flow convergence, all published under an open-source MIT license."*
* **Transition:** *"Let us conclude by summarizing our main findings and outlining future directions."*

---

### Slide 12: Conclusions, Strategic Impact & Web3 Roadmap
* **Visual:** Two balanced cards: Key Academic Conclusions on the left; Decentralized Energy & Web3 Roadmap on the right.
* **Speaker Script:**  
  > *"In conclusion on Slide 12:  
  > This project demonstrates that macro-level SCADA machine learning forecasts can directly and safely inform micro-level distribution storage dispatch, cutting solar curtailment by 90.5% with zero grid violations. It proves that tree-based ensembles are superior to recurrent networks for tabular SCADA data, and that surrogate ML models can accelerate physical power flow simulations by orders of magnitude.  
  > Looking toward the future of decentralized power grids, we are expanding this framework into peer-to-peer microgrid settlements. By leveraging web3 developer platforms like **thirdweb.com**, we can deploy smart contracts that automate curtailment compensation, settle peer-to-peer clean energy trades, and tokenize verifiable Energy Attribute Certificates (EACs) and carbon credits backed directly by authenticated SCADA telemetry.  
  > Thank you for your time and attention. I am now open to your questions."*

---

## 💡 Anticipated Questions & Defensible Answers

### Q1: Why did tree ensembles (LightGBM/XGBoost) beat the deep LSTM sequence model?
**Answer:**  
*"Power system SCADA telemetry at an hourly resolution exhibits strong tabular characteristics with pronounced calendar and lag structures (such as 24-hour and 168-hour seasonalities). By engineering explicit trigonometric harmonics, rolling windows, and capacity proxies, gradient boosted decision trees can partition the feature space efficiently without requiring huge volumes of sequential parameters. Recurrent neural networks like LSTMs typically require significantly more data to learn diurnal patterns that tree models capture natively from lagged features."*

### Q2: How did you ensure there was no data leakage in the Day-Ahead forecasts?
**Answer:**  
*"In India's Day-Ahead power market, market participants submit their schedules on Day D by 10:00 AM IST for the entire 24 hours of Day D+1. Therefore, any forecast issued for hour t of Day D+1 has an effective lead time between 14 and 37 hours. Our feature pipeline strictly filters out any telemetry recorded after 10:00 AM on Day D, ensuring zero lookahead bias and 100% adherence to real-world power market timelines."*

### Q3: Why did you use an LP with LinDistFlow instead of an AC Optimal Power Flow (AC-OPF)?
**Answer:**  
*"Full AC-OPF is a non-convex, non-linear optimization problem that frequently encounters convergence difficulties or local minima when solved across a multi-period 24-hour horizon with battery state transitions. A Linear Program using LinDistFlow approximations is convex, guaranteed to solve to global optimality within milliseconds using HiGHS, and auditable. Crucially, we didn't just assume the LP was valid—we re-simulated every single planned schedule in full non-linear AC Newton-Raphson power flow using pandapower, proving that the linear approximation resulted in zero real-world AC violations."*

### Q4: How does thirdweb.com fit into a power systems and ML project?
**Answer:**  
*"As distribution feeders transition into active microgrids with multiple rooftop solar prosumers and community battery systems, centralized accounting becomes a bottleneck. Thirdweb provides developer infrastructure for deploying custom EVM smart contracts. In our future roadmap, the forecast-informed dispatch engine can broadcast schedules to on-chain smart contracts that automatically credit prosumers for battery storage, settle peer-to-peer energy trades, and mint verifiable digital Energy Attribute Certificates (EACs) anchored directly to real SCADA metering data."*
